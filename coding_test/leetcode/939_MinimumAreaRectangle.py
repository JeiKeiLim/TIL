from tester import Tester

class Solution:
	def findRect(self, tx, ty, points):
		step = 0
		rects = []
		rect = [[tx, ty]]
		xt, yt = tx, ty

		for i in range(4):
			if i != step:
				return None

			for x, y in points:
				if x == xt and y == yt:
					continue
				if step == 0 and xt == x and yt < y:
					rect.append([x, y])
					step = 1
					xt,yt  = x, y
					break
				elif step == 1 and yt == y and xt < x:
					rect.append([x, y])
					step = 2
					xt,yt = x,y
					break
				elif step == 2 and xt == x and yt > y:
					rect.append([x,y])
					step = 3
					xt,yt = x,y
					break
				elif step == 3:
					return rect

	def minAreaRect(self, points):
		area = float('inf')
		for x, y in points:
			rect = self.findRect(x,y, points)
			if rect:
				area = min(area, (rect[2][0] - rect[0][0]) * (rect[2][1]-rect[0][1]))
				print(rect)

		if area == float('inf'):
			return 0
		else:
			return area

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
