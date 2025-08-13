class Solution(object):
    def isPowerOfThree(self, n):
        i=0
        while 3**i<n:
            i+=1
        return 3**i==n