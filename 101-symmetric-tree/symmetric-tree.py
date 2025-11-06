class Solution(object):
    def isSymmetric(self, r):
        
        lf=deque([r.left])
        ri=deque([r.right])

        while lf and ri:
            ln=lf.popleft()
            rn=ri.popleft()
            if (ln and not rn) or (not ln and rn):
                return False
            elif not ln and not rn:
                continue
            elif ln.val!=rn.val:
                return False
            
            lf.append(ln.left)
            lf.append(ln.right)
            ri.append(rn.right)
            ri.append(rn.left)

        return True