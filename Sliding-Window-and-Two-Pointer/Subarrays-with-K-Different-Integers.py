# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
class Solution(object):
    def helper(self, nums, k):
        mp = {}
        cnt = 0
        i = 0

        for j in range(0, len(nums)):
            mp[nums[j]] = mp.get(nums[j], 0) + 1

            while len(mp) > k:
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1
            cnt += j - i + 1
        return cnt

    def subarraysWithKDistinct(self, nums, k):
        return self.helper(nums, k) - self.helper(nums, k - 1)
