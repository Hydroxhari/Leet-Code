class Solution(object):
    def sortArrayByParity(self, n):
        l=0
        for r in range(len(n)):
            if n[r]%2==0:
                n[l],n[r]=n[r],n[l]
                l+=1
        return n