class Solution(object):
    def findDuplicates(self, n):
        
        from collections import defaultdict

        d=defaultdict(int)
        for i in n:
            d[i]+=1
        
        l=[]
        
        for i,j in d.items():
            if j==2:
                l.append(i)
        return l