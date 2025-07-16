import re


def is_time_string(s: str) -> bool:
    pattern = r'^(\d+(\.\d+)?h)?(\d+(\.\d+)?m)?(\d+(\.\d+)?s)?$'
    if not s:
        return False
    return bool(re.fullmatch(pattern, s))


def parse_input(user_input: str):
    if user_input.startswith("timer "):
        user_input = user_input[6:]
    parts = user_input.strip().split()
    if not parts:
        return {"cmd": "invalid"}
    if parts[0].lower() == "cancel" and len(parts) == 2:
        return {"cmd": "cancel", "label": parts[1]}
    elif parts[0].lower() == "reset" and len(parts) == 2:
        return {"cmd": "reset", "label": parts[1]}
    elif parts[0].lower() == 'start' and len(parts) == 3 and is_time_string(parts[2]):
        return {"cmd": "start", "label": parts[1], "time": parse_time_string_to_seconds(parts[2])}
    elif len(parts) == 2 and is_time_string(parts[1]):
        # 默认作为 start 处理
        return {"cmd": "start", "label": parts[0], "time": parse_time_string_to_seconds(parts[1])}
    elif len(parts) == 1 and is_time_string(parts[0]):
        # 匿名启动
        return {"cmd": "start", "label": "timer", "time": parse_time_string_to_seconds(parts[0])}
    else:
        return {"cmd": "invalid"}


def parse_time_string_to_seconds(s: str) -> float:
    """
    解析时间字符串为秒数，支持格式如：
    '1h', '1.5h30m', '30m20s', '20s1.25h' 等，无单位顺序限制。
    """
    if not s:
        return 0.0

    # 正则匹配所有带单位的段，允许浮点数
    pattern = r'(\d+(?:\.\d+)?)([hms])'
    matches = re.findall(pattern, s)
    if not matches:
        raise ValueError(f"Invalid time string format: '{s}'")

    seconds = 0.0
    used_units = set()

    for value_str, unit in matches:
        if unit in used_units:
            raise ValueError(f"Duplicate unit '{unit}' in time string: '{s}'")
        used_units.add(unit)

        value = float(value_str)
        if unit == 'h':
            seconds += value * 3600
        elif unit == 'm':
            seconds += value * 60
        elif unit == 's':
            seconds += value

    return seconds
