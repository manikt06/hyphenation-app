# Hyphenation App (CLI)

A small Python command-line tool that converts any text into a clean, lowercase, hyphenated or underscored string (similar to a URL slug).

It will:
- ask for a text input
- remove any characters that are not letters or spaces
- convert everything to lowercase
- ask whether to join words with `-` or `_`
- print the transformed result in the terminal

## Requirements

- Python 3.x installed on your system  
- PyCharm (optional, but this project is designed to be run from the PyCharm terminal)

## How to run (PyCharm terminal)

1. Open the project in PyCharm.
2. Create a file named `hyphenation-app.py` and paste your script into it.
3. Open the integrated terminal:
   - Press `Alt + F12` in PyCharm to open the terminal at the project root.
4. Run the script:

```bash
python hyphenation-app.py
```

(Use `python3` instead of `python` if your system requires it.)

## How it works (logic overview)

1. Read a line of text from the user using `input()`.
2. Build a “clean” string by keeping only:
   - alphabetic characters (`ch.isalpha()`)
   - spaces (`ch.isspace()`)
   - digits (`ch.isdigit()`)  
3. Convert the cleaned string to lowercase with `.lower()`.
4. Split into words using `.split()`.
5. Ask the user if they want:
   - `y` → join using `-`
   - `n` → join using `_`
6. Use `"-".join(words)` or `"_" .join(words)` to build the final string.

Example:

Input text:
```text
Wake Up Dead man! A Knives-Out Mystery trailer (2024)!!!
```

User chooses `y` → output:
```text
wake-up-dead-man-a-knives-out-mystery-trailer
```

## Running outside PyCharm

From a normal terminal, `cd` into the project folder and run:

```bash
python hyphenation-app.py
```

(Again, use `python3` if needed.)
