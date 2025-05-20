class Solution(object):
    def capitalizeTitle(self, title):
        final=[]
        word=title.split()
        for i in word:
            if len(i) <= 2:
                final.append(i.lower())
                pass
            else:
                u=i.lower()
                f=u.capitalize()
                final.append(f)
        return ' '.join(final)