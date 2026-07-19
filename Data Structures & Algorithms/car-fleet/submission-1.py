class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars by position descending (closest to target first)
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        
        stack = []
        
        for pos, spd in cars:
            time = (target - pos) / spd
            
            # If stack is empty or current car's time is greater than the time 
            # at the top of the stack, it forms a new fleet (push it)
            if not stack or time > stack[-1]:
                stack.append(time)
            # else: current car catches up to the fleet ahead (time <= stack[-1]),
            # so it merges into that fleet — we don't push anything
        
        return len(stack) 