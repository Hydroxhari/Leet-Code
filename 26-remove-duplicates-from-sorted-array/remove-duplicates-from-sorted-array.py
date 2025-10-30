class Solution:
    def removeDuplicates(self, n):
        p=0
        for i in range(1,len(n)):
            if n[i]>n[p]:
                n[p+1]=n[i]
                p+=1
        return p+1