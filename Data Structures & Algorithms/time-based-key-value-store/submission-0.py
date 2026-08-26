class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.time_map.get(key):
            self.time_map[key] = [(timestamp, value)]
        else:
            self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key)
        if not values:
            return ""
        l, r = 0, len(values) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2
            if (values[mid][0] <= timestamp):
                result = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return result
