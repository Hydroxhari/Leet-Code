class Solution(object):
    def checkAlmostEquivalent(self, a, b):

        c=Counter(a)
        d=Counter(b)

        s=set(a+b)

        for i in s:
            if abs(c[i]-d[i])>3:
                return False
        return True
        