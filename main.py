import json
import schedule
import time
import requests
import pystray
from PIL import Image


serversToCheck=[]
icon = pystray.Icon(
    'MC Server Checker',
    icon=Image.open('icon.ico'),
	title="MC Server Checker is running")


def check():
	for server in serversToCheck:
		try:
			response = requests.get(f"https://api.minetools.eu/ping/{server['host']}/{server['port']}")
			data = response.json()
			if data["players"]["online"] == 0:
				print(f"{server['name']} has no players online")
			else:
				print(f"{server['name']} has {data['players']['online']}/{data['players']['max']} players online")
				icon.notify(f"{data['players']['online']} online",f"{server['name']}")
				icon.remove_notification()
		except:
			print(f"{server['name']} is offline")

with open("config.json") as json_data_file:
	icon.run_detached()
	data = json.load(json_data_file)
	serversToCheck=data["servers"]
	check()
	schedule.every(data["checkInterval"]).minutes.do(check)
	while True:
		schedule.run_pending()
		time.sleep(60)