class Solution(object):
    def maxSum(self, n):

        d=defaultdict(list)
        l=[]
        for i in n:
            l.append(max( int(j) for j in str(i)))
        
        for i in range(len(n)):
            d[l[i]].append(n[i])
        
        m=0
        for i,j in d.items():
            if len(j)>1:
                j.sort()
                m=max(m,j[-1]+j[-2])
        
        return m if m!=0 else -1


