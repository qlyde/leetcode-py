class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # binary search on timestamps
        ret, ts = "", self.store[key]

        l, r = 0, len(ts) - 1
        while l <= r:
            m = (l + r) // 2
            if ts[m][1] <= timestamp:
                ret = ts[m][0]
                l = m + 1
            else:
                r = m - 1
            
        return ret


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)