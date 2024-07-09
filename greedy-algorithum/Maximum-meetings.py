# https://www.naukri.com/code360/problems/maximum-meetings_1062658?leftPanelTabValue=PROBLEM

from typing import List

def sortfunc(arr):
    return arr[2]

def maximumMeetings(start: List[int], end: List[int]) -> int:
    startTime = 0
    endTime = 0
    count = 0
    arr = []
    for i in range(0, len(start)):
        arr.append([i, start[i], end[i]])

    arr.sort(key=sortfunc)
    for i in range(0, len(arr)):
        if endTime < arr[i][1]:
            startTime = arr[i][1]
            endTime = arr[i][2]
            count += 1

    return count
