import socket
import os
import json
import subprocess
import time
import win32file
import win32pipe
import pywintypes
SOCKET_NAME = r'\\.\pipe\sandtimer_socket'

def get_sandglass_path():
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

def send_command(cmd: str):
    try:
        # 尝试连接管道并发送消息
        handle = win32file.CreateFile(
            SOCKET_NAME,
            win32file.GENERIC_WRITE,
            0,
            None,
            win32file.OPEN_EXISTING,
            0,
            None
        )
        win32file.WriteFile(handle, cmd.encode('utf-8'))
        win32file.CloseHandle(handle)
        return True

    except pywintypes.error as e:
        # 启动服务进程（例如 Qt 端）再重试
        exe_path = get_sandglass_path()
        launched = try_launch_exe(exe_path)
        if launched:
            try:
                # 重试连接
                handle = win32file.CreateFile(
                    SOCKET_NAME,
                    win32file.GENERIC_WRITE,
                    0,
                    None,
                    win32file.OPEN_EXISTING,
                    0,
                    None
                )
                win32file.WriteFile(handle, cmd.encode('utf-8'))
                win32file.CloseHandle(handle)
                return True
            except pywintypes.error:
                pass  # 第二次失败也吞掉
    return False