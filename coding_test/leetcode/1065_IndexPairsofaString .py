from tester import Tester

class Solution:
	def indexPairs(self, text, words):
		w_lens = [len(w) for w in words]
		w_text = [""] * len(words)
		result = []
		for idx, c in enumerate(text):
			for i in range(len(words)):
				w_text[i] += c
				if len(w_text[i]) > w_lens[i]:
					w_text[i] = w_text[i][1:]
				
				if len(w_text[i]) == w_lens[i] and words[i] == w_text[i]:
					# print("Matches! {} at {}~{}".format(words[i], idx-w_lens[i]+1, idx))
					result.append([idx-w_lens[i]+1, idx])

		result.sort()
		return result

	def indexPairs2(self, text, words):
		w_lens = [len(w) for w in words]
		w_text = [""] * len(words)
		r_dict = dict()

		for i, c in enumerate(text):
			for j in range(len(w_text)):
				w_text[j] += c

				if len(w_text[j]) > w_lens[j]:
					w_text[j] = w_text[j][1:]

				if len(w_text[j]) == w_lens[j] and words[j] == w_text[j]:
					s_idx = i-w_lens[j]+1
					if s_idx in r_dict.keys():
						r_dict[s_idx].append(i)
					else:
						r_dict[s_idx] = [i]
		result = []
		for i in range(len(text)):
			if i not in r_dict.keys():
				continue

			for v in r_dict[i]:
				result.append([i, v])

		return result

	def indexPairs3(self, text, words):
		result = []

		for i in range(len(text)):
			for w in words:
				e_idx = len(w) + i
				if e_idx <= len(text) and text[i:e_idx] == w:
					result.append([i, e_idx-1])

		result.sort()
		return result


tests = [["thestoryofleetcodeandme", ["story","fleet","leetcode"]],
		 ["ababa", ["aba","ab"]],
		 ["baabaaaaaa", ["b","a","ba","bb","aa"]],
		 ["ababbbaaab", ["bbb","ab","a","ba","aa"]]
		]

answers = [ [[3,7],[9,13],[10,17]], 
			[[0,1],[0,2],[2,3],[2,4]],
			[[0,0],[0,1],[1,1],[1,2],[2,2],[3,3],[3,4],[4,4],[4,5],[5,5],[5,6],[6,6],[6,7],[7,7],[7,8],[8,8],[8,9],[9,9]],
			[[0,0],[0,1],[1,2],[2,2],[2,3],[3,5],[5,6],[6,6],[6,7],[7,7],[7,8],[8,8],[8,9]]
		  ]


tester = Tester(Solution().indexPairs2, exact_match=True, verbose=1)
tester.test(tests, answers)
