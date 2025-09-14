class Solution(object):
    def maxFreqSum(self, s):

        c=Counter(s)
        mv=0
        mc=0
        for i in c.keys():
            if i in {'a','e','i','o','u'}:
                mv=max(mv,c[i])
            else:
                mc=max(mc,c[i])
        return mv+mc        