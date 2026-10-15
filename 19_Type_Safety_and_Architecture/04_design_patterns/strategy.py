from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data): ...

class BubbleSort(SortStrategy):
    def sort(self, data):
        arr = data[:]
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[0]
        return (
            self.sort([x for x in data[1:] if x < pivot])
            + [pivot]
            + self.sort([x for x in data[1:] if x >= pivot])
        )

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
    def sort(self, data):
        return self.strategy.sort(data)

data = [3, 1, 4, 1, 5, 9, 2, 6]
print(Sorter(BubbleSort()).sort(data))
print(Sorter(QuickSort()).sort(data))

# Function-based strategy
def sort_desc(data):
    return sorted(data, reverse=True)

def sort_by_len(data):
    return sorted(data, key=len)

strategies = {"desc": sort_desc, "len": sort_by_len}
print(strategies["desc"]([1, 3, 2]))