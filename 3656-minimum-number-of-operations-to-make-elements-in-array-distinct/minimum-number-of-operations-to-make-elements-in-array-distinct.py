class Solution(object):
    def minimumOperations(self, n):

        c=0
        i=0
        l=len(n)
        while n:
            if len(n)==len(set(n)):
                return c
            c+=1
            i+=3
            if i>=l:
                return c
            n=n[3:]