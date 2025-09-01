import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        # helper function: calculate gain
        def gain(p, t):
            return (p + 1) / float(t + 1) - p / float(t)
        
        # max-heap by gain (store as negative for Python min-heap)
        h = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(h)

        # distribute extra students
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(h)
            p, t = p + 1, t + 1
            heapq.heappush(h, (-gain(p, t), p, t))

        # compute final average
        total = 0.0
        while h:
            _, p, t = heapq.heappop(h)
            total += p / float(t)
        
        return total / len(classes)
