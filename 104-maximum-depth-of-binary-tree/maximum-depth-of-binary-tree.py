class Solution(object):
    def maxDepth(self, r):

        if not r:
            return 0
            
        d=deque([r])
        rs=0
        while d:
            l=len(d)
            for _ in range(l):
                e=d.popleft()
                if e.left:
                    d.append(e.left)
                if e.right:
                    d.append(e.right)
            rs+=1
        return rs