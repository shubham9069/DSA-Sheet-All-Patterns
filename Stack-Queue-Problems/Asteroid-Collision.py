# question :- https://leetcode.com/problems/asteroid-collision/description/


# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

# follow monostack approach 
# explaination :- https://www.youtube.com/watch?v=7isfomHzzno

def asteroidCollision(self, asteroids):
    stack = []

    for elem in asteroids:
        
        while stack and (stack[len(stack)-1]>0 and elem <0) :
            sum = stack[len(stack)-1]+elem
            if sum == 0:
                elem = 0
                stack.pop()
                break
            elif sum < 0 :
                stack.pop()
            else:
                elem = 0
                break
            if elem !=0:
                stack.append(elem)
        
    return stack