from database import sqlite_delete_rows, sqlite_add_column, sqlite_update_rows, sqlite_read_rows, upload_file

class SQLiteAgent:
    def __init__(self, llm):
        self.llm = llm
        self.default_table = "data"

    def handle_command(self, parsed):
        if "upload_path" in parsed:
            file_path = upload_file(parsed["upload_path"])
            return f"File uploaded to {file_path}"

        action = parsed['action']
        target = parsed['target']
        column = parsed.get('column')
        value = parsed.get('value')
        condition_column = parsed.get('condition_column')
        condition_value = parsed.get('condition_value')
        table = self.default_table

        if action == "delete":
            return sqlite_delete_rows(target, table, column, value)
        elif action == "add_column":
            return sqlite_add_column(target, table, column)
        elif action == "update":
            return sqlite_update_rows(target, table, column, value, condition_column, condition_value)
        elif action == "read":
            data = sqlite_read_rows(target, table, condition_column, condition_value)
            return data
        else:
            return "Unsupported SQLite action"
