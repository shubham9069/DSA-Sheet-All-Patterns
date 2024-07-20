# https://leetcode.com/problems/candy/


class Solution(object):
    def candy(self, ratings):
        arr = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                arr[i] = 1 + arr[i - 1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                arr[i] = max(arr[i], 1 + arr[i + 1])
        ans = 0
        for elem in arr:
            ans += elem
        return ans
