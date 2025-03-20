class Solution(object):
    def topKFrequent(self, n, k):        

        c=Counter(n)
        return heapq.nlargest(k,c,key=c.get)
