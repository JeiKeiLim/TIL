class Solution:
	def longestPalindrome(self, s: str) -> str:
		rs = ""
		for i in range(len(s)-1, -1, -1):
			rs += s[i]

		result = ""
		str_map = []
		max_l = 0
		for i in range(len(s)):
			row = []
			for j in range(len(s)):
				row.append(s[i] == rs[j])
			str_map.append(row)
		
		for i in range(len(s)):
			pen_str = ""
			for j in range(i, len(s)):
				is_match = str_map[j-i][j-i]
				if is_match:
					pen_str += s[j-i]
					print(s[j-i])
				else:
					pen_str = ""

				if len(pen_str) > max_l:
					max_l = len(pen_str)
					result = pen_str
				# print( str_map[j-i][j-i] )

			print('')
		# for row in str_map:
		# 	print(row)
		# print(str_map)
		
		return result

test = Solution()
q_list = ["babad", "cbbd", "ac"]

for q in q_list:
	print("Question :", q)
	print("Answer :", test.longestPalindrome(q))
