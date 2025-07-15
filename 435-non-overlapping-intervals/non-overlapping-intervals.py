class Solution(object):
    def eraseOverlapIntervals(self, l):

        l.sort(key= lambda x:x[1])

        fs,fe=l[0][0],l[0][1]
        s=[l[0]]
        c=0

        for i,j in l[1:]:
            if fe>i:
                c+=1
            else:
                fe=j
        return c
