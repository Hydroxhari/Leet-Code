class Solution(object):
    def checkAlmostEquivalent(self, a, b):

        l = [0]*26

        for i,j in zip(a,b):
            o=ord(i)-97
            t=ord(j)-97
            l[o]+=1
            l[t]-=1
        
        return max(max(l),abs(min(l)))<=3
