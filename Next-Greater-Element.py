# leetcode :-https://leetcode.com/problems/next-greater-element-i/


def nextGreaterElement(self, nums1, nums2):
    stack=[]
    answer = []
    map={}
    for elem in reversed(nums2):
        
        while stack and stack[len(stack)-1]<=elem:  
            stack.pop()
            
        if len(stack) == 0:
            map[elem] = -1
        else:
            map[elem] = stack[len(stack)-1]   
                  
        stack.append(elem)
            
    for elem in nums1:
         answer.append(map[elem])
    return answer

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
