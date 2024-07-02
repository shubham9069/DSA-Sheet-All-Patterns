# https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution(object):
    def helper(self, s, goal):
        i = 0
        j = 0
        sum = 0
        subArray = 0
        while j < len(s):
            sum += s[j] % 2
            while i <= j and sum > goal:
                sum -= s[i] % 2
                i += 1
            subArray += j - i + 1
            j += 1
        return subArray

    def numberOfSubarrays(self, nums, k):
        return self.helper(nums, k) - self.helper(nums, k - 1)
