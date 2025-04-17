class Solution(object):
    def countPairs(self, n, k):

        h=defaultdict(list)
        c=0

        for i in range(len(n)):
            e=n[i]
            if e in h:
                for j in h[e]:
                    if (i*j)%k==0:
                        c+=1
            h[e].append(i)
        
        return c

            

        