import heapq

class Solution(object):
    def totalCost(self, l, n, k):
        # nl: list of (cost, index)
        nl = [(j, i) for i, j in enumerate(l)]

        # initial candidate heaps (first k from left, last k from right)
        lh = nl[:k]
        rh = nl[-k:]
        heapq.heapify(lh)
        heapq.heapify(rh)

        v = set()                       # hired indices
        i = k                           # next candidate index from left side
        j = len(l) - k - 1              # next candidate index from right side
        c = 0

        while n > 0:
            # remove already-hired tops
            while lh and lh[0][1] in v:
                heapq.heappop(lh)
            while rh and rh[0][1] in v:
                heapq.heappop(rh)

            # peek current best candidates (inf if empty)
            ml = lh[0] if lh else (float('inf'), -1)
            mr = rh[0] if rh else (float('inf'), -1)

            # choose left on tie (<=) just like usual tie-break
            if ml[0] <= mr[0]:
                cost, idx = heapq.heappop(lh)
                c += cost
                v.add(idx)
                # refill left heap from i if there are unused indices between i and j
                if i <= j:
                    heapq.heappush(lh, nl[i])
                    i += 1
            else:
                cost, idx = heapq.heappop(rh)
                c += cost
                v.add(idx)
                # refill right heap from j if there are unused indices between i and j
                if i <= j:
                    heapq.heappush(rh, nl[j])
                    j -= 1

            n -= 1

        return c
