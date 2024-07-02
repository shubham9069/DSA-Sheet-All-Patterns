# https://leetcode.com/problems/binary-subarrays-with-sum/description/


class Solution(object):
    def helper(self, s, goal):
        i = 0
        j = 0
        sum = 0
        subArray = 0
        while j < len(s):
            sum += s[j]
            while i <= j and sum > goal:
                sum -= s[i]
                i += 1
            subArray += j - i + 1
            j += 1
        return subArray

    def numSubarraysWithSum(self, s, goal):
        if goal < 0:
            return 0
        return self.helper(s, goal) - self.helper(s, goal - 1)
