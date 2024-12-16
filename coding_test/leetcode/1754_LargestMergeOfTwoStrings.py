from tester import Tester

"""
You are given two strings word1 and word2. You want to construct a string merge in the following way:
While either word1 or word2 are non-empty:
1. If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
2. If word2 is non-empty, append the first character in word2 to merge and delete it from word2.

Return the lexicographically largest merge you can construct.

A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ,
a has a character strictly larger than the corresponding character in b.

Example 1:
Input: word1 = "cabaa", word2 = "bcaaa"
Output: "cbcabaaaaa"

Example 2:
Input: word1 = "abcabc", word2 = "abdcaba"
Output: "abdcabcabcaba"

Constraints:
1 <= word1.length, word2.length <= 3000
word1 and word2 consist only of lowercase English letters.
"""


class Solution:
    def largestMerge2(self, word1: str, word2: str) -> str:
        ptr1 = 0
        ptr2 = 0

        result = ""

        while ptr1 < len(word1) and ptr2 < len(word2):
            if word1[ptr1] > word2[ptr2]:
                result += word1[ptr1]
                ptr1 += 1
            elif word1[ptr1] < word2[ptr2]:
                result += word2[ptr2]
                ptr2 += 1
            else:
                if word1[ptr1:] > word2[ptr2:]:
                    result += word1[ptr1]
                    ptr1 += 1
                else:
                    result += word2[ptr2]
                    ptr2 += 1

        return result + word1[ptr1:] + word2[ptr2:]

    def largestMerge(self, word1: str, word2: str) -> str:
        ptr1 = 0
        ptr2 = 0

        result = ""

        while ptr1 < len(word1) and ptr2 < len(word2):
            tmp_ptr1 = ptr1
            tmp_ptr2 = ptr2

            if tmp_ptr1 < len(word1) and tmp_ptr2 < len(word2):
                while word1[tmp_ptr1] == word2[tmp_ptr2]:
                    tmp_ptr1 += 1
                    tmp_ptr2 += 1

                    if tmp_ptr1 >= len(word1) or tmp_ptr2 >= len(word2):
                        break

                    if word1[ptr1] > word1[tmp_ptr1] or word2[ptr2] > word2[tmp_ptr2]:
                        if word1[ptr1] > word1[tmp_ptr1]:
                            tmp_ptr1 -= 1
                        if word2[ptr2] > word2[tmp_ptr2]:
                            tmp_ptr2 -= 1
                        break

            cmp1 = "0"
            cmp2 = "0"
            if tmp_ptr1 < len(word1):
                cmp1 = word1[tmp_ptr1]
            if tmp_ptr2 < len(word2):
                cmp2 = word2[tmp_ptr2]

            if cmp1 >= cmp2:
                result += word1[ptr1 : tmp_ptr1 + 1]
                ptr1 = tmp_ptr1 + 1
            else:
                result += word2[ptr2 : tmp_ptr2 + 1]
                ptr2 = tmp_ptr2 + 1

        return result + word1[ptr1:] + word2[ptr2:]


if __name__ == "__main__":
    tests = [
        ["cabaa", "bcaaa"],
        ["abcabc", "abdcaba"],
        ["uuurruuuruuuuuuuuruuuuu", "urrrurrrrrrrruurrrurrrurrrrruu"],
        ["ssssssssssssssss", "sssksskssssssssssssesskss"],
        ["sssksskssssssssssssesskss", "ssssssssssssssss"],
        ["nnnnpnnennenpnnnnneenpnn", "nnnennnnnnpnnennnnennnnee"],
        ["nnnennnnnnpnnennnnennnnee", "nnnnpnnennenpnnnnneenpnn"],
    ]
    answers = [
        "cbcabaaaaa",
        "abdcabcabcaba",
        "uuuurruuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu",
        "sssssssssssssssssssksskssssssssssssesskss",
        "sssssssssssssssssssksskssssssssssssesskss",
        "nnnnpnnnnnennnnnnpnnennnnennnnennenpnnnnneenpnnee",
        "nnnnpnnnnnennnnnnpnnennnnennnnennenpnnnnneenpnnee",
    ]

    tester = Tester(Solution().largestMerge2)
    tester.test(tests, answers)
