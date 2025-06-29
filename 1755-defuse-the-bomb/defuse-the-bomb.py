class Solution(object):
    def decrypt(self, c, k):

        '''a=[]
        l=len(c)
        if k==0:
            return [0]*l
        for i in range(l):
            s=0
            if k<0:
                for j in range(1,-k+1):
                    s+=c[i-j]
            if k>0:
                for j in range(1,k+1):
                    s+=c[(i+j)%l]
            a.append(s)
        return a'''

        l=len(c)

        if k==0:
            return [0]*l
        
        n=c+c+c

        a=[]

        for i in range(l,l+l):
            if k<0:
                a.append(sum(n[i+k:i]))
            if k>0:
                a.append(sum(n[i+1:i+k+1]))
        return a