class Solution(object):
    def isSameTree(self, p, q):

        a,b=deque([p]),deque([q])

        while a and b:
            x,y=a.popleft(),b.popleft()

            if not x and not y:
                continue
            
            if not x or not y or x.val!=y.val:
                return False
            
            a.append(x.left)
            a.append(x.right)
            b.append(y.left)
            b.append(y.right)
        return not a and not b
        