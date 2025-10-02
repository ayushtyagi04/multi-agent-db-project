from agent_swarm import get_llm
from agents import CSVAgent, ExcelAgent, SQLiteAgent, SQLAgent

import json

llm = get_llm()
csv_agent = CSVAgent(llm)
excel_agent = ExcelAgent(llm)
sqlite_agent = SQLiteAgent(llm)
sql_agent = SQLAgent(llm)

def parse_command(command):
    prompt = (
        f"Parse this command into JSON with keys: 'db_type', 'action', 'target', "
        f"'column', 'value', 'condition_column', 'condition_value', 'upload_path' (optional): {command}. Output only JSON."
    )
    response = llm(prompt)
    json_str = response[response.find('{'):response.rfind('}')+1]
    return json.loads(json_str)

def determine_agent(db_type):
    if db_type == 'csv':
        return csv_agent
    elif db_type == 'excel':
        return excel_agent
    elif db_type == 'sqlite':
        return sqlite_agent
    elif db_type == 'sql':
        return sql_agent
    else:
        return None

def manager_agent(command):
    parsed = parse_command(command)
    db_type = parsed.get('db_type')
    agent = determine_agent(db_type)
    if agent:
        return agent.handle_command(parsed)
    else:
        return "Unsupported database type"
