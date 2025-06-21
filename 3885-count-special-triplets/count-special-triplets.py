class Solution(object):
    def specialTriplets(self, n):

        d=Counter(n)
        c=0
        h=defaultdict(int)
        for i in n:
            d[i]-=1
            c+=max(0,d[i*2]*h[i*2]) 
            h[i]+=1
        return c%((10**9)+7)
        

