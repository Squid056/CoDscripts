from enum import IntEnum
from logger import logger
from time import sleep
from search import *
from tesseractsetup import *

class ResourceType(IntEnum):
	def __str__(self) -> str:
		return self.name

	GOLD = 1
	WOOD = 2
	STONE = 3
	MANA = 4
	# ALLIANCE_CENTER = 5

def get_rss_coords(type: ResourceType) -> tuple:	
	# TEMP HARD CODED LOCATIONS (1600 by 900 screen bluestacks)
	# GOLD  X:  490 Y:  777
	# WOOD  X:  726 Y:  777
	# STONE X:  974 Y:  777
	# MANA  X: 1200 Y:  777
	y = 777 + window_rect[1]
	match type:
		case ResourceType.GOLD:
			iconLocation = pyautogui.locateOnScreen("FarmBotTest/resources/gold_mine.png", region=window_rect, confidence=0.85)
			center = pyautogui.center(iconLocation)
			return (center.x, center.y) 
		case ResourceType.WOOD:
			iconLocation = pyautogui.locateOnScreen(path + Button.WOOD_CAMP.__str__(), region=window_rect, confidence=0.9)
			center = pyautogui.center(iconLocation)
			return (center.x, center.y) 
		case ResourceType.STONE:
			iconLocation = pyautogui.locateOnScreen(path + Button.ORE_MINE.__str__(), region=window_rect, confidence=0.9)
			center = pyautogui.center(iconLocation)
			return (center.x, center.y) 
		case ResourceType.MANA:
			iconLocation = pyautogui.locateOnScreen(path + Button.MANA_WELL.__str__(), region=window_rect, confidence=0.9)
			center = pyautogui.center(iconLocation)
			return (center.x, center.y) 

def Gather(rsstype: ResourceType) -> bool:
	# run through the actions of creating a legion to farm selected resource, raise exeptions to be caught during this process
	logger.info("Attemping to farm " + rsstype.__str__())

	click_button(Button.FIND, 0.8)
	pyautogui.click(get_rss_coords(rsstype), duration=random_float())
	sleep(2)
	click_button(Button.SEARCH, rest=2)
	# temp move to center (click on the found rss node)
	center = pyautogui.center(window_rect)
	pyautogui.moveTo(center.x-140, center.y-30, random.uniform(0.1, 0.5))
	pyautogui.click(duration=random_float())
	sleep(2)
	# --
	click_button(Button.GATHER, rest=2)
	click_button(Button.CREATELEGION, rest=2)
	click_button(Button.REMOVEHERO, rest=2)
	click_button(Button.MARCH, rest=2)
	logger.info("legion deployed to farm " + rsstype.__str__())

def legion_overview_check() -> tuple[bool, int]:
	logger.debug("checking if legion count is full")
	pyautogui.press("j") # j is a custom keybind on bluestacks to open legion menu
	sleep(2)
	if not is_on_screen(Button.LEGIONLIMIT):
		logger.debug("legion overview failed to open")
		return (False, -1)
	limitIconLocation = pyautogui.locateOnScreen(path + "legionlimit.png", region=window_rect, confidence=0.9)
	countLocation = (limitIconLocation[0] + limitIconLocation[2], limitIconLocation[1], 55, 30) 
	legionImg = pyautogui.screenshot(region=countLocation)

	deployed = str(pytesseract.image_to_string(legionImg))
	count = deployed.split('/')
	if count[0] != count[1]:
		remainingLegions = int(count[1]) - int(count[0])
		logger.debug("legion count not full, can deploy " + remainingLegions.__str__() + " more legions")
		pyautogui.press("j") # j is a custom keybind on bluestacks to open legion menu
		return (True, remainingLegions)
	else:
		logger.debug("legion count is full")
		pyautogui.press("j") # j is a custom keybind on bluestacks to open legion menu
		return (False, 0)

sleep(1)
get_rss_coords(ResourceType.GOLD)