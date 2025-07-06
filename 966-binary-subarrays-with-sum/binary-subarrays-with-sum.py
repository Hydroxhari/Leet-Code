class Solution(object):
    def numSubarraysWithSum(self, n, g):

        d={0:1}
        s=0
        c=0
        for i in n:
            s+=i
            if s-g in d:
                c+=d[s-g]
            if s not in d:
                d[s]=0
            d[s]+=1
        print(d)
        return c # though in 2 min but didnt work so went with sliding 
    '''
        j=0
        s=0
        c=0
        for i in range(len(n)):
            s+=n[i]
            while s>g:
                s-=n[j]
                j+=1
            if s==g:
                print(i)
                c+=i-j+1
        return c'''