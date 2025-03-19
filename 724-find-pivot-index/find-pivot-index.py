class Solution(object):
    def pivotIndex(self, n):
        l=0
        r=sum(n)-n[0]

        if l==r:
            return 0

        for i in range(1,len(n)):
            l+=n[i-1]
            r-=n[i]
            if l==r:
                return i
        return -1
            