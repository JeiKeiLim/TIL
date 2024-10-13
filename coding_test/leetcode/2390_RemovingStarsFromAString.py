from tester import Tester

"""
2390. Removing Stars From a String
Medium

You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
"""


class Solution:
    def removeStars(self, s: str) -> str:
        """ 
        Started @ 14:32
        Ended @ 14:36
        O(n)
        """
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


if __name__ == "__main__":
    tests = [
        ["leet**cod*e"],
        ["erase*****"],
    ]
    answers = ["lecoe", ""]

    tester = Tester(Solution().removeStars)
    tester.test(tests, answers)
