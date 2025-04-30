class Solution(object):
    def findNumbers(self, n):

        c=0

        for i in n:
            c+=1 if len(str(i))%2==0 else 0     
        return c
        