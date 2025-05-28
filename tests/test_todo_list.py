import unittest
from src.todo_list import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_todo(self):
        self.todo_list.add_todo("Buy groceries")
        self.assertIn("Buy groceries", self.todo_list.get_todos())

    def test_remove_todo(self):
        self.todo_list.add_todo("Buy groceries")
        self.todo_list.remove_todo("Buy groceries")
        self.assertNotIn("Buy groceries", self.todo_list.get_todos())

    def test_get_todos(self):
        self.todo_list.add_todo("Buy groceries")
        self.todo_list.add_todo("Read a book")
        self.assertEqual(self.todo_list.get_todos(), ["Buy groceries", "Read a book"])

if __name__ == "__main__":
    unittest.main()
