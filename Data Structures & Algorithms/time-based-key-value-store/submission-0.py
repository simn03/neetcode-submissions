import bisect

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.data[key], (timestamp, value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        
        arr = self.data[key]

        if not arr:
            return ''

        l = 0
        r = len(arr) - 1

        prev_timestamp = None

        while l < r:
            m = (l + r) // 2

            if timestamp < arr[m][0]:
                r = m
            else:
                prev_timestamp = m
                l = m + 1

        if arr[l][0] <= timestamp:
            return arr[l][1]
        elif prev_timestamp != None:
            return arr[prev_timestamp][1]
        else: 
            return ''
