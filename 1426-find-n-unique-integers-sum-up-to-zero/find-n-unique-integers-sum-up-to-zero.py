class Solution(object):
    def sumZero(self, n):
        l=[]

        if n%2==0:
            for i in range(1,n//2+1):
                l.append(i)
                l.append(-i)
        else:
            for i in range(1,n//2+1):
                l.append(i)
                l.append(-i)
            l.append(0)
        
        return l