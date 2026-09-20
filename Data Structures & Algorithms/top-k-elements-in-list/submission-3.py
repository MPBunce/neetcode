class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        output = []
        for i in range(k):
            common = count.most_common(1)
            output.append(common[0][0])
            del count[common[0][0]]
        return output