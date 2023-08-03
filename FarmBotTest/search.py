import pyautogui
from enum import Enum
import win32gui
import random
from time import sleep
from logger import logger

class Button(Enum):
	def __str__(self) -> str:
		return self.name.lower() + ".png" # png file ext only for now, maybe order file ext by value ? 1 = png 2 = jpg etc 

	FIND = 1
	GATHER = 2
	HELP_MOBILE = 3
	HELP_PC = 3
	MARCH = 4
	CREATELEGION = 5
	SEARCH = 6
	REMOVEHERO = 7
	ALLIANCE = 8
	RANKINGS = 9
	LEGIONLIMIT = 10

path = "FarmBotTest/resources/" # path to images
window_name =  "Call of Dragons BS"
window_rect = win32gui.GetWindowRect(win32gui.FindWindow(None, window_name))
logger.info(window_name + "'s position and size is  " + window_rect.__str__())

class ButtonNotFound(Exception):
	def __init__(self, *args: object) -> None:
		super().__init__(*args)

def random_float(a: float=0.1, b: float=0.5) -> float:
	return random.uniform(a, b)

def is_on_screen(button: Button, confidence: float=0.9)  -> bool:
	logger.debug("trying to find " + button.name)
	location = pyautogui.locateOnScreen(path + button.__str__(), region=window_rect, confidence=confidence)
	if location != None:
		logger.debug(button.name + " was found on screen")
		return True
	else:
		logger.debug(button.name + " could not be found on screen")
		return False

def click_button(button: Button, confidence: float=0.9, rest: int=1):
	logger.debug("trying to find " + button.name)
	location = pyautogui.locateOnScreen(path + button.__str__(), region=window_rect, confidence=confidence)
	if location == None:
		logger.debug(button.name + " could not be found")
		raise ButtonNotFound(str(button.name + " could not be found"))
	
	pyautogui.moveTo(location)
	sleep(random_float(0.5, 1.5))
	pyautogui.click(duration=random_float())
	
	sleep(rest)
	logger.debug(button.name + " was pressed")
