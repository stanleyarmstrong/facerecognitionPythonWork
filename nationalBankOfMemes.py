import sys
import sqlite3
connection = sqlite3.connect('memeBase.db')

def newMemeber():
	user = input('Welcome to the National Meme Bank of the United States, would you like to join? Y/N').lower()
	if(user == 'y'):
		user = 'n'
		account =input('What will your account name be?')
		while(user != 'y'):
			user = input('Just to make sure, your account name is ' + account + ' Y/N').lower()
			while(user == 'n'):
				account = input('What would your new account name be?')
				break
		user = 'n' 
		password = input('Awesome, you will be getting a new T-shirt in the mail, but before that happens what would you like your password to be?')
		while(user != 'y'):
			user = input('Just to clarify your password is ' + password + ' Y/N').lower()
			while(user == 'n'):
				password = input('What would you like your password to be?')
				break
		print('Your account is fully set up!')
		return account + ' ' + password
	else:
		return 'Thanks for your time!'


