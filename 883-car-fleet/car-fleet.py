class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        stack = []  # Stack to track fleet arrival times
        
        for pos, vel in cars:
            time = float(target - pos) / vel  # Time to reach the target
            
            # If the stack is empty or the current car arrives later, it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)  # Number of fleets
