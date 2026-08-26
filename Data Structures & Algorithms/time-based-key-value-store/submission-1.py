class TimeMap:

    def __init__(self):
        # we can make the dictionary a list that builds on timestamp tuples with values
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if we haven't seen the key before, we have to make a new list
        if not self.time_map.get(key):
            self.time_map[key] = [(timestamp, value)]
        else:
            # otherwise, we just append
            self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # not a key, we return ""
        values = self.time_map.get(key)
        if not values:
            return ""
        # otherwise, run binary search
        l, r = 0, len(values) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2
            # we'll keep updating the result every time we get closer to the answer
            # the nice part is that it's monotonically increasing until we get something
            if (values[mid][0] <= timestamp):
                result = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        # we'll return the most recent answer whether it's right or closest only.
        return result
