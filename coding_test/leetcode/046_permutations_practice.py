class Solution:
	def permute(self, nums):
		
		perms = [[]]

		for n in nums:
			new_perms = []
			for perm in perms:
				for i in range(len(perm)+1):
					new_perms.append(perm[:i] + [n] + perm[i:])
			
			perms = new_perms
			
		return perms

tests = [[1,2],
		[1,2,3],
		# [1,2,3,4],
		]

tester = Solution()

for test in tests:
	print(test,'::', tester.permute(test))
