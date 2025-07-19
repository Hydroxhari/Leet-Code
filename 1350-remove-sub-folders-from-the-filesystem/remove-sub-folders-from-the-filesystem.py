class Solution(object):
    def removeSubfolders(self, f):
        f.sort()
        rl=[]

        ps='/_'
        for i in f:
            iu=True
            for j in range(len(i)):
                if i[j]!=ps[j]:
                    ps=i+"/"
                    break
                if j==len(ps)-1:
                    iu=False
                    break

            if iu:
                rl.append(ps[:-1])

        return rl