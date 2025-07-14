class Solution(object):
    def matchPlayersAndTrainers(self, p, t):

        p.sort()
        t.sort()

        i=0
        j=0
        c=0

        while i<len(p) and j<len(t):
            if t[j]>=p[i]:
                c+=1
                i+=1
                j+=1
            else:
                j+=1
        
        return c