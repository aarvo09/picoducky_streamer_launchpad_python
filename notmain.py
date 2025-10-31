import pyautogui
import time 

STREAMINGAPP = "stream labs"
CHATTINGAPP = "discord"
GAMINGSTORE = "steam"
MUSICAPP =     "spotify"
BROWSER =  "brave"

URL = "https://studio.youtube.com/channel/UCgIt-SVhtuaSRKJjkFFnifQ" #streamers can give there yt studio link there


def launch_app(app_name):
    print(f"launching app '{app_name}'...")
    pyautogui.press("win")
    time.sleep(1.2)

    pyautogui.write(app_name)
    time.sleep(1.5)
    
    pyautogui.press("enter")
    time.sleep(4)

def shift_window_left():
    print ("shifting window to left...")
    pyautogui.hotkey('win','left')
    time.sleep(0.8)

def shift_window_right():
    print ("shifting window to right ")
    pyautogui.hotkey('win','right')
    time.sleep(0.8)

print ("settingcup the streaming setup in ")
for i in range(5,0,-1):
    print(f"{i}..")
    time.sleep(1)
print("executing automation...")

try :
    print ("minmizing all windows..")
    pyautogui.hotkey('win','d')
    time.sleep(0.8)

    launch_app(CHATTINGAPP)
    launch_app(GAMINGSTORE)
    launch_app(MUSICAPP)
    launch_app(BROWSER)
    
    print("opening YouTube Studio dashboard...")
    time.sleep(2)  
    pyautogui.hotkey('ctrl', 'l') 
    time.sleep(0.5)
    pyautogui.write(URL, interval=0.05)  
    pyautogui.press('enter')
    time.sleep(3)
    
    launch_app(STREAMINGAPP)

    print ("setting up windows")
    time.sleep(2)
    print("switching to browser")
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.write(BROWSER)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1.5)
    print("shifting YouTube dashboard to left")
    shift_window_left()

    print("switching to Discord")
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.write(CHATTINGAPP)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1.5)
    print("shifting Discord to right")
    shift_window_right()

    print("now focusing on streamlabs")
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.write(STREAMINGAPP)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)

    print("streaming setup complete")

except Exception as e :
    print(f"error occurred : {e}")




