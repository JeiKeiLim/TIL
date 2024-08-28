from tester import Tester

class Solution:
	def hIndex(self, citations) -> int:
		max_h = 0
		len_c = len(citations)
		citations = sorted(citations)
		h = 0

		for i in range(len_c):
			tmp = min(len_c-i, citations[i])
			max_h = max(max_h, tmp)

		return max_h

tests = [[[3,0,6,1,5]], [[100]]]
answers = [3, 1]

tester = Tester(Solution().hIndex)
tester.test(tests, answers)