from heapq import heappush, heappop

class Solution:
    def maxEvents(self, events):
        events.sort()  # Sort by start day
        minHeap = []
        day = 0
        i = 0
        res = 0
        n = len(events)

        while i < n or minHeap:
            if not minHeap:
                day = events[i][0]
            # Push all events starting today into heap
            while i < n and events[i][0] <= day:
                heappush(minHeap, events[i][1])
                i += 1
            # Attend the event that ends the earliest
            heappop(minHeap)
            res += 1
            day += 1
            # Remove expired events
            while minHeap and minHeap[0] < day:
                heappop(minHeap)
        return res
