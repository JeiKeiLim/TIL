from tester import Tester  # Assuming you have a Tester class for running tests

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
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        pass  # To be implemented


if __name__ == "__main__":
    # Test cases
    tests = [
        (["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"),  # Example 1
        (["havana"], "havana"),  # Example 2
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

    tester = Tester(Solution().suggestedProducts)
    tester.test(tests, answers)
