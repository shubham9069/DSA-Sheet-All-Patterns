# https://www.naukri.com/code360/problems/find-minimum-number-of-coins_975277


def MinimumCoins(n: int) -> List[int]:
    coinArr = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    ans = []
    i = 0

    while n and i < len(coinArr):
        if coinArr[i] <= n:
            n -= coinArr[i]
            ans.append(coinArr[i])
        else:
            i += 1

    return ans
