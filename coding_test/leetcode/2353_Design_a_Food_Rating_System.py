from tester import Tester

"""
Design a food rating system that can do the following:
• Modify the rating of a food item listed in the system.
• Return the highest-rated food item for a type of cuisine in the system.

Implement the FoodRatings class:

• FoodRatings(String[] foods, String[] cuisines, int[] ratings)
  Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
  • foods[i] is the name of the ith food,
  • cuisines[i] is the type of cuisine of the ith food, and
  • ratings[i] is the initial rating of the ith food.

• void changeRating(String food, int newRating)
  Changes the rating of the food item with the name food.

• String highestRated(String cuisine)
  Returns the name of the food item that has the highest rating for the given type of cuisine.
  If there is a tie, return the item with the lexicographically smaller name.

Note:
A string x is lexicographically smaller than string y if x comes before y in dictionary order,
that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i],
then x[i] comes before y[i] in alphabetic order.

Example 1:
Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
  ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
  [9, 12, 8, 15, 14, 7]],
 ["korean"],
 ["japanese"],
 ["sushi", 16],
 ["japanese"],
 ["ramen", 16],
 ["japanese"]]

Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(
    ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
    ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
    [9, 12, 8, 15, 14, 7]
);
foodRatings.highestRated("korean"); // return "kimchi"
foodRatings.highestRated("japanese"); // return "ramen"
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16
foodRatings.highestRated("japanese"); // return "sushi"
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16
foodRatings.highestRated("japanese"); // return "ramen"

Constraints:
• 1 <= n <= 2 * 10^4
• n == foods.length == cuisines.length == ratings.length
• 1 <= foods[i].length, cuisines[i].length <= 10
• foods[i], cuisines[i] consist of lowercase English letters.
• 1 <= ratings[i] <= 10^8
• All the strings in foods are distinct.
• food will be the name of a food item in the system across all calls to changeRating.
• cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
• At most 2 * 10^4 calls in total will be made to changeRating and highestRated.
"""
import heapq
from collections import defaultdict


class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_ratings = {}
        self.foods_to_cuisines = {}
        self.cuisine_ratings = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_ratings[food] = rating
            self.foods_to_cuisines[food] = cuisine
            heapq.heappush(self.cuisine_ratings[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating
        cuisine = self.foods_to_cuisines[food]
        heapq.heappush(self.cuisine_ratings[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_ratings[cuisine]
        # Pop outdated ratings from the top of the heap
        while heap and -heap[0][0] != self.food_ratings[heap[0][1]]:
            heapq.heappop(heap)
        return heap[0][1]


def evaluate(actions: list[str], inputs: list[list]) -> list[str | None]:
    food_ratings = FoodRatings(*inputs[0])
    answer: list[str | None] = [None] * len(actions)

    for i, action in enumerate(actions):
        result = None
        if i == 0:
            pass
        elif action == "changeRating":
            food_ratings.changeRating(*inputs[i])
        else:
            result = food_ratings.highestRated(*inputs[i])
        answer[i] = result

    return answer


if __name__ == "__main__":
    actions = [
        "FoodRatings",
        "highestRated",
        "highestRated",
        "changeRating",
        "highestRated",
        "changeRating",
        "highestRated",
    ]
    inputs = [
        [
            ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
            ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
            [9, 12, 8, 15, 14, 7],
        ],
        ["korean"],
        ["japanese"],
        ["sushi", 16],
        ["japanese"],
        ["ramen", 16],
        ["japanese"],
    ]
    expected = [[None, "kimchi", "ramen", None, "sushi", None, "ramen"]]

    tester = Tester(evaluate)
    tester.test([[actions, inputs]], expected)
