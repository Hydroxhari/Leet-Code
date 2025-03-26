class Solution(object):
    def minOperations(self, g, x):
        l=[i for j in g for i in j]

        c=l[0]%x
        for i in l:
            if i%x!=c:
                return -1

        l.sort()
        m=l[len(l)//2]

        o = sum((abs(i-m)//x) for i in l)

        return o
        