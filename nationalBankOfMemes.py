
databaseOfMemeber = {}
def newMemeber():
	print('Welcome to the National Meme Bank of the United States, would you like to join? Y/N')
	user = input().lower()
	if(user == 'y'):
		user = 'n'
		print('What will your account name be?')
		account = input()
		while(user != 'y'):
			print('Just to make sure, your account name is ' + account + ' Y/N')
			user = input().lower()
			while(user == 'n'):
				print('What would your new account name be?')
				account = input()
				break
		user = 'n'
		print('Awesome, you will be getting a new T-shirt, but before that happens what would you like your password to be?')
		password = input()
		while(user != 'y'):
			print('Just to clarify your password is ' + password + ' Y/N')
			user = input().lower()
			while(user == 'n'):
				print('What would you like your password to be?')
				password = input()
				break
		print('Your account is fully set up!')
		databaseOfMemeber[account] = password
		return account + ' ' + password
	else:
		return 'Thanks for your time!'
def deposit():
	print('How many memes would you like to deposit today?')
	user = input()
	print('Ok, sounds good. Please choose the meme files name you would like to store.')
	filesToStore = input()
	print('It looks like '+ filesToStore+' are stored in the bank now. Have a good day!')
	return filesToStore
def withdrawal():
	print('How many memes would you like to withdraw today?')
	user = input()
	print('Ok, sounds good! Please choose the meme file names you would like to store.')
	user = 'n'
	filesToGetRidOf = ' '
	while(user == 'n'):
		filesToGetRidOf = input()
		print('Are you sure you want to delete '+ filesToGetRidOf + '?')
		user = input()
	print('Now deleting ' + filesToGetRidOf + '. Have a nice day!')
def signIn():
	print('Please sign in to the National Meme Bank Of the United States')
	account = input('User: ')
	password = input('Password: ')
	for key in databaseOfMemeber:
		if(account == key):
			for value in databaseOfMemeber:
				if(account == value):
					print('Login was a success! You may view your account now.')
					return True
	return False		
newMemeber()
signIn()
