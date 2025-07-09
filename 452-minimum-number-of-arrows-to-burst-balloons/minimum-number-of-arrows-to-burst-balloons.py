class Solution(object):
    def findMinArrowShots(self, p):
        p.sort(key = lambda x:x[1])

        c=0

        i=0
        while i<len(p):
            c+=1
            ep=p[i][1]
            j=i+1
            while j<len(p) and p[j][0]<=ep<=p[j][1]:
                j+=1
            i=j
        return c
