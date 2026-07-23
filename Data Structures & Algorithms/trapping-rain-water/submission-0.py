class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        res = max = 0

        for i in range(len(height)):
            if height[i] >= max:
                max = height[i]
            prefix.append(max)

        j = len(height)-1
        max = 0
        while j >= 0:
            if height[j] >= max:
                max = height[j]
            suffix.append(max)
            j-=1
        
        i = 0
        suffix.reverse()
        for i in range(len(height)):
            res += min(prefix[i], suffix[i]) - height[i]
        
        return res