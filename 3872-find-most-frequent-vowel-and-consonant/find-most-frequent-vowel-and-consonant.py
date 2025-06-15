class Solution(object):
    def maxFreqSum(self, s):

        v=0
        c=0
        d=Counter(s)

        for i in d.keys():
            if i in {'a', 'e', 'i', 'o', 'u'}:
                v=max(v,d[i])
            else:
                c=max(c,d[i])
        
        return v+c
        