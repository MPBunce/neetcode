class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            # Update existing key
            index = self.keys.index(key)
            self.values[index] = value
        else:
            # Add new key-value pair
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        return -1  # Key not found

    def remove(self, key: int) -> None:
        if key in self.keys:
            index = self.keys.index(key)
            self.keys.pop(index)
            self.values.pop(index)