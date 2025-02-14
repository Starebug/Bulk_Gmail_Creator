import time
import random
import pyautogui

def human_like_delay(min_time=1, max_time=3):
    """
    Pauses execution for a random duration between min_time and max_time seconds.
    This simulates a natural human delay between actions.
    """
    delay = random.uniform(min_time, max_time)
    time.sleep(delay)

def human_like_move(x, y, min_duration=1, max_duration=2):
    """
    Moves the mouse to the coordinates (x, y) with a randomized duration and then clicks.
    
    Parameters:
      - x, y: Coordinates where the mouse should move.
      - min_duration: The minimum duration (in seconds) for the mouse movement.
      - max_duration: The maximum duration (in seconds) for the mouse movement.
    """
    duration = random.uniform(min_duration, max_duration)
    pyautogui.moveTo(x, y, duration=duration)
