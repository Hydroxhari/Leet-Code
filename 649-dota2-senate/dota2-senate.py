from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        qR = deque()
        qD = deque()
        n = len(senate)

        for i, ch in enumerate(senate):
            if ch == 'R':
                qR.append(i)
            else:
                qD.append(i)

        while qR and qD:
            r = qR.popleft()
            d = qD.popleft()
            if r < d:
                qR.append(r + n)
            else:
                qD.append(d + n)

        return "Radiant" if qR else "Dire"
