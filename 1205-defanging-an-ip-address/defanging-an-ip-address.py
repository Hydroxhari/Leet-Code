class Solution(object):
    def defangIPaddr(self, a):
        b=a.replace('.','[.]')
        return b