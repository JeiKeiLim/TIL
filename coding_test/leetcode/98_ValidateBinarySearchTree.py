# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        left_queue = []
        right_queue = []
        
        queue = [root]
        while len(queue) > 0:
            c_node = queue.pop()
            
            if c_node.left:
                queue.append(c_node.left)
                left_queue.append([c_node.left, c_node.val])
            if c_node.right:
                queue.append(c_node.right)
                right_queue.append([c_node.right, c_node.val])
                
        while len(left_queue) > 0:
            c_node = left_queue.pop()
            
            l_que = [c_node[0]]
            pv = c_node[1]
            
            while len(l_que) > 0:
                cc_node = l_que.pop()
                if cc_node.val >= pv:
                    return False
                
                if cc_node.left:
                    l_que.append(cc_node.left)
                if cc_node.right:
                    l_que.append(cc_node.right)
        
        while len(right_queue) > 0:
            c_node = right_queue.pop()
            
            l_que = [c_node[0]]
            pv = c_node[1]
            
            while len(l_que) > 0:
                cc_node = l_que.pop()
                if cc_node.val <= pv:
                    return False
                
                if cc_node.left:
                    l_que.append(cc_node.left)
                if cc_node.right:
                    l_que.append(cc_node.right)
                    
            
        return True