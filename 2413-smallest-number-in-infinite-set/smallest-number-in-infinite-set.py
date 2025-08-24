import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.curr = 1                 # next smallest not popped yet
        self.heap = []                 # min-heap for added back numbers
        self.in_heap = set()           # to avoid duplicates in heap

    def popSmallest(self):
        if self.heap:  # take from heap if available
            smallest = heapq.heappop(self.heap)
            self.in_heap.remove(smallest)
            return smallest
        else:          # otherwise take the current number
            val = self.curr
            self.curr += 1
            return val

    def addBack(self, n):
        # Only add if it’s smaller than `curr` (already popped once)
        if n < self.curr and n not in self.in_heap:
            heapq.heappush(self.heap, n)
            self.in_heap.add(n)
