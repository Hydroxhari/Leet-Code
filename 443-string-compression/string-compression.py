class Solution(object):
    def compress(self, s):
        a=0
        c=1

        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                if c==1:
                    s[a]=s[i-1]
                elif c<10:
                    s[a]=s[i-1]
                    a+=1
                    s[a]=str(c)
                else:
                    s[a]=s[i-1]
                    sc=str(c)
                    for k in sc:
                        a+=1
                        s[a]=k
                a+=1
                c=1
        if c==1:
            s[a]=s[-1]
        elif c<10:
            s[a]=s[-1]
            a+=1
            s[a]=str(c)
        else:
            s[a]=s[-1]
            sc=str(c)
            for k in sc:
                a+=1
                s[a]=k
                
        a+=1

        return a