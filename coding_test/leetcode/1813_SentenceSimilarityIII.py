from tester import Tester  # Assuming you have a Tester class for running tests

"""
1813. Sentence Similarity III
Medium

You are given two strings `sentence1` and `sentence2`, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

### Example 1:
Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

### Example 2:
Input: sentence1 = "of", sentence2 = "A lot of words"
Output: false
Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.

### Example 3:
Input: sentence1 = "Eating right now", sentence2 = "Eating"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

### Constraints:
- 1 <= sentence1.length, sentence2.length <= 100
- sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
- The words in sentence1 and sentence2 are separated by a single space.
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        split_s1 = sentence1.split(" ")
        split_s2 = sentence2.split(" ")

        if len(split_s1) > len(split_s2):
            longer, shorter = split_s1, split_s2
        else:
            longer, shorter = split_s2, split_s1

        eq_beg = -1
        for i in range(len(shorter)):
            if longer[i] == shorter[i]:
                eq_beg = i
            else:
                break

        if eq_beg + 1 == len(shorter):
            return True

        eq_end = -1
        for i in range(len(shorter) - (eq_beg + 1)):
            idx_s = len(shorter) - i - 1
            idx_l = len(longer) - i - 1

            if shorter[idx_s] == longer[idx_l]:
                eq_end = i
            else:
                break

        return (eq_beg + eq_end + 2) == len(shorter)


if __name__ == "__main__":
    # Test cases
    tests = [
        ["My name is Haley", "My Haley"],  # Example 1
        ["of", "A lot of words"],  # Example 2
        ["Eating right now", "Eating"],  # Example 3
    ]
    answers = [
        True,  # Expected output for Example 1
        False,  # Expected output for Example 2
        True,  # Expected output for Example 3
    ]

    tester = Tester(Solution().areSentencesSimilar)
    tester.test(tests, answers)
