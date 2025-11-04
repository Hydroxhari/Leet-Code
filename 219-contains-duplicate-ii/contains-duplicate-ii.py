class Solution(object):
    def containsNearbyDuplicate(self, n, k):
        k=min(k+1,len(n))
        d=defaultdict(int)
        for i in range(k):
            if d[n[i]]:
                return True
            d[n[i]]+=1
        
        for i in range(k,len(n)):
            d[n[i-k]]-=1
            if d[n[i-k]]==0:
                del d[n[i-k]]
            
            if d[n[i]]:
                return True
            d[n[i]]+=1
        return False
