# https://leetcode.com/problems/jump-game/description/
# https://www.youtube.com/watch?v=tZAa_jJ3SwQ


class Solution(object):

    def canJump(self, nums):
        maxIdx = 0

        for i in range(0, len(nums)):
            if maxIdx < i:
                return False

            maxIdx = max(maxIdx, i + nums[i])
        return True
