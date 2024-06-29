# question https://leetcode.com/problems/remove-k-digits/description/


class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) == k:
            return "0"

        res = []
        for i in range(0, len(num)):

            while k > 0 and res and res[-1] > num[i]:
                k -= 1
                res.pop()

            if not res and num[i] == "0":
                continue
            res.append(num[i])

        while k > 0 and res:
            k -= 1
            res.pop()
        return "0" if len(res) == 0 else "".join(res)
