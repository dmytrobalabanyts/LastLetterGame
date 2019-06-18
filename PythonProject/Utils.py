
import json

def format_notification(command, data):
    result = {}
    result["command"] = command
    result["data"] = data
    return json.dumps(result) 