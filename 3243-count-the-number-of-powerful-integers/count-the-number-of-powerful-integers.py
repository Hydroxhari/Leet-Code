class Solution:
    def pw(self, a, b):
        ans = 1
        while b:
            ans *= a
            b -= 1
        return ans

    def get(self, n, l, s):
        N = str(n)
        ans = 0

        if len(N) < len(s):
            return 0
        elif len(N) > len(s):
            ok = True
            for i in range(len(N) - len(s)):
                ok &= (int(N[i]) - 0) <= l
                cur = min(l + 1, int(N[i]) - 0)

                if i == (len(N) - len(s) - 1):
                    cur += ok and (N[len(N) - len(s):] >= s)

                for j in range(i + 1, len(N) - len(s)):
                    cur *= l + 1

                ans += cur

                if int(N[i]) > l:
                    break
        else:
            ans += int(N >= s)

        return ans

    def numberOfPowerfulInt(self, start, finish, limit, s):
        return self.get(finish, limit, s) - self.get(start - 1, limit, s)