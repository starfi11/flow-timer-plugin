import sys
import os
from pathlib import Path

# 添加 plugin 和 lib 路径到 sys.path
plugin_dir = Path(__file__).parent.absolute()
sys.path.insert(0, str(plugin_dir))
sys.path.insert(0, str(plugin_dir / "lib"))

from flowlauncher import FlowLauncher
from commands import handle_query
from settings import __plugin_settings__

class TimerPlugin(FlowLauncher):
    def query(self, query):
        results = handle_query(query)
        # import json
        # print("PLUGIN OUTPUT:", json.dumps(results, indent=2))
        return results

    def context_menu(self, data):
        return []

    def setting(self):
        return __plugin_settings__()

if __name__ == '__main__':
    TimerPlugin()
