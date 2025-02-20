from tester import Tester, generate_random_string

from typing import List

"""
Given an array of strings nums containing n unique binary strings each of length n,
return a binary string of length n that does not appear in nums. If there are multiple answers,
you may return any of them.

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"] + ["110"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.


Constraints:
1. n == nums.length
2. 1 <= n <= 16
3. nums[i].length == n
4. nums[i] is either '0' or '1'.
5. All the strings of nums are unique.
"""


class Solution:
    def findDifferentBinaryString3(self, nums: List[str]) -> str:
        return "".join(["0" if nums[i][i] == "1" else "0" for i in range(len(nums))])

    def findDifferentBinaryString2(self, nums: List[str]) -> str:
        n = len(nums)
        result = []
        for i in range(n):
            result.append("0" if nums[i][i] == "1" else "0")
        return "".join(result)

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        num_set = set(nums)

        def dfs(seq: str) -> str:
            if len(seq) == n:
                if seq not in num_set:
                    return seq
                else:
                    return ""
            result = dfs(seq + "0")
            if result != "":
                return result
            return dfs(seq + "1")

        result = dfs("0")
        if result != "":
            return result

        return dfs("1")


if __name__ == "__main__":
    tests = [
        [["01", "10"]],
        [["00", "01"]],
        [["111", "011", "001"]],
        [[bin(i)[2:].zfill(20) for i in range(20)]],
    ]
    answers = ["00", "10", "000", ""]

    tester = Tester(Solution().findDifferentBinaryString3)
    tester.test(tests, answers)
