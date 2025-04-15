class Solution(object):
    def areNumbersAscending(self, s):

        p=-1
        s=s.split()
        for i in s:
            if i.isdigit():
                e=int(i)
                if p>=e:
                    return False
                p=e

        return True
