class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        op = defaultdict(int)
        rnums = []
        rnums1 = []
        for i in nums:
            op[i] += 1
        
        items = list(op.items())
        items.sort(key=lambda x: x[1], reverse = True)
        result = [item[0] for item in items[:k]]
        return result