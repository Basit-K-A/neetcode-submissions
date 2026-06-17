class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        best = 0
        cmp = 0
        while i < j:
            if heights[i] > heights[j]:
                cmp = heights[j]*(j-i)
                j -= 1
            else:
                cmp = heights[i]*(j-i)
                i += 1
            if cmp > best:
                best = cmp
            
        
        return best