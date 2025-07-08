from socket_client import send_command
from utils import parse_input

def handle_query(user_input: str):
    results = []
    result = parse_input(user_input)

    if result["cmd"] == "start":
        label = result["label"]
        time_str = result["time"]
        cmd_str = f"start {label} {time_str}"
        subtitle = f"开始计时：{label} - {time_str}"
    elif result["cmd"] == "cancel":
        cmd_str = f"cancel {result['label']}"
        subtitle = f"取消计时器：{result['label']}"
    elif result["cmd"] == "reset":
        cmd_str = f"reset {result['label']}"
        subtitle = f"重置计时器：{result['label']}"
    else:
        return [{
            "Title": "命令格式错误",
            "SubTitle": "支持: [计时器名 + 时间] / cancel / reset",
        }]

    send_command(cmd_str)

    results.append({
        "Title": cmd_str,
        "SubTitle": subtitle,
        "IcoPath": "Images\\app.png",
        "JsonRPCAction": {
            "method": "do_nothing",
            "parameters": [],
            "dontHideAfterAction": False
        }
    })

    return results
