class Solution:
	def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> list:
		r_ptr = r0
		c_ptr = c0

		result = []
		r_dir = 1
		c_dir = 1

		walk_dir = 0
		walk_dist = 1

		dist = 0

		while len(result) < (R*C):
			if (r_ptr >= 0 and r_ptr < R) and (c_ptr >= 0 and c_ptr < C):
				result.append([r_ptr, c_ptr])

			dist += 1

			if walk_dir == 0:
				c_ptr += c_dir
			else:
				r_ptr += r_dir

			if dist >= walk_dist:
				walk_dir = 1 - walk_dir
				dist = 0

				if walk_dir == 0:
					r_dir *= -1
					c_dir *= -1
					walk_dist += 1

		return result


tests = [
		[1, 4 ,0 ,0],
		[5, 6, 1, 4],
		]
answers = [
	[[0,0],[0,1],[0,2],[0,3]],
	[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]],
]

tester = Solution()

for answer, test in zip(answers, tests):
	my_ans = tester.spiralMatrixIII(test[0], test[1], test[2], test[3])
	print(tests, "::", my_ans == answer, my_ans)



