import socket
import os
import json
import subprocess
import time

HOST = "127.0.0.1"
PORT = 61420

def get_sandtimer_path():
    config_path = os.path.join(os.path.dirname(__file__), 'Settings.json')
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            return config.get("sandtimer_path", "")
    return ""

def try_launch_exe(path: str) -> bool:
    if not os.path.exists(path):
        return False
    try:
        subprocess.Popen([path], creationflags=subprocess.CREATE_NO_WINDOW)
        time.sleep(0.5)
        return True
    except Exception:
        return False

def send_command(cmd: str) -> bool:
    def try_send():
        try:
            with socket.create_connection((HOST, PORT), timeout=1) as s:
                s.sendall(cmd.encode('utf-8'))
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False

    if try_send():
        return True

    exe_path = get_sandtimer_path()
    if try_launch_exe(exe_path):
        return try_send()

    return False