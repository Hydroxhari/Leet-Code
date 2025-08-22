class Solution(object):
    def findCircleNum(self, g):

        d=defaultdict(list)
        for i in range(len(g)):
            for j in range(len(g)):
                if g[i][j]==1:
                    d[i].append(j)
        
        v=set()
        tc=0

        for i in range(len(g)):
            if i in v:
                continue
            q=deque([i])
            c=-1
            while q:
                e=q.popleft()
                if e in v:
                    continue
                v.add(e)
                c+=1
                for j in d[e]:
                    q.append(j)
            tc+=c

        return len(g)-tc

                 
