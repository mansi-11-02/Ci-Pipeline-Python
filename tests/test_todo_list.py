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

    def test_add_multiple_todos(self):
        self.todo_list.add_todo("Buy groceries")
        self.todo_list.add_todo("Read a book")
        self.todo_list.add_todo("Exercise")
        self.assertEqual(self.todo_list.get_todos(), ["Buy groceries", "Read a book", "Exercise"])

    def test_remove_nonexistent_todo_fail(self):
        with self.assertRaises(ValueError):
            self.todo_list.remove_todo("Nonexistent todo")

    def test_remove_todo_fail(self):
        self.todo_list.add_todo("Buy groceries")
        self.todo_list.remove_todo("Read a book")
        self.assertIn("Buy groceries", self.todo_list.get_todos())

    def test_clear_todos(self):
        self.todo_list.add_todo("Buy groceries")
        self.todo_list.add_todo("Read a book")
        self.todo_list.clear_todos()
        self.assertEqual(self.todo_list.get_todos(), [])

    def test_todo_count(self):
        self.todo_list.add_todo("Buy groceries")
        self.todo_list.add_todo("Read a book")
        self.assertEqual(self.todo_list.todo_count(), 2)

    def test_todo_count_fail(self):
        self.todo_list.add_todo("Buy groceries")
        self.todo_list.add_todo("Read a book")
        self.assertEqual(self.todo_list.todo_count(), 3)

    def test_get_todo_by_index(self):
        self.todo_list.add_todo("Buy groceries")
        self.todo_list.add_todo("Read a book")
        self.assertEqual(self.todo_list.get_todo_by_index(1), "Read a book")

    def test_get_todo_by_index_fail(self):
        self.todo_list.add_todo("Buy groceries")
        self.todo_list.add_todo("Read a book")
        self.assertEqual(self.todo_list.get_todo_by_index(2), "Exercise")

if __name__ == "__main__":
    unittest.main()
