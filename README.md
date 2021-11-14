# Word count
It`s a program for counting words that includes specific letters.

Implemented following features:
+ possibility to read words from .txt file
+ possibility to add word to vocabulary
+ possibility to display words in vocabulary with pagination
+ posibility to find exact number of words that contain provided letters
+ posibility to display search history in table format
+ posibility to sort words in vocabulary
+ posibility to clear vocabulary and search history
+ posibility to write your vocabulary in .txt file

Also I implemented unittests for Vocabulary class.

## Installation
I use Python 3.8.5. For check your python version:
```bash
python --version
```  
The first thing to do is to clone the repository:  
```bash
git clone https://github.com/ValeriaMahdenko/Word-Count.git
cd Word-Count
```
Create a virtual environment to install dependencies in and activate it:
```bash
python3.8 -m venv .env
source .env/bin/activate
```
Then install the dependencies:  
```bash
pip install -r requirements.txt
```

## Usage
Run the program:
```bash
python3 -m Main
```
Run the tests:
```bash
python3 Tests.py
```
Check code quality by flake8:
```
flake8
```
