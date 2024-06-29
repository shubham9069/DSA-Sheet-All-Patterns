# question https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        mp = {}
        maxi = 0
        while j < n:
            if s[j] in mp and mp[s[j]] >= i:
                i = mp[s[j]] + 1

            mp[s[j]] = j
            maxi = max(maxi, j - i + 1)
            j += 1
        return maxi
