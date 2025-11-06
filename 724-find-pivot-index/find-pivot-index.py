class Solution(object):
    def pivotIndex(self, n):

        r=sum(n)
        l=0
        
        for i in range(len(n)):
            r-=n[i]
            if l==r:
                return i
            l+=n[i]
            
        return -1


