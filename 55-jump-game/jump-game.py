class Solution(object):
    def canJump(self, n):

        s=n[0]
        if len(n)==1:
            return True
        if s==0:
            return False

        for i in range(1,len(n)-1):
            s=max(s-1,n[i])
            if s==0:
                return False
        return s!=0