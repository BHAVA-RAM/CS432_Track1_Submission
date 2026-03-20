from .table import Table

class DatabaseManager:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, degree=4):
        if name in self.tables:
            print(f"Table '{name}' already exists.")
            return
        self.tables[name] = Table(name, degree)
        print(f"Table '{name}' created.")

    def get_table(self, name):
        if name not in self.tables:
            print(f"Table '{name}' not found.")
            return None
        return self.tables[name]

    def drop_table(self, name):
        if name in self.tables:
            del self.tables[name]
            print(f"Table '{name}' dropped.")
        else:
            print(f"Table '{name}' not found.")

    def list_tables(self):
        if not self.tables:
            print("No tables exist.")
        else:
            print("Tables:", list(self.tables.keys()))
