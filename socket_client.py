import socket
import os
import json
import subprocess
import time

HOST = "127.0.0.1"
PORT = 61420

def get_sandtimer_path():
    exe_path = os.path.join(os.path.dirname(__file__), "bin", "SandGlassTimer.exe")
    return exe_path if os.path.exists(exe_path) else ""

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
        except (ConnectionRefusedError, socket.timeout, OSError) as e:
            return False

    if try_send():
        return True

    exe_path = get_sandtimer_path()
    if try_launch_exe(exe_path):
        if try_send():
            return True
        else:
            # write_log("Second try_send after launch still failed.")
            pass
    else:
        # write_log("Executable launch failed.")
        pass

    # write_log("send_command returning False")
    return False

from datetime import datetime

# def write_log(msg: str):
#     desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
#     log_file = os.path.join(desktop_path, "flow_timer_debug_log.txt")
#     timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
#     with open(log_file, "a", encoding="utf-8") as f:
#         f.write(f"{timestamp} {msg}\n")