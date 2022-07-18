from time import sleep
import pyautogui as auto
import schedule, webbrowser
import datetime
from cal_setup import get_calendar_service

def get_event():
	service = get_calendar_service()
	now = datetime.datetime.utcnow().isoformat() + 'Z'
	events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=1,
	singleEvents=True, orderBy='startTime').execute()
	events=events_result.get('items', [])
	if  not events:
		print('No upcoming event found')
	for event in events:
		start = event['start'].get('dateTime', event['start'].get('date'))
		new_time = start[11:16]
		new_link = event['hangoutLink']
		return new_time, new_link

def join():
	webbrowser.open_new_tab(link)
	sleep(10)
	auto.hotkey('ctrl', 'd')
	auto.hotkey('ctrl', 'e')
	auto.click(1355, 629)

time, link = get_event()
print(time, link)
schedule.every().day.at(time).do(join)

while True:
	schedule.run_pending()
	sleep(1)