class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def remove_todo(self, todo):
        if todo in self.todos:
            self.todos.remove(todo)

    def get_todos(self):
        return self.todos
