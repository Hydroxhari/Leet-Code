class Solution(object):
    def countSymmetricIntegers(self, l, h):

        c=0

        for i in range(l,h+1):
            s=str(i)
            if len(s)%2==0:
                l=len(s)//2
                a,b=0,0
                for i in range(l):
                    a+=int(s[i])
                for j in range(l,l+l):
                    b+=int(s[j])
                if a==b:
                    c+=1
        return c