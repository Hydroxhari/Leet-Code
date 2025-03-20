class Solution(object):
    def topKFrequent(self, n, k):

        b=[[] for i in range(len(n)+1)]

        h={}
        for i in n:
            if i not in h:
                h[i]=0
            h[i]+=1
        
        for i,j in h.items():
            b[j].append(i)
        
        c=0
        l=[]
        for i in range(len(n),0,-1):
            for j in b[i]:
                l.append(j)
                c+=1
                if c==k:
                    return l
        return -1
