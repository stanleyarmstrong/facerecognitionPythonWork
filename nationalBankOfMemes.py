import tkinter as tk
from tkinter import filedialog

import sqlite3

connection = sqlite3.connect('memeBase.db')

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
		return account + ' ' + password
	else:
		return 'Thanks for your time!'
def deposit():
	print('How many memes would you like to deposit today?')
	user = input()
	print('Ok, sounds good. Please choose the meme files names you would like to store.')
	filesToStore = input()
	print('It looks like they are stored in the bank now. Have a good day!')
	return filesToStore
print(deposit())
	
	
	
	
	