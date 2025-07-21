from day4_todo import MergableTaskList, InMemoryStorage

# Singleton Logger
class Logger:
    _inst = None
    def __new__(cls):
        if not cls._inst:
            cls._inst = super().__new__(cls)
        return cls._inst
    def log(self, msg): print("[LOG]", msg)

# Factory for storage
class StorageFactory:
    @staticmethod
    def get_backend(name):
        if name=="memory": return InMemoryStorage()
        # elif name=="file": return FileStorage()
        raise ValueError(name)

# Strategy for sorting
class SortStrategy:
    def sort(self, tasks): pass

class ByID(SortStrategy):
    def sort(self, tasks): return sorted(tasks, key=lambda t: t._id)

class ByTitle(SortStrategy):
    def sort(self, tasks): return sorted(tasks, key=lambda t: t.title)

def main():
    tl = MergableTaskList.from_titles(["d","a","c"])
    logger = Logger()
    logger.log("Before sort: " + str([t.title for t in tl.tasks]))

    strat = ByTitle()
    sorted_tasks = strat.sort(tl.tasks)
    logger.log("After sort: " + str([t.title for t in sorted_tasks]))

    backend = StorageFactory.get_backend("memory")
    backend.save(sorted_tasks)
    logger.log("Saved to memory")

if __name__ == "__main__":
    main()
