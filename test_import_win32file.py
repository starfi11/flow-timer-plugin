import sys, os

lib_dir = os.path.join(os.path.dirname(__file__), 'lib')
sys.path.insert(0, lib_dir)
if hasattr(os, 'add_dll_directory'):
    os.add_dll_directory(lib_dir)

import win32file
print("✅ win32file 导入成功")
