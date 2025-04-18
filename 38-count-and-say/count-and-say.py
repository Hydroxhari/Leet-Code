class Solution(object):
    def countAndSay(self, n):
        def cas(d):
            c=1
            s=''

            for i in range(len(d)-1):
                if d[i]!=d[i+1]:
                    s+=str(c)+d[i]
                    c=0
                c+=1
            s+=str(c)+d[-1]
            return s

        c = '1'
        if n==1:
            return c
        
        for i in range(2,n+1):
            c = cas(c)
            print(c)
        
        return c
        