# 5‑Day Todo CLI Project

A beginner-friendly, step-by-step Python command-line todo application. Over five days, you'll learn core OOP concepts and design patterns, building each module and culminating in a single `todo.py` CLI that can add, list, complete, and remove tasks using in-memory or file-based storage.

---

## 📦 Project Structure

```bash
├── day1_todo.py   # Classes, encapsulation, due-date, counter reset
├── day2_todo.py   # Inheritance, super(), method overriding, Multilevel
├── day3_todo.py   # @property, classmethod constructor, JSON I/O
├── day4_todo.py   # ABC storage, duck-typing save/load, operator overloading
├── day5_todo.py   # Singleton Logger, Factory, Strategy, Decorator
└── todo.py        # Final CLI tying it all together
```

- **Storage**: Support both in-memory and JSON file backends.
- **Patterns**: Singleton, Factory, Strategy, Decorator, plus Python ABCs.
- **Extensible**: Easily add new commands, fields, or backends.

---

## 🎯 Daily Breakdown

### Day 1: Classes & Encapsulation

- Define a `Task` class with `__init__`, instance vs. class variables
- Add `_completed` flag and `@property due_date` (validate `YYYY-MM-DD`)
- Implement `@classmethod reset_task_count()` to reset your counter

### Day 2: Inheritance & Notifications

- Extend `Task` to `TimedTask` (add `estimate_hours`)
- Build `SubTask` (multilevel inheritance) and override `mark_completed()`
- Print a notification when a subtask completes

### Day 3: Properties & JSON

- In `TaskList`, add `@property completed_tasks` for finished tasks
- Create `@classmethod from_json(filename)` to load tasks from `tasks.json`
- Practice Python’s built-in `json` module

### Day 4: Duck‑Typing & Storage

- Define `StorageBackend` via `abc.ABC` with `save()`/`load()`
- Implement `InMemoryStorage` and `FileStorage` (read/write JSON)
- Demonstrate duck-typing with `save_tasks(tasks, backend)`
- Overload `__add__` in `MergableTaskList` to merge lists

### Day 5: Patterns & CLI

- Singleton: global `Logger`
- Factory: `StorageFactory.get_backend(name)` for `"memory"`/`"file"`
- Strategy: different sorting strategies (by ID, by title)
- Decorator: wrap `Task` to add `tags` and `priority`
- Build `todo.py` with `argparse` for commands:
  - `add <title> [--due] [--tags] [--priority]`
  - `list [--backend memory|file]`
  - `complete <id>`
  - `remove <id>`
  - `reset`

---

## 🚀 Installation & Usage

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/todo-cli-5day.git
   cd todo-cli-5day
   ```
2. **Run individual modules** to test each day’s work:
   ```bash
   python3 day1_todo.py
   python3 day2_todo.py
   # … etc.
   ```
3. **Use the CLI** (defaults to `file` backend):
   ```bash
   python3 todo.py add "Buy milk" --due 2025-08-01 --tags grocery morning --priority high
   python3 todo.py list
   python3 todo.py complete 1
   python3 todo.py remove 1
   python3 todo.py reset
   ```
4. **Memory backend** (no disk writes):
   ```bash
   python3 todo.py list --backend memory
   ```

---

## 📝 Sample JSON (`tasks.json`)

```json
[
  {
    "title": "Write report",
    "description": "Prepare the quarterly financial report",
    "completed": false,
    "due_date": "2025-07-30"
  },
  {
    "title": "Email client",
    "description": "Send project update to Acme Corp",
    "completed": true,
    "due_date": "2025-07-15"
  }
]
```

Load via:

```python
from day3_todo import TaskList
tasks = TaskList.from_json('tasks.json')
```

---

## 🤝 Contributing

Feel free to:

- Add new backends (e.g. SQLite, CSV)
- Extend CLI commands (e.g. `edit`, `search`)
- Improve tests or error handling

1. Fork the repo
2. Create a branch (`git checkout -b feature/new-backend`)
3. Commit your changes (`git commit -m 'Add SQLite backend'`)
4. Push and open a pull request

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

