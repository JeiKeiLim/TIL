from tester import Tester, generate_random_string

from typing import List

"""
Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array `bank` representing the floor plan of the bank, 
which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. 
'0' means the cell is empty, while '1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:
• The two devices are located on two different rows: r1 and r2, where r1 < r2.
• For each row i where r1 < i < r2, there are no security devices in the ith row.

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

Example 1:
Input: bank = ["011001","000000","010100","001000"]
Output: 8

Explanation:
bank[0] has 3 devices at columns 1, 2, and 5
bank[2] has 2 devices at columns 1 and 3
bank[3] has 1 device at column 2

Valid beams:
- 3 devices in row 0 * 2 devices in row 2 = 6
- 2 devices in row 2 * 1 device in row 3 = 2
Total = 8

Example 2:
Input: bank = ["000","111","000"]
Output: 0

Constraints:
• m == bank.length
• n == bank[i].length
• 1 <= m, n <= 500
• bank[i][j] is either '0' or '1'.

"011001"
"000000"
"010100"
"001000"


"""


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)

        # n_devices = [sum(map(lambda x: x == "1", list(b))) for b in bank]
        n_devices = [b.count("1") for b in bank]
        answer = 0
        prev_device = n_devices[0]
        for i in range(1, m):
            if n_devices[i] == 0:
                continue
            answer += prev_device * n_devices[i]
            prev_device = n_devices[i]
        return answer


if __name__ == "__main__":
    tests = [
        [["011001", "000000", "010100", "001000"]],
        [["000", "111", "000"]],
        [
            [
                generate_random_string(500, start_char="0", end_char="1")
                for _ in range(500)
            ]
        ],
    ]
    answers = [8, 0, -1]

    tester = Tester(Solution().numberOfBeams)
    tester.test(tests, answers)
