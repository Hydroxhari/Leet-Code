from collections import deque

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        total = 0
        n = len(status)

        have_box = set(initialBoxes)    # Boxes we physically have
        opened = set()                  # Boxes we've opened
        queue = deque()

        # Add initially open boxes to the queue
        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        while queue:
            box = queue.popleft()

            # Skip if we've already opened this box
            if box in opened:
                continue

            opened.add(box)
            total += candies[box]

            # We gain keys to open other boxes
            for key in keys[box]:
                status[key] = 1  # Mark box as open
                if key in have_box and key not in opened:
                    queue.append(key)

            # We find new boxes inside this box
            for new_box in containedBoxes[box]:
                have_box.add(new_box)
                if status[new_box] == 1 and new_box not in opened:
                    queue.append(new_box)

        return total
