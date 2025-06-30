class Solution(object):
    def checkInclusion(self, s1, s2):

        if len(s1)>len(s2):
            return False

        c=defaultdict(int)
        w=defaultdict(int)
        for i in range(len(s1)):
            w[s2[i]]+=1
            c[s1[i]]+=1
        if c==w:
            return True
        for i in range(len(s1),len(s2)):
            w[s2[i]]+=1
            w[s2[i-len(s1)]]-=1
            if w[s2[i-len(s1)]]==0:
                del w[s2[i-len(s1)]]

            if c==w:
                return True
        return False
            