import numpy as np

def get_idx(arr, v, s=0, e=-1):
    s = 0
    if e < 0:
        e = len(arr)
    
    if e < 1 or arr[0] > v:
        return 0
    elif arr[-1] < v:
        return e
    
    idx = int((s+e) // 2)
    p_idx = idx

    while True:
        if arr[idx] > v:
            e = max(e-((e-s) // 2), s)
        elif arr[idx] < v:
            s = min((s+e) // 2, e)
        else:
            return idx
        
        idx = int((s+e) // 2)
        
        if p_idx == idx:
            if arr[idx] < v:
                return idx+1
            else:
                return idx
        p_idx = idx

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s_idx = 0
        l_idx = (m+n)-len(nums2)-1

        while len(nums2) > 0:
            num = nums2.pop(0)

            l_idx += 1
            
            s_idx = get_idx(nums1, num, s=s_idx, e=l_idx)

            # while s_idx < l_idx and nums1[s_idx] < num:
            #     s_idx += 1
            
            p = nums1[s_idx:]
            nums1[s_idx] = num
            nums1[(s_idx+1):] = p[:-1]
                
        return nums1


a = np.random.randint(-9223372036854775808, 9223372036854775807, size=100000)
b = np.random.randint(-9223372036854775808, 9223372036854775807, size=100000)

a.sort()
b.sort()

a_len = a.shape[0]
b_len = b.shape[0]

a = np.concatenate((a, np.zeros(b.shape[0])))

a = a.astype('int').tolist()
b = b.astype('int').tolist()

tester = Solution()

print("Testcase")
print(a)
print(a_len)
print(b)
print(b_len)

result = tester.merge(a, a_len, b, b_len)

print("Result")
# print(result)


