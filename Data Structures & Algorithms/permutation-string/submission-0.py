class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s2)
        lenS1 = len(s1)
        print("lenS1: " , lenS1)
        sortedS1 = sorted(s1)

        while l < r:
            print(s2)
            if s2[l] in sortedS1:
                print("var in this" + s2[l])
                sliced = s2[l:l+lenS1]
                print(sliced)
                if sorted(sliced) == sortedS1:
                    return True

            l += 1

        return False