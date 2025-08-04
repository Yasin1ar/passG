import string
from random import choice, shuffle

PASSWORD_LENGTH: int = 16
MIN_PASSWORD_LENGTH: int = 8
SPECIAL_CHARS: string = "!@#$%^&*()-_+="


def generate_password(length: int = PASSWORD_LENGTH) -> str:
	"""
	Generates a secure and random password of the specified length.

	The password is guaranteed to include at least one lowercase letter, one uppercase letter,
	one digit, and one special character. The remaining characters are randomly selected
	from a pool of all allowed characters (letters, digits, and special characters).

	Args:
		length (int): The desired length of the password. Defaults to 16 characters.
		Must be at least 8 characters to ensure password strength.

	Returns:
		str: A randomly generated password string.

	Raises:
		ValueError: If the specified length is less than 8 characters.

	Example:
		>>> generate_password()
		'aB3$fG7!kL9@mN2&'

		>>> generate_password(20)
		'xY4@zQ8!pL3$wR9%vT2*'

	Notes:
		- The password length must be at least 8 characters to meet minimum security requirements.
		- The password is shuffled to ensure randomness and unpredictability.
	"""
	if length < MIN_PASSWORD_LENGTH:
		raise ValueError(
			f"Password length should be at least {MIN_PASSWORD_LENGTH} characters."
		)

	# Ensure password has at least one character from each required category
	password = [
		choice(string.ascii_lowercase),
		choice(string.ascii_uppercase),
		choice(string.digits),
		choice(SPECIAL_CHARS),
	]

	# Create character pool for remaining positions
	all_characters = list(string.ascii_letters + string.digits + SPECIAL_CHARS)

	# Fill the rest with random chars
	password.extend(choice(all_characters) for _ in range(length - len(password)))

	# Final shuffle for randomization
	shuffle(password)

	return "".join(password)
