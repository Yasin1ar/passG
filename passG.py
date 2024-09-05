import os
import logging
from random import choices, choice, randint
from typing import Final

# Constants
LOG_FORMAT: Final[str] = "%(levelname)s %(asctime)s %(message)s"
LOGS_FILE: Final[str] = "logs.txt"
PASSWORD_FILE: Final[str] = "passwords.txt"

LOG_PATH: Final[str] = os.path.join(os.getcwd(), LOGS_FILE)
FILE_TO_SAVE: Final[str] = os.path.join(os.getcwd(), PASSWORD_FILE)

logging.basicConfig(filename=LOG_PATH, format=LOG_FORMAT, level=logging.DEBUG)
logger = logging.getLogger("PasswordManager")


class PassGenerator:
    """Class responsible for generating passwords."""

    # Character pools: numbers, lowercase letters, special characters
    chars: list[str] = ["1234567890", "abcdefghijklmnopqrstuvwxyz", "!@#$%&"]

    @staticmethod
    def unique_password(password: str) -> str:
        """
        Generate a unique 16-character password.

        Ensures no repeating characters by adding random choices until
        it meets the required length.
        """
        unique_password = "".join(set(password))
        while len(unique_password) < 16:
            char = choice(PassGenerator.chars[randint(0, 2)])
            if char not in unique_password:
                unique_password += char
        return unique_password

    @staticmethod
    def create_pass(unique: bool = True) -> str:
        """
        Create a 16-character password with a mix of numbers, letters, and special characters.
        If unique is True, ensures no repeating characters.
        """
        password = ''.join(choices(PassGenerator.chars[1], k=7)).capitalize()  # Letters
        password += ''.join(choices(PassGenerator.chars[0], k=5))  # Numbers
        password += ''.join(choices(PassGenerator.chars[2], k=4))  # Special characters

        return PassGenerator.unique_password(password) if unique else password


class PassManager:
    """Class responsible for password management actions (add, delete, replace)."""

    @staticmethod
    def add(prompt: str) -> None:
        """
        Add a generated password to the passwords.txt file associated with a prompt.
        """
        password = PassGenerator.create_pass()
        with open(FILE_TO_SAVE, "a") as f:
            f.write(f"{prompt.strip()} : {password}\n")

        print(f"Successfully added {prompt}: {password}")
        logger.info("Password added for %s", prompt)

    @staticmethod
    def delete(prompt: str) -> None:
        """
        Delete a password associated with a specific prompt from the passwords.txt file.
        """
        with open(FILE_TO_SAVE, "r") as f:
            lines = f.readlines()

        with open(FILE_TO_SAVE, "w") as f:
            for line in lines:
                if prompt not in line:
                    f.write(line)

        logger.info(f"Deleted password for {prompt}")
        print(f"{prompt} is successfully removed.")

    @staticmethod
    def replace(prompt: str) -> None:
        """
        Replace a password associated with a specific prompt in the passwords.txt file.
        """
        new_pass = PassGenerator.create_pass()
        with open(FILE_TO_SAVE, "r") as f:
            lines = f.readlines()

        with open(FILE_TO_SAVE, "w") as f:
            for line in lines:
                if prompt.strip() == line.split(":")[0].strip():
                    line = f"{prompt} : {new_pass}\n"
                    logger.info(f"Replaced password for {prompt} with {new_pass}")
                f.write(line)

        print(f"Password for {prompt} successfully replaced with new password: {new_pass}")

    @staticmethod
    def reorder() -> None:
        """
        Align the entries in passwords.txt for better readability.
        """
        with open(FILE_TO_SAVE, "r") as f:
            lines = f.readlines()

        longest_prompt_len = max(len(line.split(":")[0].strip()) for line in lines)

        with open(FILE_TO_SAVE, "w") as f:
            for line in lines:
                prompt, password = line.split(":")
                f.write(f"{prompt.strip().ljust(longest_prompt_len)} : {password.strip()}\n")


class Main:
    @staticmethod
    def main():
        print("""
        Commands: 
        - show: Shows all saved passwords
        - delete all: Deletes all saved passwords
        - exit: Exit the program
        """)

        while True:
            prompt = input("Enter a NAME to associate a password or a command: ").strip().lower()

            if prompt == "exit":
                PassManager.reorder()
                break
            elif prompt == "show":
                Main.show_passwords()
            elif prompt == "delete all":
                Main.delete_all_passwords()
            elif len(prompt) >= 4:
                Main.manage_prompt(prompt)
            else:
                print("Please enter a name with 4 or more characters.")

    @staticmethod
    def show_passwords() -> None:
        """Displays all stored passwords."""
        try:
            with open(FILE_TO_SAVE, "r") as f:
                lines = f.readlines()
                if lines:
                    print("Profile | Password\n" + "-" * 50)
                    for line in lines:
                        print(line.strip())
                    print("-" * 50)
                else:
                    print("No saved passwords.")
        except FileNotFoundError:
            print("No passwords file found.")

    @staticmethod
    def delete_all_passwords() -> None:
        """Delete all passwords after confirmation."""
        response = input("Are you sure you want to delete all passwords? (y/n): ").strip().lower()
        if response in ["y", "yes"]:
            with open(FILE_TO_SAVE, "w") as f:
                f.write("")
            print("All passwords deleted.")
            logger.warning("Deleted all passwords.")

    @staticmethod
    def manage_prompt(prompt: str) -> None:
        """Manage existing prompts (add, delete, replace)."""
        with open(FILE_TO_SAVE, "r") as f:
            profiles = [line.split(":")[0].strip() for line in f.readlines()]

        if prompt in profiles:
            option = input(f"{prompt} already exists. What do you want to do? (delete/replace): ").strip().lower()
            if option == "delete":
                PassManager.delete(prompt)
            elif option == "replace":
                PassManager.replace(prompt)
            else:
                print("Invalid option. Options are 'delete' or 'replace'.")
        else:
            PassManager.add(prompt)


if __name__ == "__main__":
    # Ensure passwords.txt exists
    if not os.path.exists(FILE_TO_SAVE):
        open(FILE_TO_SAVE, "w").close()

    # Start the main loop
    while True:
        Main.main()
        if input("\nPress Enter to exit or type anything to continue: ").strip() == "":
            break
