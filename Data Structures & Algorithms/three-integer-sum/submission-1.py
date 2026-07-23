class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        num = sorted(nums)

        for i in range(len(num)):
            if i > 0 and num[i] == num[i-1]:
                continue

            j = i + 1
            k = len(nums)-1

            while j < k:
                total = num[i] + num[j] + num[k]
                if total == 0:
                    res.append([num[i], num[j], num[k]])
                    j += 1
                    k -=1
                    while j < k and num[j] == num[j-1]:
                        j += 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
                elif total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
        return res