class Solution(object):
    def copyRandomList(self, h):

        r=Node(0)
        c=r
        th=h
        i=0
        di={}
        d={}

        while th:
            x=th.val
            di[th]=i
            l=Node(x)
            d[i]=l
            i+=1
            c.next=l
            c=c.next
            th=th.next
            
        th=h
        c=r.next
        i=0
        while th:
            ri = th.random
            if ri in di:
                m=di[ri]
                c.random=d[m]
            c=c.next
            th=th.next

        return r.next