class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest = k
        self.heap = [n for n in nums]
        heapq.heapify(self.heap)
        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.largest:
            heapq.heappop(self.heap)
        return self.heap[0]