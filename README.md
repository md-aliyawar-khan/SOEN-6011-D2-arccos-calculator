# SOEN 6011 — Deliverable 2
## F1: arccos(x) Calculator

**Student:** Mohammad Aliyawar Khan  
**Student ID:** 40309082  
**Course:** SOEN 6011  
**Semester:** Summer 2026  

## Overview

This repository contains a graphical calculator for the inverse cosine function,
$\arccos(x)$.

The application is implemented in Python using Tkinter. It calculates the
numerical result from scratch using a Taylor-series recurrence for
$\arcsin(x)$, together with range reduction near the endpoints of the valid
domain.

The application does not use built-in or library inverse-trigonometric
functions in its numerical calculation.

## Numerical Method

The principal result is in radians:

$$
0 \leq \arccos(x) \leq \pi
$$

For inputs close to $x = 1$ or $x = -1$, directly evaluating the Taylor series
for $\arcsin(x)$ converges slowly. The implementation therefore uses range
reduction.

For $x \geq 0$:

$$
\arccos(x) =
2\arcsin\left(\sqrt{\frac{1-x}{2}}\right)
$$

For $x < 0$:

$$
\arccos(x) = \pi - \arccos(-x)
$$

The program calculates:

- $\arcsin(x)$ using a Taylor-series recurrence
- $\sqrt{x}$ using Newton's method
- $\arccos(x)$ using the above range-reduction identities

This approach improves convergence for valid inputs near the domain endpoints.

## Features

- Tkinter graphical user interface
- Valid input domain: $-1 \leq x \leq 1$
- Result displayed in radians
- Principal output range: $0 \leq \arccos(x) \leq \pi$
- Input validation for blank, nonnumeric, non-finite, and out-of-domain values
- Helpful error messages with recovery through the GUI
- Exact endpoint handling for $x = -1$ and $x = 1$
- Taylor-series tolerance and maximum-iteration convergence handling
- Newton-method tolerance and maximum-iteration handling for square-root calculation
- Calculate, Clear, and Exit buttons
- Multiple calculations without restarting the application
- Enter key support for calculation

## Requirements

- Python 3.x
- Tkinter, typically included with standard Python installations
- No third-party packages are required

## Running the Program

Clone the repository:

```bash
git clone https://github.com/md-aliyawar-khan/SOEN-6011-D2-arccos-calculator.git
```

Open the project directory:

```bash
cd SOEN-6011-D2-arccos-calculator
```

Run the application:

```bash
python problem5.py
```

If `python` is not mapped to Python 3 on your system, use:

```bash
python3 problem5.py
```

## Using the Application

1. Enter a finite numeric value of $x$ in the interval $[-1, 1]$.
2. Select **Calculate** or press **Enter**.
3. Review the result in radians.
4. Select **Clear** to reset the interface, or **Exit** to close the application.
5. After an error, enter another value and calculate again without restarting the program.

## From-Scratch Scope

The numerical calculation does not use:

- `math.acos()`
- `math.asin()`
- `math.sin()`
- `math.cos()`
- `math.sqrt()`
- NumPy, SciPy, SymPy, or another numerical library
- Built-in inverse-trigonometric functions
- `abs()` for convergence checking

The application uses:

- `float()` only to convert text entered in the GUI into a numeric value
- Tkinter only to provide the graphical user interface
- Custom functions for absolute value, square root, Taylor-series evaluation,
  validation, and inverse-cosine calculation

Python `math.acos()` is used only to generate trusted reference values during
verification; it is not imported or called by `problem5.py`.

## Error Handling

The application handles the following conditions:

| Condition | Application behaviour |
| --- | --- |
| Empty input | Displays an input-required message |
| Nonnumeric input, such as `hello` | Displays a numeric-input message |
| `nan`, `inf`, or `-inf` | Displays a finite-number validation message |
| Value outside $[-1, 1]$, such as `2` | Displays a domain-validation message |
| Taylor series exceeds its iteration limit | Displays a convergence-error message |
| Square-root method exceeds its iteration limit | Displays a convergence-error message |

## Numerical Verification

The accuracy target is an absolute error of no more than $10^{-6}$ radians for
tested valid inputs:

$$
|\text{program result} - \text{reference value}| \leq 10^{-6}
$$

The following table contains observed results from the final version of
`problem5.py`. Reference values were generated with Python `math.acos()` only
for verification and are not used by the application.

| Input $x$ | Program result | Reference value | Absolute error |
| --- | ---: | ---: | ---: |
| `-1.0` | `3.141592653590` | `3.141592653590` | `0.00e+00` |
| `-0.9999` | `3.127450400112` | `3.127450400112` | `0.00e+00` |
| `-0.999` | `3.096867566421` | `3.096867566421` | `0.00e+00` |
| `0.0` | `1.570796326619` | `1.570796326795` | `1.76e-10` |
| `0.5` | `1.047197551172` | `1.047197551197` | `2.48e-11` |
| `0.999` | `0.044725087169` | `0.044725087169` | `8.33e-17` |
| `0.9999` | `0.014142253478` | `0.014142253478` | `7.81e-17` |
| `1.0` | `0.000000000000` | `0.000000000000` | `0.00e+00` |

## Test Cases

| Input | Expected behaviour |
| --- | --- |
| `0.5` | Displays approximately `1.0471975512` radians |
| `0` | Displays approximately `1.5707963268` radians |
| `1` | Displays `0.0000000000` radians |
| `-1` | Displays approximately `3.1415926536` radians |
| `0.999` | Displays approximately `0.0447250872` radians |
| `0.9999` | Displays approximately `0.0141422535` radians |
| `2` | Displays a domain-validation error |
| `-1.0001` | Displays a domain-validation error |
| `nan` | Displays a finite-number validation error |
| `inf` | Displays a finite-number validation error |
| `-inf` | Displays a finite-number validation error |
| `hello` | Displays a numeric-input error |
| Empty input | Displays an input-required error |

## Repository Contents

```text
README.md         Project overview, requirements, execution, numerical method, and tests
problem5.py       Tkinter GUI and from-scratch numerical implementation
SOEN_6011_D2.pdf  Compiled PDF presentation for Deliverable 2
d2_main.tex       LaTeX source code for the Deliverable 2 presentation
tkinter_b.png     GUI interface before calculation
tkinter_a.png     GUI interface after a successful calculation
```

## Repository URL

<https://github.com/md-aliyawar-khan/SOEN-6011-D2-arccos-calculator>