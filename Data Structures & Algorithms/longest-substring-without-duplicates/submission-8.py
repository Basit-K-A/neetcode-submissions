class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        l = best = 0
        for r in range(len(s)):

            counts[s[r]] += 1
            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1

            best = max(best, r-l+1)
        return best