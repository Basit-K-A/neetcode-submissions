class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hasha = {}
        starts = []
        if len(nums) > 0:
            tempmax = 1
        else:
            return 0
            
        for i in range(len(nums)):
            hasha[nums[i]] = hasha.get(nums[i],i)

        for j in range(len(nums)):
            if nums[j]-1 not in hasha:
                starts.append(nums[j])

        print(starts)
        
        for k in range(len(starts)):
            p = 1
            res = 1
            
            while starts[k]+p in hasha:
                res += 1
                p += 1
                if res > tempmax:
                    tempmax = res
        
        return tempmax