# question link- https://leetcode.com/problems/trapping-rain-water/description/

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


def trap(self, height):
    leftmost = 0
    rightmost = 0
    l = 0
    r = len(height) - 1
    res = 0

    while l < r:
        if height[l] <= height[r]:
            if height[l] >= leftmost:
                leftmost = height[l]
            else:
                res += leftmost - height[l]
            l += 1
        else:
            if height[r] >= rightmost:
                rightmost = height[r]
            else:
                res += rightmost - height[r]
            r -= 1
    return res
