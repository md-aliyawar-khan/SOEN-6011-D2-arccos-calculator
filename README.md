SOEN 6011 — Deliverable 2
F1: arccos(x) Calculator

**Student:** Mohammad Aliyawar Khan  
**Student ID:** 40309082  
**Course:** SOEN 6011  
**Semester:** Summer 2026  

## Overview

This project implements a graphical calculator for the inverse cosine function, arccos(x).

The application is developed in Python using Tkinter. The numerical value is calculated from scratch with a Taylor-series approximation. No built-in or library inverse-trigonometric functions are used.

The implementation uses:

arccos(x) = pi / 2 - arcsin(x)

The arcsin(x) value is calculated using a Taylor-series recurrence.

## Features

- Tkinter graphical user interface
- Valid input domain: -1 <= x <= 1
- Result displayed in radians
- Principal output range: 0 <= arccos(x) <= pi
- Input checks for blank, nonnumeric, NaN, infinity, and out-of-domain values
- Helpful error messages
- Exact handling for x = -1 and x = 1
- Taylor-series convergence limit and convergence-error handling
- Calculate, Clear, and Exit buttons
- Multiple calculations without restarting the application

## Requirements

- Python 3.11 or later
- Tkinter, included with standard Python installations
- No third-party packages are required

## Running the Program

Clone the repository:

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/SOEN-6011-D2-arccos-calculator.git
```

Open the project directory:

```bash
cd SOEN-6011-D2-arccos-calculator
```

Run the GUI:

```bash
python arccos_gui.py
```

## From-Scratch Implementation

The application does not use:

- `math.acos()`
- `math.asin()`
- `math.sin()`
- `math.cos()`
- NumPy, SciPy, SymPy, or another numerical library
- Built-in inverse-trigonometric functions
- `abs()` for Taylor-series convergence checking

The program uses `float()` only to convert text entered into the Tkinter input field into a numeric value. It is not used for the mathematical calculation.

## Test Cases

| Input | Expected behavior |
| --- | --- |
| `0.5` | Displays approximately `1.0471975512` radians |
| `0` | Displays approximately `1.5707963268` radians |
| `1` | Displays `0.0000000000` radians |
| `-1` | Displays approximately `3.1415926536` radians |
| `2` | Displays a domain error |
| `nan` | Displays a finite-number error |
| `inf` | Displays a finite-number error |
| `hello` | Displays a numeric-input error |
| Empty input | Displays an input-required error |

## Exception Handling

The application handles:

- `ValueError` for nonnumeric input
- `InputValidationError` for non-finite and out-of-domain input
- `ConvergenceError` when the Taylor Series reaches the maximum iteration limit

## Repository URL

<https://github.com/md-aliyawar-khan/SOEN-6011-D2-arccos-calculator>
