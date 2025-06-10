class Solution(object):
    def maxDifference(self, s):
        o,e=0,float('inf')
        d=Counter(s)

        for i in d.values():
            if i%2==0 and i<e:
                e=i
            elif i%2!=0 and i>o:
                o=i
        
        
        return o-e