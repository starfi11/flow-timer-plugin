import win32file
import win32pipe
import pywintypes

PIPE_NAME = r'\\.\pipe\sandtimer_socket'
TEST_MESSAGE = '{"cmd": "start", "label": "test", "time": 5}'

try:
    print(f"Connecting to pipe: {PIPE_NAME}")
    handle = win32file.CreateFile(
        PIPE_NAME,
        win32file.GENERIC_WRITE,
        0,
        None,
        win32file.OPEN_EXISTING,
        0,
        None
    )

    win32file.WriteFile(handle, TEST_MESSAGE.encode('utf-8'))
    print("✅ Message sent successfully!")

except pywintypes.error as e:
    print(f"❌ Failed to connect or send message: {e}")
