class Solution(object):
    def minWindow(self, s, t):

        c=Counter(t)
        m=float('inf')
        fo=''

        j=0

        cc=Counter()

        for i in range(len(s)):
            cc[s[i]]+=1

            while all(c[k]<=cc[k] for k in c.keys()):
                if m>i-j+1:
                    m=i-j+1
                    fo=s[j:i+1]
                cc[s[j]]-=1
                j+=1

        return fo