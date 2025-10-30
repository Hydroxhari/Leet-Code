class Solution(object):
    def minNumberOperations(self, t):

        t=[0]+t
        c=0
        for i in range(1,len(t)):
            if t[i]>t[i-1]:
                c+=t[i]-t[i-1]
        return c