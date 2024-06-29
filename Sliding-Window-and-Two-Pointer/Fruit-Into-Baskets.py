# https://leetcode.com/problems/fruit-into-baskets/description/


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        i = 0
        j = 0
        mp = {}
        maxi = 0
        while j < n:
            mp[fruits[j]] = mp.get(fruits[j], 0) + 1
            if len(mp) > 2:
                mp[fruits[i]] -= 1
                if mp[fruits[i]] == 0:
                    del mp[fruits[i]]
                i += 1
            maxi = max(maxi, j - i + 1)
            j += 1
        return maxi
