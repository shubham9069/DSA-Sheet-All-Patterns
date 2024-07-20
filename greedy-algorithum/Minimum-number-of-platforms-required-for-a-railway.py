# https://www.naukri.com/code360/problems/minimum-number-of-platforms_799400?leftPanelTabValue=SUBMISSION

from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


def calculateMinPatforms(at, dt, n):
    maxPlatform = 0
    i = 0
    j = 0
    at.sort()
    dt.sort()
    cnt = 0

    while i < n:
        if at[i] <= dt[j]:
            cnt += 1
            i += 1
        else:
            cnt -= 1
            j += 1
        maxPlatform = max(maxPlatform, cnt)
    return maxPlatform


# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n


# Main.
T = int(input())
while T > 0:
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)
