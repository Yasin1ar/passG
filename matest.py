from random import choices, choice

class PassGenerator:

	chars = ['1234567890', 'qwertyuiopasdfghjklzxcvbnm', '!@#$%&']

	def create_pass():

		password = ''
		for i in choices(PassGenerator.chars[1],k=3) : password += i ; password = password.title()
		for i in choices(PassGenerator.chars[0],k=3) : password += i 
		for i in choices(PassGenerator.chars[2],k=2) : password += i 

		password = set(password)
		temporary_variable = ''
		for i in password: temporary_variable += i
		password = temporary_variable 

		if ( 8 - len(set(password)) ) != 0 :
			list = PassGenerator.chars[0] + PassGenerator.chars[1]
			while len(set(password)) != 8:
				l = choice(list)
				if l not in password.lower() : 
					password += l

		return password