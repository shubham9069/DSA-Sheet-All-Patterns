# leetcode :- https://leetcode.com/problems/next-greater-element-ii/

# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.

def nextGreaterElements(self, nums):
    stack=[]
    n  = len(nums)
    ans = [0]*n


    for i in range((2*n)-1,-1,-1):            
        while stack and stack[len(stack)-1]<=nums[i%n]:
            stack.pop()

        if i < n:    
            if len(stack) == 0:
                ans[i] = -1
            else:
                ans[i] = stack[len(stack)-1]   
                
        stack.append(nums[i%n])
        return ans