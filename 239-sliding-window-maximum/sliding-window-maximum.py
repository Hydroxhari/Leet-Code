class Solution(object):
    def maxSlidingWindow(self, n, k):

        r=[]
        h=[]
        m=float('-inf')
        for i in range(k):
            heapq.heappush(h,(-n[i],i))
            m=max(m,n[i])
        r.append(m)

        for i in range(k,len(n)):
            heapq.heappush(h,(-n[i],i))
            a,b = heapq.heappop(h)
            while b<i-k+1:
                a,b=heapq.heappop(h)
            r.append(-a)
            heapq.heappush(h,(a,b))

        return r