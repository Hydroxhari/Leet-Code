class Solution(object):
    def merge(self, l):
        l.sort()

        fs,fe=l[0][0],l[0][1]
        s=[l[0]]
        for i,j in l[1:]:
            if i<=fe<=j:
                fe=max(fe,j)
                s[-1][1]=fe
            elif i>fe:
                s.append([i,j])
                fs,fe=i,j

        return s


