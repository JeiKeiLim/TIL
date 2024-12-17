from tester import Tester

from typing import List

"""
You are given a string word and an integer k.

We consider word to be k-special if |freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string.

Here, freq(x) denotes the frequency of the character x in word, and |y| denotes the absolute value of y.

Return the minimum number of characters you need to delete to make word k-special.

Example 1:
Input: word = "aabcaba", k = 0
Output: 3

Example 2:
Input: word = "dabdcbdcdcd", k = 2
Output: 2

d: 5
a: 1
b: 2
c: 3

Example 3:
Input: word = "aaabaaa", k = 2
Output: 1

Constraints:
1 <= word.length <= 10^5
0 <= k <= 10^5
word consists only of lowercase English letters.
"""


class Solution:
    def minDeletionsToMakeKSpecial2(self, word: str, k: int) -> int:
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        freq_vals = sorted(freq.values())

        memo = {}

        def backtrace(i: int, j: int) -> int:
            if abs(freq_vals[i] - freq_vals[j]) <= k:
                return 0

            if (i, j) not in memo:
                di = freq_vals[i] + backtrace(i + 1, j)
                dj = freq_vals[j] - freq_vals[i] - k + backtrace(i, j - 1)

                memo[(i, j)] = min(di, dj)

            return memo[(i, j)]

        return backtrace(0, len(freq_vals) - 1)

    def minDeletionsToMakeKSpecial(self, word: str, k: int) -> int:
        """
        Started @ 09:23
        """
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1

        freq_vals = sorted(freq.values(), reverse=True)

        memo = {}
        max_value = sum(freq_vals)
        global min_value
        min_value = max_value

        def backtrace(vals: List[int], n: int) -> int:
            global min_value

            if tuple(vals) in memo:
                return memo[tuple(vals)]

            if n > min_value:
                return max_value

            if vals[0] - vals[-1] <= k or len(vals) < 2:
                if n < min_value:
                    min_value = n

                return n

            results = []
            for i in range(len(vals)):
                current_val = vals.copy()
                current_val[i] -= 1
                if current_val[i] < 1:
                    current_val.pop(i)

                current_val.sort(reverse=True)
                result = backtrace(current_val, n + 1)
                memo[tuple(current_val)] = result
                results.append(result)

            result = min(results)
            memo[tuple(vals)] = result
            return result

        return backtrace(freq_vals, 0)


if __name__ == "__main__":
    tests = [
        ["aabcaba", 0],
        ["dabdcbdcdcd", 2],
        ["aaabaaa", 2],
        ["ahahnhahhah", 1],
        ["vvnowvov", 2],
        ["yzyyzzzyyzz", 0],
        ["vnnppvvbbn", 0],
        [
            "ykekkdhehmhhympxhgjyjsmmkxerplpeegaqwqmswpmkldlllrywjqyeqlmwyphgprsdorlllpmmwdwxsxgkwaogxgglokjykrqyhaasjjxalxwdkjexdqksayxqplwmmleevdkdqdvgelmdhkqgryrqawxeammjhpwqgvdhygyvyqahvkjrrjvgpgqxyywwdvpgelvsprqodrvewqyajwjsrmqgqmardoqjmpymmvxxqoqvhywderllksxapamejdslhwpohmeryemphplqlkddyhqgpqykdhrehxwsjvaqymykjodvodjgqahrejxlykmmaxywdgaoqvgegdggykqjwyagdohjwpdypdwlrjksqkjwrkekvxjllwkgxxmhrwmxswmyrmwldqosavkpksjxwjlldhyhhrrlrwarqkyogamxmpqyhsldhajagslmeehakrxjxpjjmjpydgkehesoygvosrhvyhrqmdhlomgmrqjrmxyvmapmspmdygkhsprqsaxsvsrkovdjprjjyworgqoakrwarjsryydpmvhvyalawsmlsdgolsxgaqhryemvkpkhqvvagmxoapmsmwkrakldlhyojqhjjghjxgksroqpoxqsorrelhqeseegpqpewxydvkvaoaldmsdpmvogaykhpxkjkwmslqjsdqowkqawxadevkswdhywrxkpvqxmgeolayqojqqwxoomyasjrqrjmoearskssppmxpgwrmsjlsrjyqrjkgwjwglxogmkqjpjkwyaqxymelsyxypqxrjvpmssoakksemjhvaxm",
            2,
        ],
    ]
    answers = [3, 2, 1, 2, 1, 1, 2, 1]

    tester = Tester(Solution().minDeletionsToMakeKSpecial2)
    tester.test(tests, answers)
