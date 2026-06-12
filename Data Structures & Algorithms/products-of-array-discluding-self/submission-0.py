class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1]*len(nums)
        right = [1]*len(nums)

        products = 1
        for i in range(len(nums)):
            left[i] = products
            products *= nums[i]
        
        j = len(nums)-1
        products = 1

        while j >= 0:
            right[j] = products
            products *= nums[j]
            j -= 1

        res = [1]*len(nums)
        for k in range(len(nums)):
            res[k] = left[k]*right[k]

        return res