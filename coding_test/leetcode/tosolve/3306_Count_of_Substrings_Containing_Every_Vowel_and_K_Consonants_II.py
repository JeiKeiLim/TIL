from tester import Tester, generate_random_string

"""
You are given a string word and a non-negative integer k.
Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:
Input: word = "aeioqq", k = 1
Output: 0

Example 2:
Input: word = "aeiou", k = 0
Output: 1

Example 3:
Input: word = "ieaouqqieaouqq", k = 1
Output: 3


Constraints:
1. 5 <= word.length <= 2 * 10^5
2. word consists only of lowercase English letters.
3. 0 <= k <= word.length - 5
"""


class Solution:
    def countSubstrings(self, word: str, k: int) -> int:
        vowel_map = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        n = len(word)
        n_consonant = 0
        i = 0
        answer = 0
        for j in range(n):
            if word[j] in vowel_map:
                vowel_map[word[j]] += 1
            else:
                n_consonant += 1

            if n_consonant < k:
                continue

            while n_consonant > k:
                if word[i] in vowel_map:
                    vowel_map[word[i]] -= 1
                else:
                    n_consonant -= 1
                i += 1

            while n_consonant == k and sum(val > 0 for val in vowel_map.values()) == 5:
                answer += 1
                if word[i] in vowel_map:
                    vowel_map[word[i]] -= 1
                else:
                    n_consonant -= 1
                i += 1

            # if n_consonant == k and sum(val > 0 for val in vowel_map.values()) == 5:
            #     answer += 1

        # for j in range(i, -1, -1):
        #     if word[j] in vowel_map:
        #         vowel_map[word[j]] -= 1
        #         if vowel_map[word[j]] == 0:
        #             break
        #         else:
        #             answer += 1
        #     else:
        #         break

        return answer


if __name__ == "__main__":
    tests = [
        ["aeioqq", 1],
        ["aeiou", 0],
        ["ieaouqqieaouqq", 1],
        ["iqeaouqi", 2],
        ["aeueio", 0],
        ["aadieuoh", 1],
        ["ieaiouqq", 1],
        [generate_random_string(2 * 10**5), 10000],
    ]
    answers = [0, 1, 3, 3, 1, 2, 2, 0]

    tester = Tester(Solution().countSubstrings)
    tester.test(tests, answers)
