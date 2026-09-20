class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            #print(i, v)
            while stack and stack[-1][1] < v:
                value = stack.pop()
                #print(value)
                res[value[0]] = i - value[0]
            stack.append([i, v])

        return res