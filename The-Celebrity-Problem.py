# question https://www.geeksforgeeks.org/problems/the-celebrity-problem/0


class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        stack = []
        
        for i in range(0,n):
            stack.append(i)
        
        while len(stack) >=2:
            i = stack.pop()
            j = stack.pop()
            
            if M[i][j]== 1:
                stack.append(j)
            else:
                stack.append(i)
        
        pot = stack[0]
        
        for i in range(0,n):
            if pot !=i:
                if M[pot][i] ==1 or M[i][pot] == 0:
                    return -1
        return pot