class Solution(object):
    def countDays(self, d, m):
        if not m:
            return d

        m.sort()
        free_days = 0
        last_end = 0

        for start, end in m:
            if start > last_end + 1:
                free_days += start - last_end - 1
            last_end = max(last_end, end)

        free_days += d - last_end
        return free_days
