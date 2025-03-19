class Solution(object):
    def pivotIndex(self, n):

        s=sum(n)
        l=0
        r=s-n[0]

        if l==r:
            return 0
        for i in range(1,len(n)):
            l+=n[i-1]
            r-=n[i]
            print(l,r)
            if l==r:
                return i
        return -1
            