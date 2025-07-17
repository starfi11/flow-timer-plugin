#TEST_MESSAGE = '{"cmd": "start", "label": "test1", "time": 5}'
TEST_MESSAGE = '{"cmd": "cancel", "label": "test1"}'
# TEST_MESSAGE = '{"cmd": "reset", "label": "test"}'
from socket_client import send_command


if send_command(TEST_MESSAGE):
    print("✅ Message sent successfully!")
else:
    print("❌ Failed to connect or send message.")
