class Solution(object):
    def maxEvents(self, ev):

        h=[]
        md=max(i for _, i in ev)
        ev.sort()
        c=0
        i=0

        for d in range(1,md+1):
            while i<len(ev) and ev[i][0]==d:
                heapq.heappush(h,ev[i][1])
                i+=1
            
            while h and h[0]<d:
                heapq.heappop(h)
            
            if h:
                heapq.heappop(h)
                c+=1
        return c
