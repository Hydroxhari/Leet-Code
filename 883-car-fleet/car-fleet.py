class Solution(object):
    def carFleet(self, target, position, speed):
        stack = []
        for pos, vel in sorted(zip(position, speed), reverse=True):
            time = float(target - pos) / vel  
            if not stack or time > stack[-1]:  
                stack.append(time)
        return len(stack)