class Solution(object):
    def countSubarrays(self, n):

        l=len(n)-2
        c=0

        for i in range(l):
            if n[i]+n[i+2] == n[i+1]/2.0:
                c+=1
        
        return c
