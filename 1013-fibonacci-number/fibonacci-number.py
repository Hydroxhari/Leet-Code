class Solution(object):
    def fib(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        a,b=0,1
        c=0

        for i in range(2,n+1):
            c=a+b
            a=b
            b=c

        return c

        