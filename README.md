# Hifu: Advanced Password Generator

Hifu is an advanced password generation tool designed to provide users with highly customizable and secure password options. It blends sophistication with flexibility, allowing users to craft passwords tailored to their specific needs, enhancing both security and usability in a user-friendly manner.

## Features

- Generate passwords with specific counts of digits, lowercase letters, uppercase letters, and special characters.
- Specify total length of the password, including optional prefixes and suffixes.
- Generate passwords using regex.
- Exclude certain characters from the password.
- Convert custom names to leet speak.
- Output passwords in plain text or JSON format.
- Evaluate and display password strength as a percentage.
- Includes the ability to check whether your current password has appeared in any known data breaches.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Kuraiyume/Hifu
    ```
2. Run the install.py:
    ```
    ./install.py
    ```
3. Run the Hifu by typing the command 'hifu':
    ```
    hifu -h
    ```

## Available Parameters

```
.___.__  .___ ._______.____
:   |  \ : __|:_ ____/|    |___
|   :   || : ||   _/  |    |   |
|   .   ||   ||   |   |    :   |
|___|   ||   ||_. |   |        |
    |___||___|  :/    |. _____/
                :      :/ Kura1yume
                       :v0.4

usage: Hifu [-h] [-n NUMBERS] [-l LOWERCASE] [-u UPPERCASE] [-s SPECIAL_CHARS] [-a AMOUNT] [-r REGEX] [-o OUTPUT_FILE] [-pfix PREFIX] [-sfix SUFFIX]
            [-t TOTAL_LENGTH] [-c CUSTOM] [-p PASSWORD] [--check-if-pwned] [--seed SEED] [--output-format {txt,json}] [--exclude-chars EXCLUDE_CHARS]

Advanced Password Generator that creates highly customizable and secure passwords tailored to your needs. Hifu allows you to specify complex options such
as password length, inclusion of special characters, numbers, uppercase and lowercase letters, and even custom patterns. It is designed to generate
passwords that are both strong and unique, providing enhanced security for your accounts. With the flexibility to configure multiple parameters, this
password generator ensures that you can meet specific requirements for different platforms, applications, or security standards.

options:
  -h, --help            show this help message and exit
  -n NUMBERS, --numbers NUMBERS
                        Number of digits in the password
  -l LOWERCASE, --lowercase LOWERCASE
                        Number of lowercase characters in the password
  -u UPPERCASE, --uppercase UPPERCASE
                        Number of uppercase characters in the password
  -s SPECIAL_CHARS, --special-chars SPECIAL_CHARS
                        Number of special characters in the password
  -a AMOUNT, --amount AMOUNT
                        Number of passwords to generate
  -r REGEX, --regex REGEX
                        Regex pattern for generating passwords
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        File to write the generated passwords to
  -pfix PREFIX, --prefix PREFIX
                        Prefix to add to each password
  -sfix SUFFIX, --suffix SUFFIX
                        Suffix to add to each password
  -t TOTAL_LENGTH, --total-length TOTAL_LENGTH
                        Total length of the password (including prefix and suffix) If 0, use specified counts
  -c CUSTOM, --custom CUSTOM
                        Custom name for the password with leet speak conversion
  -p PASSWORD, --password PASSWORD
                        Specify password for checking if the password is breached
  --check-if-pwned      Check if the password from '--password' is breached
  --seed SEED           Seed for randomization to allow reproducible results
  --output-format {txt,json}
                        Format of the output file (txt or json)
  --exclude-chars EXCLUDE_CHARS
                        Characters to exclude from the password
```
## Usage

1. Generate a Password with Specific Counts
   ```bash
   hifu -n 2 -l 4 -u 2 -s 2
   ```
   *This generates a password with 2 digits, 4 lowercase letters, 2 uppercase letters, and 2 special characters.*
   
2. Generate a Password with a Total Length
   ```bash
   hifu --total-length 12
   ```
   *This generates a password with a total length of 12 characters, including any specified prefixes and suffixes.*

3. Exclude Certain Characters
   ```bash
   hifu -n 3 -l 2 -u 4 -s 3 or --total-length 12 --exclude-chars "0OIl"
   ```
   *This generates a password excluding the characters 0, O, I, and l.*

4. Add Prefix and Suffix
   ```bash
   hifu -n 3 -l 2 -u 4 -s 3 or --total-length 12 --prefix "start-" --suffix "-end"
   ```
   *This generates a password with the specified prefix and suffix. (Note: Not all parameters are can be applied in regex option)*
5. Generate a Password with Regex
    ```bash
    hifu --regex "[a-z]{3}[A-Z]{2}[0-9]{4}" -a 5
    ```
    *This generates a password that match the provided regex pattern.*

6. Convert a Custom Name to Leet Speak
   ```bash
   hifu --custom "example"
   ```
   *This generates a password based on the leet speak conversion of the custom name "example". (Note: All parameters cannot be applied in customized password)*

7. Output to a file
   ```bash
   hifu -n 3 -l 2 -u 4 -s 3 or --total-length 12 --output-file passwords --output-format txt
   ```
   *This generates passwords and saves them to passwords.txt in plain text format. You can also use json format.*

8. Check password if existing in breaches
   ```bash
   python3 hifu.py -p bash --check-if-pwned
   ```
   
## License

- This project is licensed under the MIT License

## Author

- Kura1yume (A1SBERG)
