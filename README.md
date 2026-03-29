# Password Generator

A simple yet powerful command-line Password Generator built with Python. This project was created as a capstone project to demonstrate core Python programming concepts including functions, loops, input validation, and file handling.


## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [What I Learned](#what-i-learned)
- [Future Improvements](#future-improvements)


## About the Project

This is a terminal-based Password Generator that allows users to create strong, customizable passwords based on their preferences. The user can choose the password length, include/exclude uppercase letters, numbers, and special characters, check password strength, and optionally save the generated password to a file.


## Features

-  Generate random passwords with customizable options
-  Choose password length
-  Include/exclude uppercase letters, numbers, and special characters
-  Guarantees at least one character of each selected type
-  Password strength meter (Weak  / Medium  / Strong )
-  Save passwords to a file with a custom label
-  Input validation to handle incorrect entries
-  Option to generate multiple passwords in one session


## Getting Started

### Prerequisites

- Python 3.x installed on your system
- No external libraries required — uses only built-in Python modules (`string`, `random`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/parthkaushik100507/Password-Generator.git
   ```

2. Navigate to the project folder:
   ```bash
   cd Password-Generator
   ```

3. Run the program:
   ```bash
   python main.py
   ```


## Usage

When you run the program, follow the prompts:

```
Enter the length of the password: 12
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y
```

The program will generate a password, show its strength, and ask if you want to save it.


## Sample Output

```
 Password Generator
------------------------------
Enter the length of the password: 12
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

 Generated Password : aB3$kR9!mZqW
 Password Strength  : Strong 

Do you want to save this password? (y/n): y
Enter a label for this password (e.g. Gmail): Instagram
 Password saved to saved_passwords.txt

Generate another password? (y/n): n

 Goodbye! Stay secure.
```


## Project Structure

```
password-generator/
│
├── main.py                # Main Python script
├── saved_passwords.txt    # Auto-created when passwords are saved
└── README.md              # Project documentation
```


## What I Learned

- Using Python's built-in `string` and `random` modules
- Writing reusable functions with parameters
- Input validation using `try/except` and `while` loops
- File handling with `open()` in append mode
- Building a menu-driven terminal application


## Future Improvements

- [ ] Add a graphical user interface (GUI) using `tkinter`
- [ ] Encrypt saved passwords for security
- [ ] Add a feature to copy password directly to clipboard using `pyperclip`
- [ ] Allow users to view and delete saved passwords
- [ ] Add support for excluding ambiguous characters (e.g. `0`, `O`, `l`, `1`)


## Author

**Parth Kaushik**  
GitHub: [@parthkaushik100507](https://github.com/parthkaushik100507)


## License

This project is open source and available under the [MIT License](LICENSE).
