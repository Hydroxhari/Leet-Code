class Solution(object):
    def partitionLabels(self, s):
        h=defaultdict(int)
        for i in range(len(s)):
            h[s[i]]=i
        
        ce=0
        cs=0
        r=[]
        for i in range(len(s)):
            e=h[s[i]]
            if e>ce:
                ce=e
            if i==ce:
                r.append(ce-cs+1)
                cs=i+1
        return r
            
            