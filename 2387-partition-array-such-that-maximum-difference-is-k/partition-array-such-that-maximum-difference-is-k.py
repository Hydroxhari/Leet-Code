class Solution(object):
    def partitionArray(self, n, k):

        n.sort()
        c=0
        m=n[0]
        for i in n:
            if i-m>k:
                c+=1
                m=i
        c+=1
        return c

        