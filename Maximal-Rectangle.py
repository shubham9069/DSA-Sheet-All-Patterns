# question : https://leetcode.com/problems/maximal-rectangle/


class Solution:
    
    
    def Largest_rectangle_area(self, heights):
        # It's is a subpart of this question 
        #  question https://leetcode.com/problems/largest-rectangle-in-histogram/description/ 
        max_area = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        height = [0] * (c + 1)
        ans = 0

        for row in range(0, r):
            for col in range(0, c):

                if matrix[row][col] == "1":
                    height[col] += 1
                else:
                    height[col] = 0
            ans = max(ans, self.Largest_rectangle_area(height))
        return ans
