class Solution(object):
    def missingNumber(self, n):

        l=len(n)
        s=(l*(l+1))//2
        c=sum(n)
        return s-c