class Solution(object):
    def simplifyPath(self, p):

        s=[]
        l=p.split('/')
        for i in l:
            if not i or i=='.':
                continue
            if i=='..':
                if s:
                    s.pop()
            else:
                s.append(i)
        
        return '/'+'/'.join(s)