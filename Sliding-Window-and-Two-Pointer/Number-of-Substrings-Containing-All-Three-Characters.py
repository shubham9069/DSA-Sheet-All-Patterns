# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/




class Solution(object):
    def numberOfSubstrings(self, s):
        cnt = {c: 0 for c in "abc"}
        res = i = 0
        for j in range(len(s)):
            cnt[s[j]] += 1
            while all(cnt.values()):
                cnt[s[i]] -= 1
                i += 1
            res += i
        return res
