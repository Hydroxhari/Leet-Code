class Solution(object):
    def pivotIndex(self, n):

        p=[0]*len(n)
        for i in range(len(n)-1):
            p[i+1]=p[i]+n[i]
        
        s=0
        pi=-1
        for j in range(len(n)-1,-1,-1):
            if s==p[j]:
                pi=j
            s+=n[j]
        
        return pi

        [ 0,1,8,11,17,22]
        [27,20,17,11,6,0]

        [0,2,3]
        [0,-1,0]
