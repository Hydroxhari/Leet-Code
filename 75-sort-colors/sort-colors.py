class Solution(object):
    def sortColors(self, n):
        r,w,b=0,0,0

        for i in n:
            if i==0:
                r+=1
            elif i==1:
                w+=1
            else:
                b+=1
        
        for i in range(r):
            n[i]=0
        
        for i in range(r,r+w):
            n[i]=1
        
        for i in range(r+w,r+w+b):
            n[i]=2
        
        return n

