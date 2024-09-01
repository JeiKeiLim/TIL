from tester import Tester


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if length == 0:
                    continue
                else:
                    break
            length += 1
        # return len(s.strip().split(" ")[-1])
        return length


if __name__ == "__main__":
    tests = [
        ["Hello World"],
        ["   fly me   to   the moon  "],
        ["luffy is still joyboy"],
    ]
    answers = [5, 4, 6]

    tester = Tester(Solution().lengthOfLastWord)
    tester.test(tests, answers)
