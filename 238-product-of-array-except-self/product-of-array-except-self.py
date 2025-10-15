class Solution(object):
    def productExceptSelf(self, n):
        
        l=[1]
        p=1
        for i in n[:-1]:
            p=p*i
            l.append(p)
        p=1
        print(l)
        for i in range(len(n)-1,-1,-1):
            l[i]*=p
            p=p*n[i]
        return l

