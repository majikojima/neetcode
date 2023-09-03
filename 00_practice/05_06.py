class TimeMap:

    def __init__(self):

    def set(self, key: str, value: str, timestamp: int) -> None:

    def get(self, key: str, timestamp: int) -> str:

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))
print(obj.get("foo", 3))
obj.set("foo", "bar2", 1)
print(obj.get("foo", 4))
print(obj.get("foo", 5))