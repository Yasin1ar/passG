# Password Manager

A simple command-line-based password manager that generates strong, unique passwords and stores them securely in a text file. The password manager allows users to add, delete, replace, and display stored passwords.

## Features
- **Strong Password Generation**: Generates 16-character long passwords using a mix of uppercase letters, lowercase letters, numbers, and special characters.
- **Password Management**: Allows you to add, delete, and replace passwords associated with a specific prompt.
- **File-Based Storage**: Saves passwords to a file (`passwords.txt`), allowing for easy persistence and retrieval.
- **Logging**: Logs important actions (adding, deleting, replacing passwords) in `passG.log` for easier tracking.

## Requirements
- Python 3.6 or higher

## Installation

1. Clone this repository or download the source files.
   ```bash
   git clone https://github.com/Yasin1ar/passG
   ```

2. Navigate to the project directory:
   ```bash
   cd passG
   ```

3. Ensure that you have Python 3.6+ installed. You can check your Python version by running:
   ```bash
   python --version
   ```

(There are no external dependencies for this project, so no additional packages are required.)

## Usage

To run the password manager, execute the following command:

```bash
python passG.py
```

### Available Commands

Once the program is running, you can use the following commands:

1. **Add Password**: 
   ```bash
   add [prompt]
   ```
   Adds a new password associated with a given prompt (e.g., `add gmail.com`).

2. **Delete Password**: 
   ```bash
   delete [prompt]
   ```
   Deletes the password associated with the given prompt (e.g., `delete gmail.com`).

3. **Replace Password**: 
   ```bash
   replace [prompt]
   ```
   Replaces the existing password for the given prompt with a new one (e.g., `replace gmail.com`).

4. **Show Passwords**:
   ```bash
   show
   ```
   Displays all saved passwords.

5. **Delete all passwords**:
   ```bash
   delete all
   ```
   Deletes all saved passwords.
6. **Exit**:
   ```bash
   exit
   ```
   Exits the password manager program.

### Example

```bash
> add facebook.com
Password for 'facebook.com' has been added successfully.

> show
Saved Passwords:
----------------------------
facebook.com: A1!bC2dE3@FgH4

> replace facebook.com
Password for 'facebook.com' has been replaced successfully.

> delete facebook.com
Password for 'facebook.com' has been deleted successfully.
```

## File Structure

- **passG.py**: Main program file that contains the logic for password generation and management.
- **passwords.txt**: File where all generated passwords are stored (created automatically if it doesn't exist).
- **passG.log**: Log file where all actions (adding, deleting, replacing) are logged.

## Logging

The application logs all significant events to a file (`passG.log`). Each time a password is added, deleted, or replaced, an entry is made in this log file. This helps track important operations and debug any issues.

## Security Considerations

- **Plain-text storage**: Passwords are stored in plain text in `passwords.txt`. For enhanced security, consider adding encryption for password storage.
- **Local-only application**: This password manager is intended for local use. If you plan to use it in a more sensitive environment, consider additional security layers (encryption, password hashing, etc.).

## Future Enhancements

- **Encryption**: Encrypt passwords before storing them in the file for better security.
- **Password Expiry**: Implement password expiry and notify users when a password needs to be updated.
- **Search Functionality**: Add the ability to search for specific passwords by prompt.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.