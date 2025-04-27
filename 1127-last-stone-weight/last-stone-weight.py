class Solution(object):
    def lastStoneWeight(self, s):

        h=[]
        for i in s:
            heapq.heappush(h,-i)
        
        while len(h)>1:
            a=heapq.heappop(h)
            b=heapq.heappop(h)
            c = -a + b
            heapq.heappush(h,-c)

        return 0 if len(h)==0 else -h[0] 
        