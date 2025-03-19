class Solution(object):
    def middleNode(self, h):
        f,s=h,h
        while f and f.next:
            s=s.next
            f=f.next.next
        return s