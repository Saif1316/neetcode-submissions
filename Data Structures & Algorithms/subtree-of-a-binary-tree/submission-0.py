# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def sameTree(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if self.sameTree(node,subRoot):
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False


        