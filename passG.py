from random import choices, choice

class PassGenerator:

	chars = ['1234567890', 'qwertyuiopasdfghjklzxcvbnm', '!@#$%&']

	def create_pass():

		password = ''
		for i in choices(PassGenerator.chars[1],k=3) : password += i ; password = password.title()
		for i in choices(PassGenerator.chars[0],k=3) : password += i 
		for i in choices(PassGenerator.chars[2],k=2) : password += i 

		password_list = list(password)
		password = ''

		while len(password) != 8:
			
			char = choice(password_list)
			if char not in password : password += char

		return password