from util.plugins.common import *

def monitordelete(id):
	payload = f'api_key={apikey}&format=json&id={id}'
	try:
		response = requests.request("POST", 'https://api.uptimerobot.com/v2/deleteMonitor', data=payload, headers=headers)
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
		print(f'Monitor deleted with ID', response['monitor']['id'])
		os.system('pause')
		from main import main
		main()