class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1 = {}
        for k in range(len(s1)):
            count1[s1[k]] = 1 + count1.get(s1[k],0)

        count = {}
        i = 0
        j = 0

        while j < len(s1):
            count[s2[j]] = 1 + count.get(s2[j],0)
            j += 1
        
        while j < len(s2):
            print(count1,count)
            if count1 == count:
                return True
            
            l = s2[i]
            count[l] -= 1
            if count[l] == 0:
                del count[l]
            i += 1
            
            right_char = s2[j]
            count[right_char] = 1 + count.get(right_char, 0)
            j += 1

        if count1 == count:
            return True
            
        return False