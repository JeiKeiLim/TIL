from tester import Tester

"""
You are given a string s and an integer repeatLimit.
Construct a new string repeatLimitedString using the characters of s such that no letter appears
more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, 
string a has a letter that appears later in the alphabet than the corresponding letter in b.
If the first min(a.length, b.length) characters do not differ, then the longer string is lexicographically larger.

Example 1:
Input: s = "cczazcc", repeatLimit = 3
Output:    "zzcccac"
Explanation:
We use all of the characters from s to construct the repeatLimitedString "zzcccac".
- The letter 'a' appears at most 1 time in a row.
- The letter 'c' appears at most 3 times in a row.
- The letter 'z' appears at most 2 times in a row.
The string is the lexicographically largest repeatLimitedString possible.

Example 2:
Input: s = "aababab", repeatLimit = 2
Output:    "bbabaa"
Explanation:
We use only some of the characters from s to construct the repeatLimitedString "bbabaa".
- The letter 'a' appears at most 2 times in a row.
- The letter 'b' appears at most 2 times in a row.
The string is the lexicographically largest repeatLimitedString possible.

Constraints:
1 <= repeatLimit <= s.length <= 10^5
s consists of lowercase English letters.
"""


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        """O(nm + n log n)"""
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        total = sum(freq.values())
        prev_total = total + 1
        char_list = sorted(set(s), reverse=True)
        result = ""

        while total > 0 and prev_total != total:  # O(n)
            prev_total = total
            do_break = False
            for char in char_list:  # O(m)
                repeat = min(freq[char], repeatLimit)
                if do_break:
                    repeat = min(1, freq[char])

                if repeat < 1:
                    continue

                if (result[-repeatLimit:] + char) == (char * (repeatLimit + 1)):
                    if prev_total == total:
                        continue
                    else:
                        break

                result += char * repeat
                total -= repeat
                freq[char] -= repeat

                if do_break:
                    break
                if freq[char] > 0:
                    do_break = True

        return result


if __name__ == "__main__":
    tests = [
        ["cczazcc", 3],
        ["aababab", 2],
        ["xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1],
    ]
    answers = [
        "zzcccac",
        "bbabaa",
        "zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba",
    ]

    tester = Tester(Solution().repeatLimitedString)
    tester.test(tests, answers)
