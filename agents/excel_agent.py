from database import excel_delete_rows, excel_add_column, excel_update_rows, excel_read_rows, upload_file

class ExcelAgent:
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
        sheet = "Sheet1"

        if action == "delete":
            return excel_delete_rows(target, sheet, column, value)
        elif action == "add_column":
            return excel_add_column(target, sheet, column)
        elif action == "update":
            return excel_update_rows(target, sheet, column, value, condition_column, condition_value)
        elif action == "read":
            data = excel_read_rows(target, sheet, condition_column, condition_value)
            return data
        else:
            return "Unsupported Excel action"
