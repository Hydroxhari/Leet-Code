class Solution(object):
    def countSeniors(self, d):

        c=0
        for i in d:
            if i[11:13]>'60':
                c+=1
        return c
        