class Solution(object):
    def twoSum(self, n, t):
        h={}
        for i in range(len(n)):
            d=t-n[i]
            if d in h:
                return [h[d]+1,i+1]
            h[n[i]]=i
        return [-1,-1]