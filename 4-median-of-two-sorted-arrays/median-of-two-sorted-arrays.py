class Solution(object):
    def findMedianSortedArrays(self, n, m):
        a=0
        l=n+m
        l.sort()
        o=len(l)
        if o%2==0:
            return (l[o/2-1]+l[o/2])/2.0
        return l[o//2]
        