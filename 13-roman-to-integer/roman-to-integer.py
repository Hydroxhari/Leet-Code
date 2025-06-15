class Solution:
    def romanToInt(self, s: str) -> int:

        d = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        t=0
        p=0

        for i in s:
            if d[i]>p:
                t+=d[i]-p-p
            else:
                t+=d[i]
            p=d[i]
                
        return t



        