class Solution(object):
    def isSymmetric(self, r):
        if not r:
            return False
        
        a=deque([r.left])
        b=deque([r.right])

        while a and b:
            e1=a.popleft()
            e2=b.popleft()

            if not e1 and not e2:
                continue
            
            if not e1 or not e2 or e1.val!=e2.val:
                return False
            
            a.append(e1.left)
            a.append(e1.right)
            b.append(e2.right)
            b.append(e2.left)
        
        return not a and not b