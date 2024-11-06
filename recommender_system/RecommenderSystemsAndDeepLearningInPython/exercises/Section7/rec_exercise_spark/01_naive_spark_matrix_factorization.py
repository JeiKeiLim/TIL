from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import SparkContext
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = (
        SparkSession.builder.master("local[*]")
        .appName("MatrixFactorization")
        .config("spark.driver.memory", "32g")
        .getOrCreate()
    )
    sc = spark.sparkContext
    # SparkContext.setSystemProperty("spark.driver.memory", "16g")
    # SparkContext.setSystemProperty("spark.executor.memory", "16g")
    # sc = SparkContext("local", "MatrixFactorization")

    data = sc.textFile("/home/user/Datasets/MovieLens20M/rating.csv")
    header = data.first()

    data = data.filter(lambda row: row != header)

    ratings = data.map(lambda l: l.split(",")).map(
        lambda l: Rating(int(l[0]), int(l[1]), float(l[2]))
    )

    train, test = ratings.randomSplit([0.8, 0.2])

    print(
        f"# of ratings: {ratings.count()}, (Train, Test) {train.count()}, {test.count()}"
    )

    K = 10
    epochs = 10
    model = ALS.train(train, K, epochs)

    x = train.map(lambda p: (p[0], p[1]))
    p = model.predictAll(x).map(lambda r: ((r[0], r[1]), r[2]))
    ratesAndPreds = train.map(lambda r: ((r[0], r[1]), r[2])).join(p)

    mse = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1]) ** 2).mean()
    print("(Train) Mean Squared Error = " + str(mse))

    x = test.map(lambda p: (p[0], p[1]))
    p = model.predictAll(x).map(lambda r: ((r[0], r[1]), r[2]))
    ratesAndPreds = test.map(lambda r: ((r[0], r[1]), r[2])).join(p)

    mse = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1]) ** 2).mean()
    print("(Test) Mean Squared Error = " + str(mse))
