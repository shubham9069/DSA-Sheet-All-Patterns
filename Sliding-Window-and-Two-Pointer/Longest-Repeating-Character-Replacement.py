# question :-https://leetcode.com/problems/longest-repeating-character-replacement/description/

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        i = 0
        j = 0
        maxi = 0
        mp = {}
        maxFreq = 0
        Jtoggle = 1
        while j < n:

            mp[s[j]] = mp.get(s[j], 0) + 1
            maxFreq = max(maxFreq, mp[s[j]])
            change = (j - i + 1) - maxFreq
            if change <= k:
                maxi = max(maxi, j - i + 1)
            else:
                mp[s[i]] -= 1
                i += 1
            j += 1
        return maxi
