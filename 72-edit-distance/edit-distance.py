from collections import defaultdict

class Solution(object):
    def minDistance(self, a, b):

        d = defaultdict(int)

        def dp(i, j):
            if (i, j) in d:
                return d[(i, j)]

            # Base cases
            if i == len(a):
                return len(b) - j
            if j == len(b):
                return len(a) - i

            if a[i] == b[j]:
                d[(i, j)] = dp(i + 1, j + 1)
            else:
                ins = 1 + dp(i, j + 1)   # insert
                rep = 1 + dp(i + 1, j + 1)  # replace
                dep = 1 + dp(i + 1, j)   # delete
                d[(i, j)] = min(ins, rep, dep)
            return d[(i, j)]

        return dp(0, 0)
