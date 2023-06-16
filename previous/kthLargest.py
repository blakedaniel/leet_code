import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        # constructing minheap with k nums
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


thirdLargest = KthLargest(3, [4, 5, 8, 2])
thirdLargest.add(3)
thirdLargest.add(5)
thirdLargest.add(10)
thirdLargest.add(9)
thirdLargest.add(4)
