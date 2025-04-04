class Solution(object):
    def doesValidArrayExist(self, d):
        a=0
        for i in d:
            a^=i
        return a==0