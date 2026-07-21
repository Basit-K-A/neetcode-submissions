class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mStack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while mStack and temperatures[i] > temperatures[mStack[-1]]:
                poppedInd = mStack.pop()
                res[poppedInd] = i - poppedInd
            mStack.append(i)
        return res