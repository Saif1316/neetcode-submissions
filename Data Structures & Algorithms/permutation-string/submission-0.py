class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = {}
        for i in s1:
            count_s1[i] = 1 + count_s1.get(i,0)
        need = len(count_s1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j],0)
                if count_s1.get(s2[j],0) < count2[s2[j]]:
                    break
                if count_s1.get(s2[j], 0) == count2[s2[j]]:
                    cur +=1
                if cur == need:
                    return True
        return False
        
        



        