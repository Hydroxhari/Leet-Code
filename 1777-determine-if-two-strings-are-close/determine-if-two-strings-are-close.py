class Solution(object):
    def closeStrings(self, w1, w2):
        c1=Counter(w1)
        c2=Counter(w2)
        v1=sorted(c1.values())
        v2=sorted(c2.values())
        k1=sorted(c1.keys())
        k2=sorted(c2.keys())
        return k1==k2 and v1==v2
