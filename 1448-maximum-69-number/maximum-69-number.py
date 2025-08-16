class Solution(object):
    def maximum69Number (self, n):
        s=str(n)
        nn=0
        a=1
        for i in s:
            cn=int(i)
            if a and i=='6':
                cn=9
                a-=1
            nn=nn*10+cn
        return nn
