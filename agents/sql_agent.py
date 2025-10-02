from database import sql_delete_rows, sql_add_column, sql_update_rows, sql_read_rows
import os

class SQLAgent:
    def __init__(self, llm):
        self.llm = llm
        self.conn_str = os.getenv('SQL_CONN_STRING')

    def handle_command(self, parsed):
        action = parsed['action']
        target = parsed['target']  # Table name
        column = parsed.get('column')
        value = parsed.get('value')
        condition_column = parsed.get('condition_column')
        condition_value = parsed.get('condition_value')

        if not self.conn_str:
            return "SQL connection string not configured"

        if action == "delete":
            return sql_delete_rows(self.conn_str, target, column, value)
        elif action == "add_column":
            return sql_add_column(self.conn_str, target, column)
        elif action == "update":
            return sql_update_rows(self.conn_str, target, column, value, condition_column, condition_value)
        elif action == "read":
            data = sql_read_rows(self.conn_str, target, condition_column, condition_value)
            return data
        else:
            return "Unsupported SQL action"
