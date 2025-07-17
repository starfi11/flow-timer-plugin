import win32file
import win32pipe
import pywintypes

PIPE_NAME = r'\\.\pipe\sandtimer_socket'
#TEST_MESSAGE = '{"cmd": "start", "label": "test1", "time": 5}'
TEST_MESSAGE = '{"cmd": "cancel", "label": "test1"}'
# TEST_MESSAGE = '{"cmd": "reset", "label": "test"}'
from socket_client import send_command
try:
    # print(f"Connecting to pipe: {PIPE_NAME}")
    # handle = win32file.CreateFile(
    #     PIPE_NAME,
    #     win32file.GENERIC_WRITE,
    #     0,
    #     None,
    #     win32file.OPEN_EXISTING,
    #     0,
    #     None
    # )
    #
    # win32file.WriteFile(handle, TEST_MESSAGE.encode('utf-8'))
    send_command(TEST_MESSAGE)
    print("✅ Message sent successfully!")

except pywintypes.error as e:
    print(f"❌ Failed to connect or send message: {e}")
