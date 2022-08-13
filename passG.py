""" A program that generates Solid 8-digits passwords, and keep them safe in .txt file in the chosen folder """

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

	file = "C:\\Users\\yasin\\Documents\\MyDucs\\Important\\passwords\\Passwords.txt"

	def add():
		with open(PassManager.file, 'a') as f:
			f.write(f"{profile} : {PassGenerator.create_pass()}\n")


	def delete():
		with open(PassManager.file, "w") as f:
			lines = f.readlines()
			for line in lines:
				if profile not in line:
					f.write(line)

	def replace():
		with open(PassManager.file, "w") as f:
			lines = f.readlines()
			for line in lines:
				if profile in line:
					print(line)

class Main:

	def main():
		with open(PassManager.file, 'r') as f:
			lines = f.readlines()
			profile = 'read'
			while profile == "read" or len(profile) < 4:
    			profile = input(">> ")
    			if profile == "read":
        			list=[]        
        			for i in lines:
            			l = i.split(':')
            			line=f"{l[0].strip()} : {l[1][0:-1]}"
            			list.append(line)
	


if __name__ == "__main__":
	Main.main()
	exit()