class Solution(object):
    def moveZeroes(self, n):

        l=0
        for i in range(len(n)):
            if n[i]!=0:
                n[l],n[i]=n[i],n[l]
                l+=1
        