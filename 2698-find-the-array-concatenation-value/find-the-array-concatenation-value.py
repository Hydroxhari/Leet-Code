class Solution(object):
    def findTheArrayConcVal(self, n):
        l=0
        r=len(n)-1

        c=0

        if len(n)%2!=0:
            c=n[len(n)//2]
        
        print(c)

        while l<r:
            s=str(n[l])+str(n[r])
            c+=int(s)
            l+=1
            r-=1
        
        return c


