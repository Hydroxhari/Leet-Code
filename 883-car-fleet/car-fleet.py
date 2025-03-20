class Solution(object):
    def carFleet(self, target, position, speed):
        cars_map={}
        res=0
        position_stack=[]
        for i in range(len(position)):
            cars_map[position[i]] = speed[i]
        for car_pos in sorted(cars_map, reverse=True):
            iterations=float(target-car_pos)/cars_map[car_pos]
            if position_stack and position_stack[-1]>=iterations:
                continue
            else:
                position_stack.append(iterations)
        return len(position_stack)
        '''stack = []
        for pos, vel in sorted(zip(position, speed), reverse=True):
            time = float(target - pos) / vel  
            if not stack or time > stack[-1]:  
                stack.append(time)
        return len(stack)'''