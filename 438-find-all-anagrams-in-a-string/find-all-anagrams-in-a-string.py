class Solution(object):
    def findAnagrams(self, s, p):

        a=len(s)
        b=len(p)
        g=[]
        if a<b:
            return g

        c=Counter(s[:b])
        l=Counter(p)
        if c==l:
            g.append(0)

        for i in range(b,a):
            c[s[i-b]]-=1
            if c[s[i-b]]==0:
                del c[s[i-b]]
            c[s[i]]+=1

            if c==l:
                g.append(i-b+1)
        
        return g