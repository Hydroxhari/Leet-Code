class Solution(object):
    def compress(self, s):

        pc=s[0]
        c=1
        ans=''
        for i in s[1:]:
            if pc==i:
                c+=1
            else:
                ans+=pc
                if c>1:
                    ans+=str(c)
                pc=i
                c=1
        ans+=pc
        if c>1:
            ans+=str(c)

        for i in range(len(ans)):
            s[i]=ans[i]
        return len(ans)

            