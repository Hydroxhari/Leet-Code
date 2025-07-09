class Solution(object):
    def productExceptSelf(self, n):

        pa=[1]*len(n)
        s=1
        for i in range(len(n)):
            pa[i]=s
            s*=n[i]
        
        s=1
        for i in range(len(n)-1,-1,-1):
            pa[i]*=s
            s*=n[i]
        return pa