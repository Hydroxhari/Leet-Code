class Solution(object):
    def deleteDuplicates(self, h):
        if not h:
            return h
        c=h
        while c and c.next:
            if c.val == c.next.val:
                c.next=c.next.next
            else:
                c=c.next
        return h
