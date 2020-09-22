import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time =time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # image+시간정보.png로 저장

keyboard.add_hotkey("F9", screenshot) # 사용자가 F9키를 누르면 스크린샷 저장
# keyboard.add_hotkey("a", screenshot) # 사용자가 a키를 누르면 스크린샷 저장
# keyboard.add_hotkey("ctrl+shift+a", screenshot) # 사용자가 ctrl+shift+a키를 누르면 스크린샷 저장
keyboard.wait("esc") # 사용자가 exc를 누를 때까지 프로그램 수행