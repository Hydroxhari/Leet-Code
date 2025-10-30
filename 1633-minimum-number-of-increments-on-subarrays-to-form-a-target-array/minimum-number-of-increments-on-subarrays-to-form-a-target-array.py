class Solution(object):
    def minNumberOperations(self, t):

        p=0
        c=0
        for i in t:
            if i>p:
                c+=i-p
            p=i
        return c
        