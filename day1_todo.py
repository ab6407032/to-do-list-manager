class Task:
    """Represents a single to-do task."""
    task_count = 0                 # class variable

    def __init__(self, title, description=""):
        Task.task_count += 1
        self._id = Task.task_count  # “private” by convention
        self.title = title          # instance vars
        self.description = description
        self._completed = False

    # getter
    def is_completed(self):
        return self._completed

    # setter
    def mark_completed(self):
        self._completed = True

    def __str__(self):
        status = "Ok" if self._completed else "No"
        return f"[{status}] ({self._id}) {self.title}"

def main():
    t1 = Task("Write report")
    print(t1)
    t1.mark_completed()
    print(t1)

if __name__ == "__main__":
    main()
