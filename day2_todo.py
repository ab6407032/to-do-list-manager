from day1_todo import Task

class TimedTask(Task):
    """Task with a time estimate."""
    def __init__(self, title, estimate_hours, description=""):
        super().__init__(title, description)
        self.estimate = estimate_hours

    def __str__(self):
        base = super().__str__()
        return f"{base} ~{self.estimate}h"

class SubTask(TimedTask):
    """A smaller piece of a bigger task."""
    def __init__(self, parent: Task, title, estimate_hours):
        super().__init__(title, estimate_hours)
        self.parent = parent

    def __str__(self):
        return f"{super().__str__()} (subtask of {self.parent._id})"

def main():
    p = Task("Build feature")
    s = SubTask(p, "Write tests", 2)
    print(p, s, sep="\n")

if __name__ == "__main__":
    main()
