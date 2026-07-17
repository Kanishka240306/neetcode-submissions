class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for current in range(len(temperatures)):
            while stack and temperatures[current]>temperatures[stack[-1]]:
                previous =stack.pop()
                result[previous]=current-previous
            stack.append(current)
        return result