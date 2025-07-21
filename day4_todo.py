from abc import ABC, abstractmethod
from day3_todo import TaskList, Task

class StorageBackend(ABC):
    @abstractmethod
    def save(self, tasks): pass

    @abstractmethod
    def load(self): pass

class InMemoryStorage(StorageBackend):
    def __init__(self):
        self.data = []

    def save(self, tasks):
        self.data = tasks

    def load(self):
        return self.data

# Operator overloading: merge two lists
class MergableTaskList(TaskList):
    def __add__(self, other):
        mt = MergableTaskList()
        mt._tasks = self.tasks + other.tasks
        return mt

def main():
    a = MergableTaskList.from_titles(["X"])
    b = MergableTaskList.from_titles(["Y","Z"])
    c = a + b
    print([t._id for t in c.tasks])
    # storage demo
    store = InMemoryStorage()
    store.save(c.tasks)
    print("Loaded:", [t._id for t in store.load()])

if __name__ == "__main__":
    main()
