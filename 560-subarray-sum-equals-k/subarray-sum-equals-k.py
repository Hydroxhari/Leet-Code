class Solution(object):
    def subarraySum(self, n, k):

        d=defaultdict(int)
        d[0]=1

        s=0
        c=0
        for i in n:
            s+=i
            if s-k in d:
                c+=d[s-k]
            d[s]+=1
        return c