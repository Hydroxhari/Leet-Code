class Solution(object):
    def countOperations(self, n, m):

        c=0
        while n and m:
            if n>m:
                n=n-m
            else:
                m=m-n
            c+=1
        return c