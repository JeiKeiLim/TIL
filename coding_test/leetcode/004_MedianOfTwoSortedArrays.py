class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        result = 0

        l1 = len(nums1)
        l2 = len(nums2)
        
        if l1 < l2:
            l1, l2, nums1, nums2 = l2, l1, nums2, nums1
        
        if l2 == 0:
            l2, nums2 = l1, nums1
        
        c_idx1 = int(l1//2)
        c_idx2 = int(l2//2)

        for i in range(10):
            if nums1[c_idx1] < nums2[c_idx2]:
                c_idx2 = int(c_idx2 // 2)
                c_idx1 += int((l1-c_idx1) // 2)
            else:
                c_idx1 = int(c_idx1 // 2)
                c_idx2 += int((l2-c_idx2) // 2)

            left_n1 = c_idx1
            right_n1 = l1 - c_idx1 - 1

            left_n2 = c_idx2
            right_n2 = l2 - c_idx2 - 1

            ln = left_n1 + left_n2
            rn = right_n1 + right_n2
            
            print("nums1,2 =", nums1[c_idx1], nums2[c_idx2])
            print("idx1,2 =", c_idx1, c_idx2)
            print("left_n1,2 =", left_n1, left_n2, ", right_n1,2 =", right_n1, right_n2)

            balance = abs(ln-rn)
            if l1 > l2 and balance == 1:
                if left_n1 > left_n2:
                    return nums1[c_idx1]
                else:
                    return nums2[c_idx2]
            elif l1 < l2 and balance == 1:
                if right_n1 > right_n2:
                    return nums1[c_idx1]
                else:
                    return nums2[c_idx2]            
            elif balance == 0:
                return (nums1[c_idx1] + nums2[c_idx2]) / 2

test = Solution()
q_list = [  [[1,2,3,4,5,6,7], [7, 9, 10, 12]],
            [[1,3],[2]],
            [[1,2], [3,4]] 
            ]

for q in q_list:
    print("\nQustion : ", q)
    print("Answer : ", test.findMedianSortedArrays(q[0], q[1]))

