from tester import Tester

class Solution:
    def generateParenthesis(self, n: int):
        if n == 1:
            return ["()"]

        brackets = self.generateParenthesis(n-1)
        len_b = len(brackets)
        add_candidate = []
        for elem in brackets:
            add_candidate.append("()%s" % elem)
            add_candidate.append("%s()" % elem)
            add_candidate.append("(%s)" % elem)

        new_bracket = set(add_candidate)

        return list(new_bracket)

tester = Solution()
tests = [[2], [3], [4], [5]]
answer = [  ["(())", "()()"],
            ["((()))","(())()","()(())","(()())","()()()"],
            ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"],
            ["((((()))))","(((()())))","(((())()))","(((()))())","(((())))()","((()(())))","((()()()))","((()())())","((()()))()","((())(()))","((())()())","((())())()","((()))(())","((()))()()","(()((())))","(()(()()))","(()(())())","(()(()))()","(()()(()))","(()()()())","(()()())()","(()())(())","(()())()()","(())((()))","(())(()())","(())(())()","(())()(())","(())()()()","()(((())))","()((()()))","()((())())","()((()))()","()(()(()))","()(()()())","()(()())()","()(())(())","()(())()()","()()((()))","()()(()())","()()(())()","()()()(())","()()()()()"]
            ]

tester = Tester(Solution().generateParenthesis)
tester.test(tests, answer)
