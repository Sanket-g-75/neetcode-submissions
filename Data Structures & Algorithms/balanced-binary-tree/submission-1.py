# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def depth_dfs(node):
            if not node:
                return 0
            
            return 1 + max(depth_dfs(node.left),depth_dfs(node.right))

        left = depth_dfs(root.left)
        right = depth_dfs(root.right)

        if abs(left-right) > 1:
            return False
        
        
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False

        return True

        