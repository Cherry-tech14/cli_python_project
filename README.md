# CLI Python Projects

## Project Overview

This repository contains two beginner-friendly Python command-line applications:

1. **CLI Calculator**
2. **CLI Expense Tracker**

These projects were developed to practise Python fundamentals, including functions, loops, conditional statements, lists, dictionaries, error handling, and user input validation.

Both applications run in the terminal.

## 1. CLI Calculator

The CLI Calculator performs basic arithmetic operations based on user input.

### Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Modulo (`%`)
- Menu-driven interaction
- Input validation
- Division-by-zero handling
- Option to quit the program

### How to Run

```bash
python3 calculator.py
```

Follow the instructions displayed in the terminal to select an operation and enter two numbers.

## 2. CLI Expense Tracker

The CLI Expense Tracker allows users to record expenses and calculate their total spending.

### Features

- Add an expense with a description and amount.
- View all recorded expenses.
- Calculate the total amount spent.
- Reject empty expense descriptions.
- Handle invalid numeric inputs.
- Reject zero and negative amounts.
- Exit the application.

### How to Run

```bash
python3 tracker.py
```

### Menu Options

| Option | Description |
|---|---|
| 1 | Add an expense |
| 2 | View recorded expenses |
| 3 | Calculate total spending |
| q | Quit the application |

### Example Output

```text
==CLI Expense Tracker==

1. Add expense
2. View expenses
3. Show total
q. Quit

Choose an option: 1
Enter Your description: Transport
Enter amount in Naira: 500
Expense added successfully
```

### Data Storage

The Expense Tracker uses a Python list containing dictionaries to store expenses temporarily.

Expenses remain available while the application is running.

**Note:** Expenses are not saved permanently. All recorded expenses are lost when the application closes.

## 3. Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

Both applications use Python's standard functionality and do not require installing third-party packages.

## 4. Project Structure

```text
cli-python-project/
├── calculator.py      # Performs arithmetic calculations
├── tracker.py         # Records and calculates expenses
└── README.md          # Project documentation
```

## 5. How to Get Started

### Prerequisites

Ensure Python 3 is installed.

Check your Python version:

```bash
python3 --version
```

### Running the Applications

Open a terminal inside the project directory.

To run the calculator:

```bash
python3 calculator.py
```

To run the expense tracker:

```bash
python3 tracker.py
```

## 6. Python Concepts Practised

The projects helped reinforce the following Python concepts:

- Variables and data types
- User input and output
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- Functions and return statements
- Lists and dictionaries
- Exception handling (`try`, `except`)
- Input validation
- String formatting
- Basic arithmetic operations

## 7. Future Improvements

Possible improvements include:

- Saving expenses permanently using JSON.
- Adding options to edit or delete expenses.
- Organizing expenses into categories.
- Generating monthly expense reports.
- Adding automated tests.

## 8. Conclusion

These projects demonstrate the practical application of Python fundamentals through two interactive command-line programs.

The CLI Calculator focuses on arithmetic operations and error handling, while the CLI Expense Tracker demonstrates data collection, temporary storage, iteration, and calculations.