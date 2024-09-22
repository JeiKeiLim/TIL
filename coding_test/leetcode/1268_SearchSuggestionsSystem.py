from tester import Tester  # Assuming you have a Tester class for running tests

from typing import List

"""
1268. Search Suggestions System
Medium

You are given an array of strings `products` and a string `searchWord`.

Design a system that suggests at most three product names from `products` after each character of `searchWord` is typed. Suggested products should have a common prefix with `searchWord`. If there are more than three products with a common prefix, return the three lexicographically minimum products.

Return a list of lists of the suggested products after each character of `searchWord` is typed.

### Example 1:
Input: products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

### Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

### Constraints:
- 1 <= products.length <= 1000
- 1 <= products[i].length <= 3000
- 1 <= sum(products[i].length) <= 2 * 10^4
- All strings of `products` are unique.
- `products[i]` consists of lowercase English letters.
- 1 <= searchWord.length <= 1000
- `searchWord` consists of lowercase English letters.
"""


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        """
        Started @ 08:13
        Ended @ 08:19

        O(nm^2) solution
        """
        result = []
        products.sort()
        for i in range(1, len(searchWord) + 1):
            current_search = searchWord[:i]
            current_result = []
            for prod in products:
                if prod[:i] == current_search:
                    current_result.append(prod)

                if len(current_result) == 3:
                    break

            result.append(current_result)

        return result

    def suggestedProducts2(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        """
        Started @ 08:20
        Ended @ 08:29

        Also O(nm)
        """
        result = [[] for _ in range(len(searchWord))]
        products.sort()

        for prod in products:
            for i in range(len(searchWord)):
                if i < len(prod) and prod[i] == searchWord[i]:
                    if len(result[i]) < 3:
                        result[i].append(prod)
                else:
                    break

        return result


if __name__ == "__main__":
    # Test cases
    tests = [
        [["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"],  # Example 1
        [["havana"], "havana"],  # Example 2
    ]
    answers = [
        [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
        ],  # Expected output for Example 1
        [
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
        ],  # Expected output for Example 2
    ]

    tester = Tester(Solution().suggestedProducts2)
    tester.test(tests, answers)
