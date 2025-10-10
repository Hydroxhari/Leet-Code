class Solution(object):
    def maximumEnergy(self, e, k):
        l=[0]*len(e)
        for i in range(len(e)-1,-1,-1):
            if i+k<len(l):
                l[i]=e[i]+l[i+k]
            else:
                l[i]=e[i]
        return max(l)
        

        