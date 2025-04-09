class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [0] * self.capacity

    def insert(self, value: int):
        if self.size == self.capacity:
            self.resize()

        self.data[self.size] = value
        self.size += 1

    def resize(self):
        new_capacity = self.capacity * 2
        new_data = [0] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def get(self, index: int) -> int:
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")

    def __str__(self):
        return str(self.data[:self.size])
    
arr = DynamicArray()

arr.insert(11)
arr.insert(10)
arr.insert(77)
arr.insert(89)
print("Current array: ", arr)
print("Using get(), Item at index 3: ", arr.get(3))

for i in range(5, 10):
    arr.insert(i * 10)

print("After more insertions: ", arr)