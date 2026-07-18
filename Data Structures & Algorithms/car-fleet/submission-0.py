class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        # Pair up position and speed, then sort by position descending (closest to target first)
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        
        max_time = 0.0
        fleets = 0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            
            if time > max_time:
                # This car can't catch up to the fleet ahead, forms a new fleet
                fleets += 1
                max_time = time
            # else: it merges into the fleet ahead (time <= max_time), no new fleet
        
        return fleets