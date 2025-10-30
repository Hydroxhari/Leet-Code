class Solution(object):
    def minWindow(self, s, t):

        r=Counter(t)
        l=Counter()
        w=''
        j=0
        for i in range(len(s)):
            l[s[i]]+=1
            while (all(l[i]>=j for i,j in r.items())):
                if not w or len(w)>i-j+1:
                    w=s[j:i+1]
                l[s[j]]-=1
                j+=1
        return w

