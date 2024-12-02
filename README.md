# advent-of-code-2024

> [Advent of Code 2024](https://adventofcode.com/2024) in Python

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Install

Create a virtual environment:
```sh
python3 -m venv env
```

Then, activate it:
```sh
source env/bin/activate
```

Finally, install dependencies via:
```sh
pip install -r requirements.txt
```

## Develop

To launch a specific day, you can `cd` into it, then just launch it. 

Example with the first day (challenge 1/2):
```sh
cd day-1 && python3 main_1.py
```

## Test

If you want to verify your answer via the example given in Advent of Code, you can just run the tests via `pytest`: 
```sh
pytest
```