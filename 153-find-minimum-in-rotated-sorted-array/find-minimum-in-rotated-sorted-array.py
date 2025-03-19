class Solution(object):
    def findMin(self, n):
        l,r=0,len(n)-1
        while l<r:
            m=(r+l)//2
            if n[m]>n[r]:
                l=m+1
            else:
                r=m
        return n[l]
        