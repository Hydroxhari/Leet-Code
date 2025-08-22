class Solution(object):
    def canVisitAllRooms(self, r):

        v=set()
        d=deque([0])

        while d:
            e=d.popleft()
            if e in v:
                continue
            v.add(e)
            for i in r[e]:
                d.append(i)
        
        return len(v)==len(r)