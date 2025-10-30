class Solution(object):
    def productExceptSelf(self, n):
        s=1
        c=0
        for i in n:
            if i==0:
                c+=1
            else:
                s*=i
            
        l=[0]*len(n)
        if c>1:
            return l
        
        elif c==1:
            for i in range(len(n)):
                if n[i]==0:
                    l[i]=s
        else:
            for i in range(len(n)):
                l[i]=s//n[i]
        return l
        
