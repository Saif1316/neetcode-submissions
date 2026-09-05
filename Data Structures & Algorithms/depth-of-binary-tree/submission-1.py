# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Approach 1: Using Recursion
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

        # Approach 2: Using Iterative BFS
        if not root:
            return 0
        q = deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

        # Approach 3: Iterative DFS with pre-order traversal
        # if not root:
        #     return 0
        # stack = []
        # stack.append(root)
        # level = 0
        # while stack:
        #     for i in range(len(stack)):
        #         node = stack.pop()
        #         if node.right:
        #             stack.append(node.right)
        #         if node.left:
        #             stack.append(node.left)
        #     level += 1
        # return level


        