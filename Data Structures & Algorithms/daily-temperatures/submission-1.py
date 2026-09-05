class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force approach
        n = len(temperatures)
        result = [0] * n

        left = 0
        while left < n:
            right = left + 1
            while right < n:
                if temperatures[right] > temperatures[left]:
                    result[left] = right - left
                    break
                right += 1
            left += 1

        return result

        # stack based approach
        # result = [0]*len(temperatures)
        # stack = []
        # for i,t in enumerate(temperatures):
        #     while stack and t > stack[-1][0]:
        #         stackT, stackInd = stack.pop()
        #         result[stackInd] = i - stackInd
        #     stack.append((t,i))
        # return result 
            
        