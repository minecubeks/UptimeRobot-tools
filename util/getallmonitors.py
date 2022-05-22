from util.plugins.common import *
mcount = 0

def monitorgetall():
	global mcount
	payload = f'api_key={apikey}&format=json'
	try:
		response = requests.request("POST", 'https://api.uptimerobot.com/v2/getMonitors', data=payload, headers=headers)
	except:
		print('Error')
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
		for id in response['monitors']:
			mcount+=1
			print('')
			print(f'Monitor #{mcount}:')
			print(f'{green}Monitor ID: {yellow}' + str(id['id']) + freset)
			print(f'{green}Monitor name: {yellow}' + id['friendly_name'] + freset)
		os.system('pause')
		from main import main
		mcount = 0
		main()