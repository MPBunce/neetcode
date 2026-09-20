from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""

        countT = Counter(t)
        need = len(t)
        window = Counter()

        best_l, best_r = 0, -1
        best_len = float("inf")
        l = 0

        for r, c in enumerate(s):
            window[c] += 1
            if window[c] <= countT[c]:
                need -= 1

            while need == 0:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l, best_r = l, r

                lc = s[l]
                window[lc] -= 1
                if window[lc] < countT[lc]:
                    need += 1
                l += 1

        return s[best_l:best_r + 1] if best_len != float("inf") else ""