import sys
import os
from pathlib import Path
import win32file

# 添加 plugin 和 lib 路径到 sys.path
plugin_dir = Path(__file__).parent.absolute()
lib_dir = plugin_dir / "lib"
sys.path.insert(0, str(plugin_dir))
sys.path.insert(0, str(lib_dir))
# 添加 DLL 搜索路径
if hasattr(os, 'add_dll_directory'):
    os.add_dll_directory(str(lib_dir))
else:
    os.environ["PATH"] = str(lib_dir) + ";" + os.environ.get("PATH", "")

from flowlauncher import FlowLauncher
from commands import handle_query
from settings import __plugin_settings__
from socket_client import send_command
from utils import parse_input
import json

class TimerPlugin(FlowLauncher):
    def query(self, param: str = '') -> list:
        return handle_query(param)

    def do_command(self, data):
        try:
            # data 就是 handle_query 里传过来的 result 字典
            send_command(json.dumps(data))
            return []  # 不显示任何输出
        except Exception as e:
            return [{
                "Title": "Failed to send command",
                "SubTitle": str(e),
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {"method": "do_nothing", "parameters": []}
            }]

    def context_menu(self, data):
        return [{
            "Title": "context_menu",
            "SubTitle": "点击不会触发行为",
            "JsonRPCAction": {
                "method": "do_nothing",
                "parameters": []
            }
        }]

    def setting(self):
        return __plugin_settings__()

    def do_nothing(self, data=None):
        return [{
            "Title": "do_nothing",
            "SubTitle": "点击不会触发行为",
            "JsonRPCAction": {
                "method": "do_nothing",
                "parameters": []
            }
        }]


if __name__ == '__main__':
    TimerPlugin()

# # 插件测试
# from flowlauncher import FlowLauncher
#
#
# class TimerPlugin(FlowLauncher):
#     def query(self, param: str = '') -> list:
#         return [{
#             "Title": "测试",
#             "SubTitle": "点击不会触发行为",
#             "JsonRPCAction": {
#                 "method": "do_nothing",
#                 "parameters": []
#             }
#         }]
#
#     def do_nothing(self, data=None):
#         return []
#
#
# if __name__ == '__main__':
#     TimerPlugin()
