class Solution(object):
    def moveZeroes(self, n):
        l=[]
        for i in range(len(n)):
            if n[i]!=0:
                l.append(n[i])
        t=len(n)-len(l)
        l.extend([0]*t)
        n[:]=l[:]
