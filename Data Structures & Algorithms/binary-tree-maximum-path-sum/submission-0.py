# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def gain(node):
            if not node:
                return 0

            # Only take positive contributions from children
            left_gain = max(gain(node.left),0)
            right_gain = max(gain(node.right),0)

            # Best path sum "through" this node (using both children)
            price_newpath = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum,price_newpath)

            # Return max gain if continuing the same path upward
            # (can only use ONE child, since a path can't branch)
            return node.val + max(left_gain,right_gain)
        gain(root)
        return self.max_sum

        