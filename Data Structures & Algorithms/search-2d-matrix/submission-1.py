class Solution:
    def binarysearch(self,mat,target,left,right):
        if left > right:
            return None
        mid = (left + right) // 2

        if mat[mid] == target:
            return mat[mid]
        elif target > mat[mid]:
            return self.binarysearch(mat,target,mid+1,right)
        else:
            return self.binarysearch(mat,target,left,mid-1)


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            output = self.binarysearch(i,target,0,len(i)-1)
            if output == target:
                return True
        return False