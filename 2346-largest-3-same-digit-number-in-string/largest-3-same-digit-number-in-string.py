class Solution(object):
    def largestGoodInteger(self, n):

        for i in range(9,-1,-1):
            if str(i)*3 in n:
                return str(i)*3
        return ''