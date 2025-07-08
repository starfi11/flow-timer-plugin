import sys
import json
from socket_client import send_command
from utils import parse_input

def main():
    raw = sys.stdin.read()
    query = json.loads(raw)

    user_input = query.get("Parameters", "")
    if not user_input:
        # 空输入返回提示
        print(json.dumps([{
            "Title": "请输入: 计时器名称 + 时间，如 '泡茶 20m'",
            "SubTitle": "示例: timer 泡茶 20m",
            "IcoPath": "Images\\app.png"
        }]))
        return

    result = parse_input(user_input)

    if result["cmd"] == "start":
        label = result["label"]
        time_str = result["time"]
        command_str = f"start {label} {time_str}"
        subtitle = f"开始计时：{label} - {time_str}"
    elif result["cmd"] == "cancel":
        command_str = f"cancel {result['label']}"
        subtitle = f"取消计时器：{result['label']}"
    elif result["cmd"] == "reset":
        command_str = f"reset {result['label']}"
        subtitle = f"重置计时器：{result['label']}"
    else:
        print(json.dumps([{
            "Title": "命令格式错误",
            "SubTitle": "支持: [计时器名 + 时间] / cancel / reset",
        }]))
        return

    # 实际发送命令
    send_command(command_str)

    # 返回 Flow 候选项
    print(json.dumps([{
        "Title": command_str,
        "SubTitle": subtitle,
        "IcoPath": "Images\\app.png"
    }]))

if __name__ == "__main__":
    main()
