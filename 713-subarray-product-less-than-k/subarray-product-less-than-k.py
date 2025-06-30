class Solution(object):
    def numSubarrayProductLessThanK(self, n, k):

        c=0
        j=0
        p=1

        for i in range(len(n)):
            p*=n[i]
            while p>=k and j<=i:
                p//=n[j]
                j+=1
            c+=(i-j+1)
        return c

        