class Solution(object):
    def sortArrayByParity(self, n):
        e = [i for i in n if i % 2 == 0]
        o = [i for i in n if i % 2 != 0]
        return e+o