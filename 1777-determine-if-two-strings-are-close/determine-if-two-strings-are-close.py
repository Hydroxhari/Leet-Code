class Solution(object):
    def closeStrings(self, a, b):

        n=Counter(a)
        m=Counter(b)

        return sorted(n.keys())==sorted(m.keys()) and sorted(n.values())==sorted(m.values())
        