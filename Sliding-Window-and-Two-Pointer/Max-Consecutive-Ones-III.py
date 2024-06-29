# https://leetcode.com/problems/max-consecutive-ones-iii/description/


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        maxi = 0
        zero = 0
        while j < n:
            if nums[j] == 0:
                zero += 1
            while zero > k:
                if nums[i] == 0:
                    zero -= 1
                i += 1

            maxi = max(maxi, j - i + 1)
            j += 1

        return maxi
  