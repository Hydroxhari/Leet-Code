class Solution(object):
    def getCommon(self, n1, n2):
        if n1[0] > n2[-1] or n1[-1] < n2[0]:
            return -1
        l,r=0,0
        while l<len(n1) and r<len(n2):
            if n1[l]==n2[r]:
                return n1[l]
            elif n1[l]>n2[r]:
                r+=1
            elif n1[l]<n2[r]:
                l+=1
        return -1