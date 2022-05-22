from util.plugins.common import *

def monitoredit(id, name=None, url=None, port=None, interval=None, timeout=None, status=None, editnum=None):
	if editnum == 1:
		payload = f'api_key={apikey}&format=json&id={id}&friendly_name={name}'
	if editnum == 2:
		payload = f'api_key={apikey}&format=json&id={id}&url={url}'
	if editnum == 3:
		payload = f'api_key={apikey}&format=json&id={id}&port={port}'
	if editnum == 4:
		payload = f'api_key={apikey}&format=json&id={id}&interval={interval}'
	if editnum == 5:
		payload = f'api_key={apikey}&format=json&id={id}&timeout={timeout}'
	if editnum == 6:
		payload = f'api_key={apikey}&format=json&id={id}&status={status}'
	try:
		response = requests.request("POST", 'https://api.uptimerobot.com/v2/editMonitor', data=payload, headers=headers)
	except:
		print(response)
		quit()
	response = json.loads(response.text)
	if response['stat'] == 'fail':
		print(' ')
		print(red + 'Error:' + freset)
		print(response['error']['message'])
		os.system('pause')
		from main import main
		main()
	else:
		print('')
		print(f'Monitor edited')
		if editnum == 1:
			print(green + f'New name: {yellow}{name}' + freset)
		if editnum == 2:
			print(green + f'New url/ip: {yellow}{url}' + freset)
		if editnum == 3:
			print(green + f'New port: {yellow}{port}' + freset)
		if editnum == 4:
			print(green + f'New interval: {yellow}{interval}' + freset)
		if editnum == 5:
			print(green + f'New timeout: {yellow}{timeout}' + freset)
		if editnum == 6:
			if status == '1':
				print(green + f'New status: {yellow}resumed' + freset)
			else:
				print(green + f'New status: {yellow}paused' + freset)
		print(green + 'press enter to contonue')
		os.system('pause')
		from main import mainreq
		mainreq(2, id)