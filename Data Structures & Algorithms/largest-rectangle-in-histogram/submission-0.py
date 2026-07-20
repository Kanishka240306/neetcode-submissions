class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices, heights[stack] is increasing
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index  # extend the width leftward
            stack.append((start, h))
        # process remaining bars in stack (right boundary = end of array)
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
        return max_area