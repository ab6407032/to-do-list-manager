from day1_todo import Task

class TaskList:
    def __init__(self):
        self._tasks = []

    @classmethod
    def from_titles(cls, titles):
        tl = cls()
        for t in titles:
            tl.add_task(Task(t))
        return tl

    @staticmethod
    def validate_id(tid):
        return isinstance(tid, int) and tid > 0

    @property
    def tasks(self):
        return list(self._tasks)  # return a copy

    def add_task(self, task: Task):
        self._tasks.append(task)

    def remove_task(self, tid):
        if self.validate_id(tid):
            self._tasks = [t for t in self._tasks if t._id != tid]

def main():
    tl = TaskList.from_titles(["A","B","C"])
    print([str(t) for t in tl.tasks])
    tl.remove_task(2)
    print([str(t) for t in tl.tasks])

if __name__ == "__main__":
    main()
