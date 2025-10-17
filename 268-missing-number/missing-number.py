class Solution(object):
    def missingNumber(self, nu):
        
        n=len(nu)
        s=(n*(n+1))//2
        m=sum(nu)
        return s-m