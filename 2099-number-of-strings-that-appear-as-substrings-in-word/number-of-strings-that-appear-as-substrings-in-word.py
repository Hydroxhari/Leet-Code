class Solution(object):
    def numOfStrings(self, p, w):
        c=0
        for i in p:
            if i in w:
                c+=1
        return c