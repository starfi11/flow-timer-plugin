import socket
import os
import json
import subprocess
import time

SOCKET_NAME = r'\\.\pipe\sandglass_socket'

def get_sandglass_path():
    config_path = os.path.join(os.path.dirname(__file__), 'Settings.json')
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            return config.get("sandglass_path", "")
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

def send_command(cmd: str):
    try:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(SOCKET_NAME)
        s.sendall(cmd.encode('utf-8'))
        s.close()
    except Exception:
        exe_path = get_sandglass_path()
        launched = try_launch_exe(exe_path)
        if launched:
            try:
                s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                s.connect(SOCKET_NAME)
                s.sendall(cmd.encode('utf-8'))
                s.close()
                return
            except Exception:
                pass

        print(json.dumps([{
            "Title": "发送失败：沙漏服务不可用",
            "SubTitle": f"尝试启动服务失败，请检查路径是否正确：{exe_path}"
        }]))
