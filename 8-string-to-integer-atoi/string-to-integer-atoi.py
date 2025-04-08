class Solution(object):
    def myAtoi(self, s):

        s=s.lstrip()
        if not s:
            return 0

        n=1
        if s[0]=='-':
            n=-1
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]
        
        r=''
        for i in s:
            if i.isdigit():
                r+=i
            else:
                break
        if not r:
            return 0

        r=int(r)*n
        if r<-2**31 :
            return -2**31
        if r>2**31-1:
            return 2**31-1
        return r
        