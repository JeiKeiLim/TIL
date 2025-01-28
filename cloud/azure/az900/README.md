This note is based on the course AI-900: Microsoft Azure Fundamentals from Udemy https://www.udemy.com/course/best-ai-900-fundamentals


- Official website: https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/?practice-assessment-type=certification

# Section1
## 1. Azure AI services

1. Vision services
2. Speech services
3. Language services
4. Decision services

# Section2 - Describe AI workloads and considerations (15-20%)
## 2.1. Types of AI workloads

1. Prediction and Demand Forecasting
2. Anomaly Detection
3. Computer Vision
4. Natural Language Processing
5. Conversational AI

## 2.2. Guiding principles in AI
### 2.2.1. Unintended consequences

- Wrong decisions
- Illegal
- Cannot be explained
- Harmful
- Bias

## 2.3. 6 Principles of Responsible AI

1. Fairness
2. Reliability and Safety
3. Privacy and Security
4. Inclusiveness
5. Transparency
6. Accountability


### 2.3.1. Principles of Fairness

- Bank loan approval
- Hiring

### 2.3.2. Principles of Reliability and Safety

- Self-driving cars
- Medical diagnosis

### 2.3.3. Principles of Privacy and Security

- Data privacy
- Data security
- Targetted advertising might be considered as a privacy violation

### 2.3.4. Principles of Inclusiveness

- Accessibility to everyone
- Speech impairment
- Visual impairment
- ...

### 2.3.5. Principles of Transparency

- Explainability
- Ex) loan rejection needs to be explained

### 2.3.6. Principles of Accountability

- Who is responsible for the AI system?

# Section 3 - Describe fundamental principles of machine learning on Azure (20-25%)

# Section 4 - Core Machine Learning Tasks

1. Data Ingestion
    - Azure Data Factory
    - Azure ML Python SDK
    - Upload data to Azure storage
2. Data Preparation
    2.1. Data cleaning
    2.2. Data transformation
        - Parquet, CSV
        - Pandas
        - Ray, Dask, Spark
    2.3. Create a datastore in Azure ML
    2.4. Create a dataset in Azure ML
    2.5. Register a dataset in Azure ML

3. Model Training
    - AutoML
    - ML Designer: Choose algorithm to use
    - Evaluation
4. Model evaluation
    - Classification
        - Confusion matrix
        - Precision, Recall
            - Recall (TP / (TP+FN)), Precision (TP / (TP+FP))
        - F1 score
        - ROC curve
        - AUC
        - Accuracy
    - Regression
        - Mean Absolute Error (MAE)
        - Mean Squared Error (MSE)
        - Root Mean Squared Error (RMSE)
        - R-squared
    - Cross-validation
5. Model Deployment

# Section 5 - No code machine learning
## 5.1. Azure AutoML
  1. Identify the problem - Classification, Regression, Time Series Forecasting
  2. Choose the environment - Python SDK or ML Studio
  3. Specify the dataset
  4. Configure the compute
  5. Configure the AutoML parameters
  6. Submit a training run
  7. Review the results

# Section 6 - Computer vision workloads with Azure (15-20%)

## 6.1. Azure Computer vision

- Pre-trained ML model
- Classification, Object detection, Captioning, OCR, Face detection

## 6.2. Azure Custom Vision

- Classification 
- Object detection

## 6.3. Azure Cognitive Services

- Facial recognition
- Image analysis
- Spatial analysis
- Optical character recognition (OCR)


# Section 7 - Natural Language Processing workloads with Azure (15-20%)

# Basic steps to text analysis

1. Tokenization
    - Text normalization: Removing punctuation, lowercasing
    - Stop words removal: Removing common words (the, a, an, ...)
    - n-grams: Group of n words (I, We, You, ...)
    - Stemming: Removing suffixes (ing, ed, ...)
    - Lemmatization: Reducing words to their base form (running -> run)
2. Frequency analysis
    - Count the frequency of words

# Azure AI Language Services

- Named Entity Recognition
- Entity Linking
- Personally Identifiable Information (PII)
- Language Detection
- Sentiment analysis and Opinion Mining
- Summarization
- Key Phrase Extraction


## 7.1. Basic NLP concepts

### 7.1.1. Key phrase extraction
- Identify the main points in a text

### 7.1.2. Entity recognition

- Identify entities in a text

### 7.1.3. Sentiment analysis

- Determine the sentiment of a text

### 7.1.4. Language detection

- Identify the language of a text

### 7.1.5. Language Modeling

### 7.1.6. Speech recognition and synthesis

### 7.1.7. Translation

## 7.2. Azure NLP services

- Text Analytics
- Language Understanding
    - Uttterance
    - Intent
    - Entity
- Speech
    - Speech to text
    - Text to speech
    - Audio translation
- Translator

# Section 8 - Generative AI workloads with Azure (15-20%)
## 8.1. Types of generative AI

1. Natural Language Generation
2. Image Generation
3. Code Generation
