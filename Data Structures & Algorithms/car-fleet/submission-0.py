class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = []

        # match each position with speed
        for x in range(len(position)):
            position_speed.append((position[x], speed[x]))

        #sort each position from descending order to see who we can match with
        sorted_posis = sorted(position_speed, key=lambda x: x[0], reverse=True)

        # find the speeds of each position
        times = [(target - y[0]) / y[1] for y in sorted_posis]
        
        # find the current slowest fleet, if time is greater, then we should create another fleet
        slowest_fleet = 0
        fleets = 0
        for time in times:
            if time > slowest_fleet:
                fleets += 1
                slowest_fleet = time
        return fleets