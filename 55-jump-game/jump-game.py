class Solution(object):
    def canJump(self, n):

        s=n[0]
        for i in range(1,len(n)):
            if s<i:
                return False
            s=max(s,i+n[i])
        return True