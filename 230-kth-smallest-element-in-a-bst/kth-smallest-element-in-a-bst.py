class Solution(object):
    def kthSmallest(self, r, k):
        self.c=0
        self.a=None

        def io(r):
            if not r or self.a is not None:
                return 
            
            io(r.left)

            self.c+=1
            if self.c==k:
                self.a=r.val
                return 
            
            io(r.right)
        
        io(r)
        return self.a
            