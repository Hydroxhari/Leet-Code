class Solution(object):
    def findSubstring(self, s, w):

        def dp(t,wo):
            if c!=t:
                return False
            cw=defaultdict(int)
            for i in range(0,len(wo),k):
                cw[wo[i:i+k]]+=1
            
            return cw==d

        d=Counter(w)
        k=len(w[0])
        w=''.join(w)
        c=Counter(w)
        t=Counter()
        ans=[]
        j=0



        for i in range(len(s)):
            t[s[i]]+=1
            if i-j+1==len(w):
                if dp(t,s[j:i+1]):
                    ans.append(j)
                t[s[j]]-=1
                if t[s[j]]==0:
                    del t[s[j]]
                j+=1
        return ans

