import sys
def newMemeber():
	print('Welcome to the National Meme Bank of United States, would you like to join? Y/N')
	user = raw_input().lower()
	if(user is 'y'):
		user = 'n'
		print('What will your account name be?')
		account = raw_input()
		while(user != 'y'):
			print('Just to make sure, your account name is ' + account + ' Y/N')
			user = raw_input().lower() 
		user = 'n'
		print('Awesome, you will be getting a new T-shirt in the mail, but before that happens what would you like your password to be?')
		password = raw_input()
		while(user != 'y'):
			print('Just to clarify your password is ' + password + ' Y/N')
			user = raw_input().lower()
		print('Your account is fully set up!')
	else:
		return 'Thanks for your time!'
print(newMemeber())