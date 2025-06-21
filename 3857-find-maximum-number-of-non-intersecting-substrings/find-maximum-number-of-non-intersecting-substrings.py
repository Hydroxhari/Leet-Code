class Solution(object):
    def maxSubstrings(self, w):

        h=defaultdict(int)
        c=0

        for i in range(len(w)):
            if w[i] in h:
                if i-h[w[i]]+1>=4:
                    c+=1
                    h=defaultdict(int)
                continue
            h[w[i]]=i
        return c

