class Solution(object):
    def isZeroArray(self, n, q):
        
        l = [0]*(len(n)+1)

        for i,j in q:
            l[i]+=1
            l[j+1]-=1
        
        c=0
        for i in range(len(n)):
            c+=l[i]
            n[i]-=c
            if n[i]>0:
                return False
        
        return True
