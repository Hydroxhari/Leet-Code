class Solution(object):
    def eraseOverlapIntervals(self, l):

        l.sort()

        c=0

        le = l[0][1]
        for i in l[1:]:
            s,e = i[0],i[1]
            if s<le:
                c+=1
                le=min(e,le)
            else:
                le=e

        return c

        