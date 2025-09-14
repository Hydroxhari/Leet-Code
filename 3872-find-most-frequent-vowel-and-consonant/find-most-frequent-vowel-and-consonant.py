class Solution(object):
    def maxFreqSum(self, s):
        c=Counter(s)
        vf,cf=0,0
        for i in c.keys():
            if i in 'aeiou':
                vf=max(vf,c[i])
            else:
                cf=max(cf,c[i])
        return vf+cf
        