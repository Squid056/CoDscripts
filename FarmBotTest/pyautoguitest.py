from gather import *
import keyboard
import time
from win32gui import GetWindowText, GetForegroundWindow


cycleCounter = 1
currentRSS = 1
sleepTimer = 6 # in seconds

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

	legions = legion_overview_check() # find a way to open this when sthere are no legions currently out of city
	sleep(2)
	if legions[0] == True and legions[1] > 0:
		sleepTimer = 6 # shorten cycle timer to put out gather legions
		try:
			Gather(rsstype=currentRSS)
			if currentRSS < 4:
				currentRSS += 1
			else:
				currentRSS = 1
		except ButtonNotFound:
			logger.debug("temp gather bug")
	elif legions[0] == False and legions[1] == 0:
		logger.debug("set cycle timer to 6mins")
		sleepTimer = 360 # increase cycle timer since all legions are farming
	
	time.sleep(6)
	logger.debug("completed cycle " + cycleCounter.__str__())
	cycleCounter += 1
	
	

# TODO
# get game state from looking at screen
# alliance donations ?
