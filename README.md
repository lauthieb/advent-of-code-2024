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
cd day_1 && python3 main_day_1_1.py
```

## Test

If you want to verify your answer via the example given in Advent of Code, you can just run the tests via `pytest`: 
```sh
pytest
```

## Execute all scripts

Go to the root folder, then launch:
```sh
python3 execute_all_scripts.py
```

## Start a new day challenge

Go to the root folder, then launch:
```sh
python3 create_day_structure.py
```

Then, for example you enter `3` when prompted, the script will generate the following structure:

```
day_3/
├── input.txt
├── main_day_3_1.py
├── main_day_3_2.py
├── test_day_3_1.py
└── test_day_3_2.py
```

And, here we go!

## License

    MIT License

    Copyright (c) 2024 Laurent Thiebault

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.