import time
import random
import pyautogui

def human_like_delay(min_time=1, max_time=3):
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)

def human_like_move(x, y, min_duration=1, max_duration=2):
    duration = random.uniform(min_duration, max_duration)
    pyautogui.moveTo(x, y, duration=duration)
