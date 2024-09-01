from tester import Tester

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        answer = 0
            
        sum_vt = sum(nums)
        for ws in range(len(nums), 1, -1):
            sum_vt = sum_vt-nums[ws] if ws < len(nums) else sum_vt
            # print("{}:{} :: {}".format(len(nums), ws, sum_vt))
            
            target_v = ws/2
            sum_v = sum_vt
            
            if sum_v == target_v:
                answer = ws
                break
            
            for i in range(ws, len(nums)):
                sum_v = sum_v-nums[i-ws]+nums[i]
                
                if sum_v == target_v:
                    answer = ws
                    break
                    
            if answer != 0:
                break
        
        return answer

		
tests = [[0,1,1,1,0,0], [[0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0]],
]

answers = [[6], [74]
]


tester = Tester(Solution().findMaxLength, verbose=0)
tester.test(tests, answers)

