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

class PassManager:

	path = '/home/Yasin10ar/Documents/MyDucs/PassG/passwords.txt'

	def add():
		with open(PassManager.path, 'a') as f:
			f.write(f"{profile} : {PassGenerator.create_pass()}\n")


	def delete():
		with open(PassManager.path, "w") as f:
			lines = f.readlines()
			for line in lines:
				if profile not in line:
					f.write(line)

	def replace():
		with open(PassManager.path, "w") as f:
			lines = f.readlines()
			for line in lines:
				if profile in line:
					print(line)

	def main():
		with open(PassManager.path, 'r') as f:
			lines = f.readlines()
			print(lines)
			if profile in lines:
				option = input(f"{profile} already exist, what do you want to do? (delete/replace) : ")

				if option == 'delete':
					PassManager.delete()
				elif option == 'replace':
					pass
				else:
					print("wrong input, options are 'delete' and 'replace'/n exiting")

			else:
				PassManager.add()


if __name__ == "__main__":
	
	profile =input('PassG > ')
	PassManager.main()
	exit()