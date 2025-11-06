class Solution(object):
    def minWindow(self, s, t):

        a,b=len(s),len(t)
        if b>a:
            return ''
        
        c=Counter(t)
        r=Counter()
        m=s*2
        j=0
        for i in range(a):
            r[s[i]]+=1
            while all(r[x]>=y for x,y in c.items()):
                if len(m)>i-j+1:
                    m=s[j:i+1]
                r[s[j]]-=1
                j+=1
        return '' if m==s*2 else m