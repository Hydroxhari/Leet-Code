class Solution(object):
    def addTwoNumbers(self, l1, l2):

        l=ListNode(0)
        h=l
        c=0
        while l1 or l2 or c:
            a= l1.val if l1 else 0
            b= l2.val if l2 else 0

            t = a+b+c
            c=t//10
            h.next=ListNode(t%10)
            h=h.next

            if l1: l1=l1.next
            if l2: l2=l2.next
        
        return l.next

