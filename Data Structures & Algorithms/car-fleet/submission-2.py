class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort each position from descending order to see who we can match with
        sorted_posis = sorted(zip(position, speed), reverse=True)
        
        # find the current slowest fleet, if time is greater, then we should create another fleet
        slowest_fleet = 0
        fleets = 0
        for sorted_posi in sorted_posis:
            time = (target - sorted_posi[0]) / sorted_posi[1]
            if time > slowest_fleet:
                fleets += 1
                slowest_fleet = time
        return fleets