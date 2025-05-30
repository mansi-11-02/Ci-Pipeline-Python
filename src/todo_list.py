import os  # Unused import

class TodoList:
    def __init__(self):
        self.todos = []
        self.password = "12345"  # Hardcoded password

    def add_todo(self, todo):
        self.todos.append(todo)

    def remove_todo(self, todo):
        if todo in self.todos:
            self.todos.remove(todo)

    def get_todos(self):
        return self.todos

    def complex_condition(self, todo):
        if todo in self.todos and len(todo) > 5 and todo.startswith("A"):
            return True
        return False

    def duplicate_code(self):
        # Duplicate code block
        self.todos.append("Sample Todo")
        self.todos.append("Sample Todo")
