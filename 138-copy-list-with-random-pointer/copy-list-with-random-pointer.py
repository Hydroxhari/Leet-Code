class Solution(object):
    def copyRandomList(self, head):
        hMap = {None : None}
        cur = head
        while cur:
            copy = ListNode(cur.val)
            hMap[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = hMap[cur]
            copy.next = hMap[cur.next]
            copy.random = hMap[cur.random]
            cur = cur.next
        return hMap[head] 
        