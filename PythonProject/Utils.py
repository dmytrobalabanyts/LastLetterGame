
import json

def format_command(command, data):
    result = {}
    result["command"] = command
    result["data"] = data
    return json.dumps(result)