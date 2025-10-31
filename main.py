import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

STREAMINGAPP = "stream labs"
CHATTINGAPP = "discord"
GAMINGSTORE = "steam"
MUSICAPP = "spotify"
BROWSER = "brave"

URL = "studio.youtube.com/channel/UCgIt-SVhtuaSRKJjkFFnifQ" #streamers can give there yt studio link there

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

def press_keys(*keys):
    kbd.press(*keys)
    time.sleep(0.1)
    kbd.release_all()
    time.sleep(0.2)

def type_text(text):
    layout.write(text)
    time.sleep(0.05)

def launch_app(app_name):
    print(f"launching app '{app_name}'")
    
    press_keys(Keycode.GUI)
    time.sleep(1.2)

    type_text(app_name)
    time.sleep(1.5)

    press_keys(Keycode.ENTER)
    time.sleep(4) 

def shift_window_left():
    print("shifting window to left")
    press_keys(Keycode.GUI, Keycode.LEFT_ARROW)
    time.sleep(0.8)

def shift_window_right():
    print("shifting window to right")
    press_keys(Keycode.GUI, Keycode.RIGHT_ARROW)
    time.sleep(0.8)

print("settingup the live setup in ")
for i in range (5,0,-1):
    print(f"{i}")
    time.sleep(1)

print("minmizing all windows")
press_keys(Keycode.GUI, Keycode.D)
time.sleep(0.8)

launch_app(CHATTINGAPP)
launch_app(GAMINGSTORE)
launch_app(MUSICAPP)
launch_app(BROWSER)

print("opening YouTube Studio dashboard")
time.sleep(2) 

press_keys(Keycode.CONTROL, Keycode.L) 
time.sleep(0.5)
type_text(URL) 
press_keys(Keycode.ENTER)
time.sleep(3) 

launch_app(STREAMINGAPP)

print("setting up windows")
time.sleep(2)

print("switching to browser")
launch_app(BROWSER) 
time.sleep(1.5)

print("shifting YouTube dashboard to left")
shift_window_left()

print("switching to Discord")
launch_app(CHATTINGAPP) 
time.sleep(1.5)

print("shifting Discord to right")
shift_window_right()

print("now focusing on streamlabs")
launch_app(STREAMINGAPP)
time.sleep(1)

print("streaming setup complete")