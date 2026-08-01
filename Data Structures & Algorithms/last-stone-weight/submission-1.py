class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            y = -heapq.heappop(maxheap)
            x = -heapq.heappop(maxheap)
            if y > x:
                heapq.heappush(maxheap, -(y - x))
        return 0 if not maxheap else -heapq.heappop(maxheap)
