from manager_agent import manager_agent
import json

if __name__ == "__main__":
    print("Multi-Agent Database Management System Started.")
    while True:
        user_command = input("\nEnter your command:\n")
        try:
            result = manager_agent(user_command)
            if isinstance(result, list):
                # Pretty print records if result is a list of dicts
                print(json.dumps(result, indent=2))
            else:
                print(result)
        except Exception as e:
            print(f"Error during processing: {e}")
