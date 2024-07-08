# https://www.naukri.com/code360/problems/fractional-knapsack_975286?leftPanelTabValue=SUBMISSION



def sortkey(val):
    return val[2]

def maximumValue(items, n, w):

    for arr in items:
        fraction = arr[1] / arr[0]
        arr.append(fraction)

    items.sort(key=sortkey, reverse=True)

    ans = 0

    for arr in items:
        if w >= arr[0]:
            ans += arr[1]
            w -= arr[0]
        else:
            ans += arr[2] * w
            w = 0

    return ans
