# Time Complexity : O(n)
class Solution(object):
    def isIsomorphic(self, s, t):

        h={}
        d={}
        for i,j in zip(s,t):
            if i in h and h[i]!=j:
                return False
            if j in d and d[j]!=i:
                return False
            h[i]=j
            d[j]=i

        return True