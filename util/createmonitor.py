from util.plugins.common import *

def monitorcreate(type, url, name, subtype=None, port=None, keywordtype=None, keywordvalue=None, interval=300, timeout=60, httpname=None, httppass=None, httpauthtype=None, posttype=None, postvalue=None, httpmethod=None):
	if type == '5':
		payload = f'api_key={apikey}&format=json&type={type}&friendly_name={name}'
	if type == '4':
		payload = f'api_key={apikey}&format=json&type={type}&url={url}&friendly_name={name}&sub_type={subtype}&port={port}&interval={interval}&timeout={timeout}'
	if type == '3':
		payload = f'api_key={apikey}&format=json&type={type}&friendly_name={name}&url={url}&interval={interval}'
	if type == '1':
		payload = f'api_key={apikey}&format=json&type={type}&friendly_name={name}&url={url}&interval={interval}&timeout={timeout}'
	try:
		response = requests.request("POST", 'https://api.uptimerobot.com/v2/newMonitor', data=payload, headers=headers)
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
		print(f'Monitor created with ID', response['monitor']['id'])
		os.system('pause')
		from main import main
		main()