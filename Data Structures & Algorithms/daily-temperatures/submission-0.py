class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                temp = stack.pop()
                res[temp[0]] = index - temp[0]
            stack.append([index, val])
        return res