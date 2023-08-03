from gather import *
import keyboard
import time
from win32gui import GetWindowText, GetForegroundWindow


cycleCounter = 1
currentRSS = 1
 
while True:
	if keyboard.is_pressed("e"):
		logger.debug("Exiting bot loop.")
		break
	
	if GetWindowText(GetForegroundWindow()) != "Call Of Dragons BS":
		continue

	try:
		click_button(Button.HELP_MOBILE)
	except ButtonNotFound:
		logger.debug("help could not be performed on cycle " + cycleCounter.__str__())

	legions = legion_overview_check() # find a way to open this when there are no legions currently out of city
	sleep(2)
	if legions[0] == True and legions[1] > 0:
		try:
			Gather(rsstype=currentRSS)
			if currentRSS < 4:
				currentRSS += 1
			else:
				currentRSS = 1
		except ButtonNotFound:
			logger.debug("temp gather bug")

	time.sleep(6)
	logger.debug("completed cycle " + cycleCounter.__str__())
	cycleCounter += 1
	
	

# TODO
# proper debug message function with timestamps!!
# get gather  function working ( send march, dont send if max legions are out)
# get a working gather loop 

# gather_rss(ResourceType.GOLD)

