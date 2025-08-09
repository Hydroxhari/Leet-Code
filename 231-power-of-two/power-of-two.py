class Solution(object):
    def isPowerOfTwo(self, n):

        if n<=0:
            return False
        if n==1:
            return True
        if n%2!=0:
            return False
        
        while n>2:
            n//=2
            if n%2!=0:
                return False
        return True

            