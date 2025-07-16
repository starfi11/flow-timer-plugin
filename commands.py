from socket_client import send_command
from utils import parse_input
import json


def handle_query(user_input: str):
    try:
        result = parse_input(user_input)
        cmd = result.get("cmd", "invalid")
        label = result.get("label", "")
        seconds = result.get("time", 0)

        if cmd == "invalid":
            return [{
                "Title": "Invalid command",
                "SubTitle": "Usage: [label + time], or cancel/reset",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {"method": "do_nothing", "parameters": []}
            }]

        # Compose subtitle
        if cmd == "start":
            subtitle = f"Start timer: '{label}' for {seconds:.1f} seconds"
        elif cmd == "cancel":
            subtitle = f"Cancel timer: '{label}'"
        elif cmd == "reset":
            subtitle = f"Reset timer: '{label}'"
        else:
            subtitle = "Unknown command"

        # Send socket command
        try:
            send_command(json.dumps(result))
        except Exception as e:
            return [{
                "Title": "Socket error",
                "SubTitle": str(e),
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {"method": "do_nothing", "parameters": []}
            }]

        return [{
            "Title": f"{cmd} {label}",
            "SubTitle": subtitle,
            "IcoPath": "Images/app.png",
            "JsonRPCAction": {"method": "do_nothing", "parameters": []}
        }]

    except Exception as e:
        return [{
            "Title": "Internal error",
            "SubTitle": str(e),
            "IcoPath": "Images/app.png",
            "JsonRPCAction": {"method": "do_nothing", "parameters": []}
        }]
