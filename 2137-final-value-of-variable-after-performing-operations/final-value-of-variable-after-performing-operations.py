class Solution(object):
    def finalValueAfterOperations(self, o):

        c=0

        for i in o:
            if '--' in i:
                c-=1
            elif '++' in i:
                c+=1
        return c