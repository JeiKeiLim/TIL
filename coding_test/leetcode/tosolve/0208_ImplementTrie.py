from tester import Tester  # Assuming you have a Tester class for running tests

"""
208. Implement Trie (Prefix Tree)
Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

### Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

### Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, True, False, True, null, True]

Explanation:
- Trie trie = new Trie();
- trie.insert("apple");
- trie.search("apple");   // return True
- trie.search("app");     // return False
- trie.startsWith("app"); // return True
- trie.insert("app");
- trie.search("app");     // return True

### Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
"""


class Trie:

    def __init__(self):
        pass  # To be implemented

    def insert(self, word: str) -> None:
        pass  # To be implemented

    def search(self, word: str) -> bool:
        pass  # To be implemented

    def startsWith(self, prefix: str) -> bool:
        pass  # To be implemented


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    # Test cases
    tests = [
        (
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
        ),  # Example 1
    ]
    answers = [
        [None, None, True, False, True, None, True],  # Expected output for Example 1
    ]

    tester = Tester(
        Trie
    )  # Assuming Tester is available for testing class-based problems
    tester.test(tests, answers)
