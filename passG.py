""" A program that generates Solid 16-digits passwords, and keep them safe in passwords.txt file in the chosen path"""

from random import choices, choice
import os
import logging
# FOR WRITING LOGS WHICH IS HELPFUL IN DEBUG
LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
# YOU CAN CHANGE THE LOG PATH HERE
LOG_PATH = os.getcwd() + "\\loggs.txt"
logging.basicConfig(filename = LOG_PATH,
					format=LOG_FORMAT,
					level=logging.DEBUG)

logger = logging.getLogger("Main")

class PassGenerator:
	"""Password Generating Section"""
	# YOU CAN FILTER WHICH CHARACTER SHOULD APPEAR IN YOUR PASSWORD HERE
	chars = ["1234567890", "qwertyuiopasdfghjklzxcvbnm", "!@#$%&"]

	def create_pass() -> str:

		password = ""
		for i in choices(PassGenerator.chars[1],k=7) : password += i 
		password = password[:3].upper()+ password[3:]
		for i in choices(PassGenerator.chars[0],k=5) : password += i 
		for i in choices(PassGenerator.chars[2],k=4) : password += i 

		# FOR MAKING ALL PASSWORD'S CHARACTERS COMPLETELY UNIQUE, YOU CAN COMMENT IT TILL THE LINE '37' IF YOU DON'T WANT IT
		password = set(password)
		_ = ""
		for i in password: _ += i
		password = _ 
		if ( 16 - len(set(password)) ) != 0 :
			list = PassGenerator.chars[0] + PassGenerator.chars[1] + PassGenerator.chars[2]
			while len(set(password)) != 16:
				l = choice(list)
				if l not in password.lower() : 
					password += l

		return password

class PassManager:
	"""Password Storing, deleting, manipulating Section """


	def add(prompt:str):
		"""Adding a password to passwords.txt"""
		with open(file_to_save, "a") as f:
			password = PassGenerator.create_pass()
			f.write(f"{prompt.strip()} : {password}\n")
			s = len(prompt) - 7
			space_a = 0 ; space_b = 0
			if s > 0 : space_a = s 
			elif s < 0 : space_b = abs(s)  
			print(f" Successfully added    profile{space_a *  ' '} : password\n")
			print(f"                       {prompt}{space_b * ' '} : {password}\n")
			logger.info("Password added")

	def delete(prompt:str):
		"""Deleting a password from passwords.txt"""
		with open(file_to_save, "r") as f:
			lines = f.readlines()
			with open(file_to_save, "w") as f:
				for line in lines:
					if prompt not in line:
						f.write(line+"\n")
		
		logger.info(f"{prompt} is removed successfully")
		print(f" {prompt} is removed successfully")
		
	def replace(prompt:str):
		"""Replacing a password in passwords.txt"""
		with open(file_to_save, "r") as f:
			lines = f.readlines()
		with open(file_to_save, "w") as f:
			for line in lines:
				if prompt.strip() == line.split(":")[0].strip():
					new_pass = PassGenerator.create_pass()
					line = line.split(":")[0] + ": " + new_pass
					logger.info(f"{line} replaced with new password {new_pass}")
				f.write(line+"\n") 
		print(" Successfully replaced with new password '{}'".format(new_pass))

	def reorder():
		"""Shape the appearance in passwords.txt """
		with open(file_to_save, "r") as f:
			lines = f.readlines()
			longest_len = 4
			for line in lines:
				profile_len = len(line.split(":")[0].strip())
				if profile_len > longest_len : longest_len = profile_len
		with open(file_to_save , "w") as f:
			space = " "
			for line in lines : 
				l = line.split(":")
				f.write(f"{l[0].strip()}{space * (longest_len - len(l[0].strip()))} :  {l[1].strip()}\n")
class Main:
	
	def main():
		print("\nCommands are 'show', 'delete all' and 'exit'.\n \
	   				show --> Shows all the passwords saved on password.txt \n \
	   				delete all --> Deletes all the passwords in passwords.txt \n \
					exit --> Exit the program \n \
	   				hint : strongly recommend to use a good and memorable or informative prompt \n \
					that will help you to know which password is for which later. \n \
					e.x of prompts : Yasin10ar@gmail.com , facebook.com , Crypto Wallet & ... ")

		while True:
			prompt = input("\nEnter a NAME to associate a password to it >> ")

			if prompt.lower() == "exit": 
					PassManager.reorder()
					exit()

			elif prompt.lower() == "show" :
				with open(file_to_save, "r") as f:
					lines = f.readlines()
					if len(lines) == 0 :
						print("The list is empty, You have no saved password.")
					else:
						print("Profile | Password")
						print("-"*50)
						for line in lines:
							print("\n"+line)
							print("*"*50)
						print("-"*50)
				continue

			elif len(prompt) < 4 :
						print(" If you want to generate a password, YOU MUST enter a word with 4 character or more")
						continue
			elif prompt.lower() == "delete":
				print(" If you want to delete a password, first type only it's profile(the name you associated your password with)\n \
	  				   then chose delete when it ask you delete or replace. \n \
	  				   If you want to delete all the passwords in passwords.txt, use 'delete all' command.")
				continue
			elif prompt.lower() == "delete all":
						with open(file_to_save,"r") as f:
							lines = f.readlines()
							if len(lines) == 0:
								print(" The file is already empty")
								continue
							else:
								response = input(" Are you sure you want to delete all your passwords? (y/n) : ")
								if response in ["Yes", "yes", "Y", "y"]:
									with open(file_to_save, "w") as f:
										f.write("")
										print(" The file is clear now and all the passwords are gone")
										logger.warning("'delete all' command have deleted all passwords")
								break

			with open(file_to_save, "r") as f:
				lines = f.readlines()
				profiles = [line.split(':')[0] for line in lines]
				flag = True				
				
				counter = 1
				for p in profiles:
					if prompt.strip() == p.strip():

						if counter > 1:
							option = input(f" for the {counter} time, {prompt} already exists, what do you want to do? (delete/replace) : ")
						else:
							option = input(f" {prompt} already exists, what do you want to do? (delete/replace) : ")
						
						if option.lower() == "delete":
							PassManager.delete(p)
							flag = False
							counter += 1
							
						elif option.lower() == "replace":
							PassManager.replace(p)
							flag = False
							counter += 1
							
						else:
							print( "Wrong input, options are 'delete' and 'replace'\n exiting ...")
							flag = False
			
			if flag :PassManager.add(prompt);break
			

if __name__ == "__main__":
	# THE PATH YOU WANT passwords.txt TO BE, MODIFY IT TO YOUR NEED
	file_to_save = os.getcwd() + "\\passwords.txt"
	try:
		# TO CHECK IF THE FILE IS CREATED
		with open(file_to_save, 'r'):
			pass
	except:
		# TO CREATE A FILE IF DOES NOT EXISTS 
		with open(file_to_save, 'w'):
			pass

	FLAG = "on"
	while len(FLAG) > 0:
		Main.main()
		PassManager.reorder()
		FLAG = input("\nType anything to add another one or press Enter to exit : ")