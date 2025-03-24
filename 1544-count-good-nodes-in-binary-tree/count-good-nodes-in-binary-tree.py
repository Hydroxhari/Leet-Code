class Solution(object):
    def goodNodes(self, r):
        
        if not r:
            return 0
        
        q=deque([(r,r.val)])
        c=0
        while q:
            n,v=q.popleft()
            if n.val>=v:
                c+=1
            
            v=max(v,n.val)
            if n.left:
                q.append((n.left,v))
            if n.right:
                q.append((n.right,v))
        return c
        
