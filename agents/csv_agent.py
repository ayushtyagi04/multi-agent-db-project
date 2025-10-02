from database import csv_delete_rows, csv_add_column, csv_update_rows, csv_read_rows, upload_file

class CSVAgent:
    def __init__(self, llm):
        self.llm = llm

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

        if action == "delete":
            return csv_delete_rows(target, column, value)
        elif action == "add_column":
            return csv_add_column(target, column)
        elif action == "update":
            return csv_update_rows(target, column, value, condition_column, condition_value)
        elif action == "read":
            data = csv_read_rows(target, condition_column, condition_value)
            return data
        else:
            return "Unsupported CSV action"
