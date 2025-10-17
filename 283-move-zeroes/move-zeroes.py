class Solution(object):
    def moveZeroes(self, n):
        p=0
        for i in range(len(n)):
            if n[i]!=0:
                n[p],n[i]=n[i],n[p]
                p+=1
        return n