import sys
def newMemeber():
	user = input('Welcome to the National Meme Bank of United States, would you like to join? Y/N').lower()
	if(user is 'y'):
		user = 'n'
		account =input('What will your account name be?')
		while(user != 'y'):
			user = input('Just to make sure, your account name is ' + account + ' Y/N').lower()
			while(user == 'n'):
				account = input('What would your new account name be?')
		user = 'n'
		print('Awesome, you will be getting a new T-shirt in the mail, but before that happens what would you like your password to be?')
		password = input()
		while(user != 'y'):
			print('Just to clarify your password is ' + password + ' Y/N')
			user = input().lower()
			while(user == 'n'):
				password = input('What would you like your password to be?')	
		print('Your account is fully set up!')
		return account + ' ' + password
	else:
		return 'Thanks for your time!'
newMemeber()