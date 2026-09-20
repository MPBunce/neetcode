class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        
        result = ""
        for time, value in self.dic[key]:
            if time <= timestamp:
                result = value  # Update result with more recent valid value
            else:
                break  # Since timestamps are in order, no need to check further
        
        return result

