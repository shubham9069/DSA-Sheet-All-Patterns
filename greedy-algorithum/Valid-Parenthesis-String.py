# https://leetcode.com/problems/valid-parenthesis-string/description/

# clean code 
class Solution(object):
    def checkValidString(self, s):
        n = len(s)
        cntOpen = 0
        cntClose = 0

        for elem in s:
            if elem == "(" or elem == "*":
                cntOpen += 1
            else:
                cntOpen -= 1
            if cntOpen < 0:
                return False

        for elem in reversed(s):
            if elem == ")" or elem == "*":
                cntClose += 1
            else:
                cntClose -= 1
            if cntClose < 0:
                return False
        return True
    
    
    # merge  two loop into one
    
class Solution(object):
    def checkValidString(self, s):
        n = len(s)
        cntOpen = 0
        cntClose = 0

        for i in range(0,n):
            leftElem = s[i]
            rightElem = s[n-i-1] 
            if leftElem =="(" or leftElem == "*":
                cntOpen +=1
            else:
                cntOpen-=1

            if rightElem ==")" or rightElem == "*":
                cntClose +=1
            else:
                cntClose-=1
                
            if cntOpen<0 or cntClose<0:
                return False
        return True
            
            
         
