class Solution(object):
    def removeStars(self, s):

        l=[]
        for i in s:
            if i=='*':
                l.pop()
                continue
            l.append(i)
        return ''.join(l)
        