class Solution(object):
    def reverseKGroup(self, h, k):

        def reverse(l):
            l=l.next
            c=l
            p=None
            while c:
                n=c.next
                c.next=p
                p=c
                c=n
            return p

        c=h
        l=0
        while c:
            l+=1
            c=c.next
        
        np = l//k
        tp=np

        storage=[]
        c=h
        while np:
            cnt=k
            l=ListNode(0)
            ch=l
            while cnt:
                ch.next=c
                ch=ch.next
                c=c.next
                cnt-=1
            ch.next=None
            storage.append(l)
            np-=1
        l=ListNode(0,c)
        storage.append(l)
        
        i=0
        while tp:
            ele=storage[i]
            ele=reverse(ele)
            storage[i]=ele
            tp-=1
            i+=1
        if len(storage)>i:
            ele=storage[i]
            storage[i]=ele.next
        
        fl=ListNode(0)
        c=fl
        while storage:
            e=storage.pop(0)
            wh=e
            while wh:
                c.next=wh
                wh=wh.next
                c=c.next
            
        return fl.next