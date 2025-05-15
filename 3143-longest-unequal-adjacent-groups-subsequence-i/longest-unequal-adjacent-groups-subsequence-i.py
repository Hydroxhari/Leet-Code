class Solution(object):
    def getLongestSubsequence(self, w, g):

        l=[]
        l.append(w[0])

        j=0

        for i in range(1,len(w)):
            if g[j]!=g[i]:
                l.append(w[i])
                j=i
        
        return l
