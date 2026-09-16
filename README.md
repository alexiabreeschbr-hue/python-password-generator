# PyPassword Generator

A secure CLI password generator built in Python that dynamically constructs randomized, custom-length passwords using standard library character sets and input validation.

## Features
* **Custom Character Composition:** Allows users to specify exact counts for letters, numbers, and symbols.
* **Built-in Validation:** Includes `try-except` exception handling to catch invalid non-numeric inputs without crashing.
* **Standard Library Security:** Utilizes `string.ascii_letters`, `string.punctuation`, and `string.digits` alongside `random.shuffle()` for strong randomness.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/alexiabreeschbr-hue/python-password-generator.git
