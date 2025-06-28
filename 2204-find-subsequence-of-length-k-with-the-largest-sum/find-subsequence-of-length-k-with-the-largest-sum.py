class Solution(object):
    def maxSubsequence(self, n, k):

        h=[]
        for i in range(len(n)):
            heapq.heappush(h,(-n[i],i))
        
        l=heapq.nsmallest(k,h)
        l.sort(key=lambda x:x[1])
        r=[]
        for i,j in l:
            r.append(-i)
        return r



