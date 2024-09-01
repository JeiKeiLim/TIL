import random

class Solution:

	def __init__(self, radius: float, x_center: float, y_center: float):
		self.radius = radius
		self.xc = x_center
		self.yc = y_center

	def randPoint(self) -> list:
		while True:
			rx = (random.random() - 0.5) * 2
			ry = (random.random() - 0.5) * 2
			
			if ((rx**2) + (ry**2)) <= 1:
				break

		return [rx*self.radius+self.xc, ry*self.radius+self.yc]
				
		

# Your Solution object will be instantiated and called as such:
obj = Solution(1000, 100.1, 200.3)

for i in range(1000):
	print(obj.randPoint())

