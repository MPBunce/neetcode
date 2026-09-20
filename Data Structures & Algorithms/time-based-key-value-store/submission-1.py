class TimeMap:

    def __init__(self):
        # Use list instead of set to maintain order
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append to list (timestamps are strictly increasing)
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        
        # Find the most recent timestamp <= target timestamp
        result = ""
        for time, value in self.dic[key]:
            if time <= timestamp:
                result = value  # Update result with more recent valid value
            else:
                break  # Since timestamps are in order, no need to check further
        
        return result

