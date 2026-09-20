class Solution:
    def minWindow(self, s: str, t: str) -> str:
        heap = []
        heapq.heapify(heap)
        l, r = 0, len(s)
        
        m = Counter(t)

        while l < r: 
            #start at each position 
            if s[l] in t:
                l2 = l
                while l2 < r:
                    sliced = s[l:l2+1] 
                    c = m.copy()
                    print(sliced)
                    for n in sliced:
                        #print(c)
                        if n in c:
                            c[n] -= 1
                            if c[n] == 0:
                                del c[n]
                    #print(c)
                    if not c:
                        print("c in None")
                        print((len(sliced), sliced))
                        heapq.heappush(heap, (len(sliced), sliced))

                    l2+=1


            l += 1

        return heap[0][1] if heap else "" 