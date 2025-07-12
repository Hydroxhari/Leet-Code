class Solution(object):
    def maxFreeTime(self, ev, k, st, et):

        ft=[]

        fst=0
        for i in range(len(st)):
            ft.append(st[i]-fst)
            fst=et[i]
        ft.append(ev-fst)
        print(ft)
        m=0
        s=0
        nk=k+1
        for i in range(nk):
            s+=ft[i]
        m=max(m,s)
        for i in range(nk,len(ft)):
            s=s-ft[i-nk]+ft[i]
            m=max(m,s)
        return m
        
