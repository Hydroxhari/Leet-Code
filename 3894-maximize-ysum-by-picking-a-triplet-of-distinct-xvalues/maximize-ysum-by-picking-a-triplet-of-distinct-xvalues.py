class Solution(object):
    def maxSumDistinctTriplet(self, x, y):

        h={}

        for i in range(len(x)):

            if x[i] in h:

                if h[x[i]]<y[i]:
                    h[x[i]]=y[i]

                continue
            
            h[x[i]]=y[i]
        
        l=list(h.values())
        l.sort()
        print(h)
        print(l)
        return sum(l[-3:]) if len(l)>2 else -1            
        