class Solution(object):
    def maximumDifference(self, n):
        m = -1
        a = n[0]  # start with first element

        for i in range(1, len(n)):
            if n[i] > a:
                m = max(m, n[i] - a)
            else:
                a = n[i]  # update min if current is smaller

        return m
