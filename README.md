<div align="center">

# 🐍 Python Fundamentals

### Learning Python step by step, from first `print()` to OOP, NumPy and charts

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Arrays-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-11557C?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen?style=for-the-badge)

</div>

---

## 📖 About

This repository is my learning journal. Every program here is a small, hands-on practice of one Python concept. The goal is to build a strong foundation in programming and problem-solving, one concept at a time.

---

## 🗺️ What I Have Practiced

### 🔤 1. Input, Output and Variables

| Concept | What it does |
| --- | --- |
| `input()` | Takes text from the user |
| `int()` / `float()` | Converts input into numbers |
| `print()` with `sep` and `end` | Controls spacing and line endings of output |
| f-strings | Puts variables directly inside text, like `f"Hello {name}"` |

### 🔀 2. Conditional Statements

| Concept | What it does |
| --- | --- |
| `if` / `elif` / `else` | Runs different code for different conditions |
| `and` / `or` | Combines multiple conditions |
| Comparison operators | Checks values with `==`, `>=`, `<`, and chained ranges like `0 <= x < 50` |

Used to build: grade evaluator, traffic light, ticket pricing, vowel/consonant checker.

### 🔁 3. Loops

| Concept | What it does |
| --- | --- |
| `for` loop with `range()` | Repeats a task a fixed number of times |
| `while` loop | Repeats until a condition becomes false |
| `while True` + `break` | Runs forever until we stop it |
| Flag variable | A True/False switch that controls when a loop ends |

### 📋 4. Lists

| Method | What it does |
| --- | --- |
| `append()` | Adds an item at the end |
| `pop()` | Removes and returns the last item |
| `remove()` | Removes the first matching value |
| `sort()` / `reverse()` | Orders or flips the list in place |
| `index()` / `count()` | Finds the position of an item or how many times it appears |
| Slicing `[a:b]` | Takes a part of a list |

### 🗂️ 5. Dictionaries

| Concept | What it does |
| --- | --- |
| Key-value pairs | Stores related data under a name |
| `.items()` / `.keys()` / `.values()` | Loops through pairs, keys only, or values only |
| `sorted()` | Sorts keys without changing the original |
| List of dictionaries | Stores many records of the same shape |
| Dictionary inside a dictionary | Stores detailed info for each user |
| List inside a dictionary | Stores multiple values under one key |

### 🔡 6. Strings

| Method / Concept | What it does |
| --- | --- |
| Indexing and slicing | Picks characters, like `s[0]`, `s[-1]`, `s[2:5]` |
| `[::-1]` | Reverses a string |
| `lower()` / `upper()` / `title()` | Changes letter case |
| `strip()` | Removes extra spaces |
| `replace()` | Swaps one word for another |
| `split()` | Breaks a sentence into words |
| `in` operator | Checks if a piece of text exists inside another |
| `+` and `*` | Joins strings or repeats them |
| `encode()` / `decode()` | Converts text to bytes and back |
| Immutability | Strings can't be changed in place, so we build a new one |

### ⚙️ 7. Functions

| Concept | What it does |
| --- | --- |
| `def` and `return` | Creates reusable code that gives back a result |
| Parameters and arguments | Sends data into a function |
| Default arguments | Uses a fallback value when none is given |
| Keyword arguments | Passes values by name, in any order |
| `*args` | Accepts any number of positional values |
| `**kwargs` | Accepts any number of named values |
| Returning multiple values | Sends back a tuple |
| Passing a function as an argument | Treats functions like data |
| Docstrings and comments | Document what the code does |
| Generators with `yield` | Produce values one at a time, even endlessly, with `next()` |

### 🏗️ 8. Object-Oriented Programming

| Concept | What it does |
| --- | --- |
| `class` and objects | A blueprint and the things made from it |
| `__init__()` | Constructor that sets up each new object |
| Instance vs class attributes | Data unique to an object vs data shared by all |
| Methods | Functions that belong to a class |
| Inheritance | A child class reuses a parent class |
| Encapsulation | Hides data with private `__variables` and uses getters and setters |
| Abstraction | Uses `ABC` and `@abstractmethod` to force a structure on child classes |
| Polymorphism | Same method name, different behavior in different classes |
| `@staticmethod` | A method that doesn't need an object |
| Operator overloading | Defines how `+` works for our own objects with `__add__()` |
| `__str__()` | Controls how an object prints |

### 🔢 9. NumPy

| Method | What it does |
| --- | --- |
| `np.array()` | Creates an array from a list (1D, 2D, 3D, or `ndmin`) |
| `.shape` / `.ndim` / `.size` / `.dtype` | Shows the array's shape, dimensions, element count, and type |
| `np.zeros()` / `np.ones()` / `np.empty()` | Creates arrays of zeros, ones, or unfilled values |
| `np.full()` | Fills an array with any value |
| `np.zeros_like()` / `np.ones_like()` | Copies the shape of another array |
| `np.arange()` | Like `range()`, but returns an array |
| `np.linspace()` / `np.logspace()` | Creates evenly spaced numbers (linear or log scale) |
| `np.eye()` / `np.identity()` / `np.diag()` | Creates identity and diagonal matrices |
| `np.random.rand()` / `randint()` / `randn()` | Creates random numbers, with `seed()` to repeat them |
| `.reshape()` / `.flatten()` | Changes the shape or turns the array back into 1D |
| `np.tile()` / `np.repeat()` | Repeats the whole array or each element |
| Vectorized math | Adds, multiplies or sums every element without a loop |
| `timeit` | Measures how fast a piece of code runs |

### 📊 10. Data and Visualization

| Library / Method | What it does |
| --- | --- |
| `pandas.DataFrame()` | Builds a table from a dictionary |
| `to_csv()` / `read_csv()` | Saves a table to CSV and loads it back |
| `csv.reader()` | Reads a CSV file row by row and searches it |
| `plt.plot()` | Draws a line graph |
| `plt.bar()` | Draws a bar chart |
| Labels, title, legend, grid | Make a chart readable |
| 3D plot (`projection="3d"`) | Draws a curve in 3D space using `sin`, `cos` and `exp` |

### 🧠 11. Problem Solving

- Swapping two values in three ways: temporary variable, arithmetic, and bitwise XOR
- Generating prime numbers
- Removing punctuation from text
- Removing every copy of an item from a list
- Simple interest and temperature conversion
- A typing-effect animation using `time.sleep()` and `sys.stdout`

---

## 🛠️ Technologies Used

- **Python 3**
- **NumPy** for arrays
- **Pandas** for tables and CSV
- **Matplotlib** for charts

Install the libraries with:

```bash
pip install numpy pandas matplotlib
```

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/AnubhavSinghZ/python_fundamental.git

# 2. Go into the folder
cd python_fundamental

# 3. Run any program
python filename.py
```

---

## 🎯 Goal

To move from writing simple scripts to building real projects in **Python**, **Data Analysis** and **AI Development**.

---

## 👨‍💻 Author

**Anubhav Singh**
Computer Science Student | Learning Python and AI Development

⭐ If you find this repository helpful, consider giving it a star!
