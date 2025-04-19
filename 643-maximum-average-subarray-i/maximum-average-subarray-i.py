class Solution(object):
    def findMaxAverage(self, n, k):

        m=0
        w=sum(n[:k])
        m=w/float(k)
        for i in range(len(n)-k):
            w+=n[k+i]-n[i]
            m=max(m,w/float(k))
        
        return m

