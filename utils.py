def parse_input(user_input: str):
    parts = user_input.strip().split()
    if not parts:
        return {"cmd": "invalid"}

    if parts[0].lower() == "cancel" and len(parts) == 2:
        return {"cmd": "cancel", "label": parts[1]}
    elif parts[0].lower() == "reset" and len(parts) == 2:
        return {"cmd": "reset", "label": parts[1]}
    elif len(parts) == 2:
        # 默认作为 start 处理
        return {"cmd": "start", "label": parts[0], "time": parts[1]}
    else:
        return {"cmd": "invalid"}
