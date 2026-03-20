from .bplustree import bplustree

class Table:
    def __init__(self, name, degree=4):
        self.name = name
        self.tree = bplustree(degree)

    def insert(self, key, record):
        self.tree.insert(key, record)

    def select(self, key):
        found, value = self.tree.search(key)
        if found:
            return value
        return None

    def update(self, key, record):
        return self.tree.update(key, record)

    def delete(self, key):
        return self.tree.delete(key)

    def range_query(self, start, end):
        return self.tree.range_query(start, end)

    def all_records(self):
        return self.tree.get_all()

    def visualize(self):
        return self.tree.visualize_tree(filename=self.name)
