
class Solution:
	def smallestRepunitDivByK(self, K: int) -> int:
		n = 0
		m_set = set()

		for i in range(K):
			n = (n*10 + 1) % K 

			if n == 0:
				return i+1
			elif n in m_set:
				return -1

			m_set.add(n)

		return -1


tests = [1, 23, 149, 9, 3929, 6429, 19645, 49993, 99993]
answers = [1, 22, 148, 9, 491, 2142, -1, 49992, 33330]

tester = Solution()

for answer, test in zip(answers, tests):
	predict = tester.smallestRepunitDivByK(test)

	print(test, answer, predict, answer == predict)

