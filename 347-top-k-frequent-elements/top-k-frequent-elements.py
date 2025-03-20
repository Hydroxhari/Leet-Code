class Solution(object):
    def topKFrequent(self, n, k):
        h = defaultdict(int)
        for num in n:
            h[num] += 1

        m=max(h.values())
        b=[[] for i in range(m+1)]

        for v,c in h.items():
            b[c].append(v)

        l=[]
        for i in range(len(b)-1,0,-1):
            if b[i]:
                l.extend(b[i])
                if len(l)>=k:
                    return l[:k]


        
