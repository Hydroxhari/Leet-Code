class Solution(object):
    def mostBooked(self, n, me):

        me.sort()
        fr=list(range(n))
        ur=[]
        rc=[0]*n

        for s,e in me:
            while ur and ur[0][0]<=s:
                _,cur = heapq.heappop(ur)
                heapq.heappush(fr,cur)
            
            dr = e-s

            if fr:
                cfr = heapq.heappop(fr)
                heapq.heappush(ur,(e,cfr))
                rc[cfr]+=1
            else:
                eet,cur = heapq.heappop(ur)
                heapq.heappush(ur,(eet+dr,cur))
                rc[cur]+=1
        
        c=max(rc)
        for i in range(n):
            if rc[i]==c:
                return i