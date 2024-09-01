from tester import Tester

class Solution:
	def minAreaRect(self, points):
		pass

tests = [[[[1,1],[1,3],[3,1],[3,3],[2,2]]], 
		 [[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]],
		 [[[0,1],[1,3],[3,3],[4,4],[1,4],[2,3],[1,0],[3,4]]]
		]
answers = [4, 2, 2]

'''
00123456789
0 # 
1#
2
3 ###
4 # ##
5
6
7
8
9
'''

tester = Tester(Solution().minAreaRect)
tester.test(tests, answers)
