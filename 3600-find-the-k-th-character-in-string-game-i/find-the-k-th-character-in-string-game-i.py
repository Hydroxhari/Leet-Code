class Solution:
    def kthCharacter(self, k: int) -> str:

        s='a'
        while len(s)<k:
            n=s
            for i in s:
                n+=chr((ord(i)+1)%(ord('z')+1))
            s=n
        print(s)
        return s[k-1]

        