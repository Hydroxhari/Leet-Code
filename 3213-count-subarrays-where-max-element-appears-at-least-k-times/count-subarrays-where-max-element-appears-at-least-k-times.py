class Solution(object):
    def countSubarrays(self, n, k):

        e=max(n)

        c=0
        j=0
        ec=0

        for i in range(len(n)):
            if n[i]==e:
                ec+=1

            while ec>=k:
                c+=len(n)-i
                if n[j]==e:
                    ec-=1
                j+=1

        return c    