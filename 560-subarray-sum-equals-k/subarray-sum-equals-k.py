class Solution(object):
    def subarraySum(self, n, k):

        '''j=0
        s=0
        c=0
        for i in range(len(n)):
            s+=n[i]
            while s>k:
                s-=n[j]
                j+=1
            if s==k:
                c+=1
        return c''' #took 2 min failed due to neagtive ig

        d={0:1}
        s=0
        c=0
        for i in range(len(n)):
            s+=n[i]
            if s-k in d:
                c+=d[s-k]
            if s not in d:
                d[s]=0
            d[s]+=1
        return c 