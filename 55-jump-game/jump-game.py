class Solution(object):
    def canJump(self, n):

        m=0
        for i,e in enumerate(n):
            if i>m:
                return False
            m=max(m,i+e)
            if m>=len(n)-1:
                return True
        return True