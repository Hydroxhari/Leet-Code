class Solution(object):
    def isSameTree(self, p, q):

        a=deque([p])
        b=deque([q])

        while a and b:
            x=a.popleft()
            y=b.popleft()

            if not x and y or not y and x:
                return False
            elif not x and not y:
                continue
            elif x.val!=y.val:
                return False
            
            a.append(x.left)
            a.append(x.right)
            b.append(y.left)
            b.append(y.right)
        
        return not a and not b

        