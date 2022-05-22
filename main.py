from util.plugins.common import *
from util.createmonitor import *
from util.deletemonitor import *
from util.getallmonitors import *
from util.editmonitor import *
if config['api_key'] == "":
	print(red + 'API Key is not set!')
	os.system('pause')
	quit()
else:
	apikey = config['api_key']

def mainreq(selection ,id=None):
	if selection == 1:
		setTitle(f'UptimeRobot Tools v{this_ver} │ Get All Monitors')
		os.system('cls')
		banner()
		monitorgetall()
  
	if selection == 2:
		setTitle(f'UptimeRobot Tools v{this_ver} │ Edit Monitor')
		os.system('cls')
		banner()
		if id == None:
			print(green + f'Enter monitor ID: {lightblack}' + freset)
			monitorid = input(blue + '>> ' + freset)
		else:
			monitorid = id
		print('What you want to edit:')
		print(f"""{freset}[{cyan}1{freset}]{lightblack} Name
{freset}[{cyan}2{freset}]{lightblack} URL or IP
{freset}[{cyan}3{freset}]{lightblack} Port
{freset}[{cyan}4{freset}]{lightblack} Interval
{freset}[{cyan}5{freset}]{lightblack} Timeout
{freset}[{cyan}6{freset}]{lightblack} Status
	""")
		while True:
			try:
				option2 = int(input(blue + '>> ' + freset))
			except ValueError:
				continue
			else:
				if option2 in range(1,7):
					if option2 == 1:
						print(green + 'Enter new name for monitor:' + freset)
						monitornewname = input(blue + '>> ' + freset)
						monitoredit(monitorid, monitornewname, None, None, None, None, None, 1)
					if option2 == 2:
						print(green + 'Enter new URL or IP for monitor:' + freset)
						monitornewurl = input(blue + '>> ' + freset)
						monitoredit(monitorid, None, monitornewurl, None, None, None, None, 2)
					if option2 == 3:
						print(green + 'Enter new port for monitor:' + freset)
						monitornewport = input(blue + '>> ' + freset)
						monitoredit(monitorid, None, None, monitornewport, None, None, None, 3)
					if option2 == 4:
						print(green + f'Enter new interval for monitor: {lightblack}(in seconds)' + freset)
						monitornewinterval = input(blue + '>> ' + freset)
						monitoredit(monitorid, None, None, None, monitornewinterval, None, None, 4)
					if option2 == 5:
						print(green + f'Enter new timeout for monitor: {lightblack}(1-60 seconds)' + freset)
						monitornewtimeout = input(blue + '>> ' + freset)
						monitoredit(monitorid, None, None, None, None, monitornewtimeout, None, 5)
					if option2 == 6:
						print(green + f'Enter new status for monitor: {lightblack}(1= pause, 2= resume)' + freset)
						monitornewstatus = input(blue + '>> ' + freset)
						monitoredit(monitorid, None, None, None, None, None, monitornewstatus, 6)
					break
				else:
					print(Fore.RED + 'Invalid selection! (1-6)' + freset)
					continue
  
	if selection == 3:
		setTitle(f'UptimeRobot Tools v{this_ver} │ Create Monitor')
		os.system('cls')
		banner()
		print(green + f'Enter type: {lightblack}(1= HTTP(s), 2= Keyword, 3= Ping, 4= Port, 5= Heartbeat)' + freset)
		monitortype = input(blue + '>> ' + freset)
		print(green + 'URL or IP:' + freset)
		monitorurl = input(blue + '>> ' + freset)
		print(green + 'Frinedly name:' + freset)
		monitorname = input(blue + '>> ' + freset)
		if monitortype == '4':
			print(green + f'Sub_type: {lightblack}1= HTTP, 2= HTTPS, 3= FTP, 4= SMTP, 5= POP3, 6= IMAP, 99= Custom Port)' + freset)
			monitorsubtype = input(blue + '>> ' + freset)
			if monitorsubtype == '99':
				print(green + f'Port: ' + freset)
				monitorport = input(blue + '>> ' + freset)
				print(green + 'Want to define more parameters? (Y/N)' + freset)
				wantmorepar = input(blue + '>> ' + freset)
				if wantmorepar == 'N':
					monitorcreate(monitortype, monitorurl, monitorname, monitorsubtype, monitorport)
				else:
					print(green + f'Interval: {lightblack}(in seconds)' + freset)
					monitorinterval = input(blue + '>> ' + freset)
					print(green + f'Timeout: {lightblack}(1-60 seconds)' + freset)
					monitortimeout = input(blue + '>> ' + freset)
					monitorcreate(monitortype, monitorurl, monitorname, monitorsubtype, monitorport, None, None , monitorinterval, monitortimeout)
			else:
				monitorcreate(monitortype, monitorurl, monitorname, monitorsubtype)
		if monitortype == '2':
			print(green + 'Want to define more parameters? (Y/N)' + freset)
			wantmorepar = input(blue + '>> ' + freset)
		if monitortype == '1':
			print(green + 'Want to define more parameters? (Y/N)' + freset)
			wantmorepar = input(blue + '>> ' + freset)
			if wantmorepar == 'N':
				monitorcreate(monitortype, monitorurl, monitorname)
			else:
				print(green + f'Interval: {lightblack}(in seconds)' + freset)
				monitorinterval = input(blue + '>> ' + freset)
				print(green + f'Timeout: {lightblack}(1-60 seconds)' + freset)
				monitortimeout = input(blue + '>> ' + freset)
				monitorcreate(monitortype, monitorurl, monitorname, None, None, None, None , monitorinterval, monitortimeout)
				

	if selection == 4:
		setTitle(f'UptimeRobot Tools v{this_ver} │ Delete Monitor')
		os.system('cls')
		banner()
		print(green + f'Enter monitor ID: {lightblack}' + freset)
		monitorid = input(blue + '>> ' + freset)
		monitordelete(monitorid)
def main():
	os.system('cls')
	setTitle(f'UptimeRobot Tools v{this_ver}')
	banner()
	print(f"""{freset}[{cyan}1{freset}]{lightblack} Get all monitors
{freset}[{cyan}2{freset}]{lightblack} Edit monitor
{freset}[{cyan}3{freset}]{lightblack} Create new monitor
{freset}[{cyan}4{freset}]{lightblack} Delete monitor
	""")
	while True:
		try:
			option = int(input(blue + '>> ' + freset))
		except ValueError:
			continue
		else:
			if option in range(1,5):
				mainreq(option)
				break
			else:
				print(Fore.RED + 'Invalid selection! (1-4)' + freset)
				continue
main()