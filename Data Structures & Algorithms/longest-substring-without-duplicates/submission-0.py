class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxT = 0
        l = 0
        temp = set()

        for r in range(len(s)):
            while s[r] in temp:
                temp.remove(s[l])
                l += 1
            temp.add(s[r])
            maxT = max(maxT, r - l + 1)

        return maxT