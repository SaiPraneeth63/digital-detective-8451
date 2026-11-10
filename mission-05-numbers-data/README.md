# Mission 5 - Numbers and data

## 1. Task/objective
Convert decimal, binary, and hexadecimal values manually, verify them using Python, build a working number converter program (number_converter.py), and explain text-encoding standards.

## 2. Work completed
- Performed manual conversions for decimal, binary, and hexadecimal values showing step-by-step logic.
- Verified all calculations in the Python interactive terminal using built-in conversion functions.
- Developed, tested, and documented number_converter.py using multiple positive test values.
- Answered questions regarding ASCII decimal codes and the necessity of character encoding standards like UTF-8.

## 3. Commands / tools used
- Python 3 (bin(), hex(), int()): Built-in functions used for number base conversions.
- Python script (number_converter.py): Custom script built to automate decimal-to-binary/hex conversions.
- Terminal: Used for executing interactive Python sessions and script tests .
- Visual Studio Code: Used as the text editor.

## 4. My understanding
Computers store and process all data using binary bits (zeros and ones) organized into bytes. Binary (base-2) and hexadecimal (base-16) systems provide compact ways to read and interpret machine-level memory addresses and values. Character encoding standards map human-readable text characters to specific numeric byte codes so text displays accurately across systems.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- mission-05-numbers-data/number_converter.py

### Task 5.1 & 5.2: Manual Conversions and Python Verification
| Question / Conversion | Manual Working / Answer | Python Verification Result | Matches? |
| :--- | :--- | :--- | :--- |
| Decimal 13 to binary | Divided by 2 successively: 13/2 = 6 R 1, 6/2 = 3 R 0, 3/2 = 1 R 1, 1/2 = 0 R 1, resulting in 1101 | bin(13) equals '0b1101' | Yes |
| Decimal 25 to binary | Divided by 2 successively: 25/2 = 12 R 1, 12/2 = 6 R 0, etc., resulting in 11001 | bin(25) equals '0b11001' | Yes |
| Binary 1010 to decimal | Calculated position values: (1 x 8) + (0 x 4) + (1 x 2) + (0 x 1) = 8 + 2 = 10 | int('1010', 2) equals 10 | Yes |
| Binary 1101 to decimal | Calculated position values: (1 x 8) + (1 x 4) + (0 x 2) + (1 x 1) = 8 + 4 + 1 = 13 | int('1101', 2) equals 13 | Yes |
| Hexadecimal A to decimal | Hexadecimal A equals 10 in decimal | int('A', 16) equals 10 | Yes |
| Hexadecimal 1F to decimal | Calculated position values: (1 x 16) + (15 x 1) = 16 + 15 = 31 | int('1F', 16) equals 31 | Yes |
| Binary 1111 to hexadecimal | Grouped 4 bits: 1111 in binary equals 15 in decimal, which is F in hex | hex(15) equals '0xf' | Yes |

### Task 5.3: Number Converter Test Runs
| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| 10 | 0b1010 | 0xa |
| 25 | 0b11001 | 0x19 |
| 100 | 0b1100100 | 0x64 |

### Task 5.4: Text Encoding Answers
- ASCII decimal codes: Uppercase letter A is 65 (Hex 41), and lowercase letter a is 97 (Hex 61).
- Why encoding is needed: Computers only recognize numeric bit states. Encoding standards provide a universal lookup table mapping characters to numbers so text can be accurately transmitted and displayed.
- Non-ASCII character example: Emojis or accented letters (like é) require extended encodings like UTF-8 because basic ASCII only supports 128 standard English characters.

## 8. Commit details
- Commit message: "Build number converter and practise data representation"
- Pushed successfully to GitHub.