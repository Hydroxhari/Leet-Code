class Solution(object):
    def reverseDegree(self, s):

        c=0
        for i in range(len(s)): 
            c+=(i+1)*(123-ord(s[i]))
        return c       