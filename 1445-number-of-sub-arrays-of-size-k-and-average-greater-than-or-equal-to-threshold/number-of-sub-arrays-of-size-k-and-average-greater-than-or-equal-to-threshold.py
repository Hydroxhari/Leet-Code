class Solution(object):
    def numOfSubarrays(self, a, k, t):

        j=0
        c=0
        s=0
        for i in range(k):
            s+=a[i]
        if s//k>=t:
            c+=1
        for i in range(k,len(a)):
            s=s-a[i-k]+a[i]
            if s//k>=t:
                c+=1
        return c

