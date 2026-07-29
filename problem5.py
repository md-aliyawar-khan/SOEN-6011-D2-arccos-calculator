"""
SOEN 6011 - Deliverable 2
Problem 5: From-Scratch arccos(x) Tkinter GUI

The program calculates arccos(x) in radians using a Taylor series
with range reduction near the endpoints.

For x >= 0:
arccos(x) = 2 * arcsin(sqrt((1 - x) / 2))

For x < 0:
arccos(x) = pi - arccos(-x)

arcsin(x) is computed using a Taylor-series recurrence.
The square root is computed using Newton's method.
No math library or built-in inverse-trigonometric function is used.
"""

import tkinter as tk


PI = 3.141592653589793
TOLERANCE = 1e-10
MAX_ITERATIONS = 1000
SQRT_TOLERANCE = 1e-14
SQRT_MAX_ITERATIONS = 100
MAX_FINITE_MAGNITUDE = 1e308


class InputValidationError(Exception):
    """Raised when the input is invalid."""


class ConvergenceError(Exception):
    """Raised when a numerical method fails to converge."""


def absolute_value(value):
    """Return the absolute value without using abs()."""
    if value < 0.0:
        return -value
    return value


def is_finite_number(value):
    """
    Return True only if value is finite.

    NaN is rejected because NaN is not equal to itself.
    Extremely large values are rejected without using float("inf").
    """
    if value != value:
        return False

    if absolute_value(value) > MAX_FINITE_MAGNITUDE:
        return False

    return True


def calculate_square_root(value):
    """
    Calculate sqrt(value) with Newton's method.

    Precondition: value is finite and value >= 0.
    """
    if value < 0.0:
        raise InputValidationError(
            "Square root input must be greater than or equal to zero."
        )

    if value == 0.0:
        return 0.0

    guess = 1.0
    iteration = 0

    while iteration < SQRT_MAX_ITERATIONS:
        next_guess = 0.5 * (guess + value / guess)

        if absolute_value(next_guess - guess) <= SQRT_TOLERANCE:
            return next_guess

        guess = next_guess
        iteration = iteration + 1

    raise ConvergenceError(
        "Square-root calculation did not converge within "
        + str(SQRT_MAX_ITERATIONS)
        + " iterations."
    )


def calculate_arcsin(x):
    """
    Calculate arcsin(x) with a Taylor-series recurrence.

    The function is used only with a reduced input magnitude,
    improving convergence near arccos endpoints.
    Precondition: x is finite and belongs to [-1, 1].
    """
    if x == 0.0:
        return 0.0

    result = 0.0
    coefficient = 1.0
    power = x
    iteration = 0

    while iteration < MAX_ITERATIONS:
        term = coefficient * power
        result = result + term

        if absolute_value(term) <= TOLERANCE:
            return result

        iteration = iteration + 1

        coefficient = (
            coefficient
            * (2 * iteration - 1)
            * (2 * iteration - 1)
            / ((2 * iteration) * (2 * iteration + 1))
        )

        power = power * x * x

    raise ConvergenceError(
        "Taylor-series calculation did not converge within "
        + str(MAX_ITERATIONS)
        + " iterations."
    )


def calculate_arccos(x):
    """
    Calculate arccos(x) in radians.

    The result belongs to the principal range [0, pi].
    Range reduction improves Taylor-series convergence near x = -1 and x = 1.
    """
    if not is_finite_number(x):
        raise InputValidationError(
            "Enter a finite number. Values such as nan are not allowed."
        )

    if x < -1.0 or x > 1.0:
        raise InputValidationError(
            "Input is outside the valid domain. Enter a value from -1 to 1."
        )

    if x == 1.0:
        return 0.0

    if x == -1.0:
        return PI

    if x < 0.0:
        return PI - calculate_arccos(-x)

    reduced_input = calculate_square_root((1.0 - x) / 2.0)
    return 2.0 * calculate_arcsin(reduced_input)


class ArccosCalculatorGUI:
    """Tkinter GUI for the arccos(x) calculator."""

    def __init__(self, window):
        self.window = window
        self.window.title("arccos(x) Calculator")
        self.window.geometry("560x340")
        self.window.resizable(False, False)
        self.window.configure(bg="#F5F7FA")

        self.build_interface()

    def build_interface(self):
        tk.Label(
            self.window,
            text="arccos(x) Calculator",
            font=("Arial", 18, "bold"),
            fg="#1C437B",
            bg="#F5F7FA"
        ).pack(pady=(24, 8))

        tk.Label(
            self.window,
            text="Enter a finite value of x where -1 <= x <= 1",
            font=("Arial", 11),
            fg="#232323",
            bg="#F5F7FA"
        ).pack(pady=(0, 14))

        input_frame = tk.Frame(self.window, bg="#F5F7FA")
        input_frame.pack(pady=4)

        tk.Label(
            input_frame,
            text="x =",
            font=("Arial", 12, "bold"),
            fg="#232323",
            bg="#F5F7FA"
        ).pack(side=tk.LEFT, padx=(0, 8))

        self.input_entry = tk.Entry(
            input_frame,
            width=24,
            font=("Arial", 12),
            justify="center"
        )
        self.input_entry.pack(side=tk.LEFT)
        self.input_entry.focus_set()

        button_frame = tk.Frame(self.window, bg="#F5F7FA")
        button_frame.pack(pady=18)

        tk.Button(
            button_frame,
            text="Calculate",
            width=12,
            font=("Arial", 10, "bold"),
            bg="#1C437B",
            fg="white",
            command=self.calculate
        ).pack(side=tk.LEFT, padx=6)

        tk.Button(
            button_frame,
            text="Clear",
            width=12,
            font=("Arial", 10),
            command=self.clear_fields
        ).pack(side=tk.LEFT, padx=6)

        tk.Button(
            button_frame,
            text="Exit",
            width=12,
            font=("Arial", 10),
            command=self.window.destroy
        ).pack(side=tk.LEFT, padx=6)

        self.result_label = tk.Label(
            self.window,
            text="Result will be displayed here.",
            font=("Arial", 12, "bold"),
            fg="#1C437B",
            bg="#F5F7FA",
            wraplength=510
        )
        self.result_label.pack(pady=(8, 6))

        self.status_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 10),
            fg="#B00020",
            bg="#F5F7FA",
            wraplength=510
        )
        self.status_label.pack(pady=(4, 10))

        self.window.bind("<Return>", self.calculate_from_enter)

    def calculate_from_enter(self, event):
        """Run calculation when the user presses Enter."""
        self.calculate()

    def calculate(self):
        """Validate GUI input and display either a result or a helpful error."""
        input_text = self.input_entry.get().strip()

        self.result_label.config(
            text="Result will be displayed here.",
            fg="#1C437B"
        )
        self.status_label.config(text="", fg="#B00020")

        if input_text == "":
            self.status_label.config(
                text="Input is required. Enter a finite number from -1 to 1."
            )
            return

        try:
            # Used only to convert GUI text into a numeric value.
            value = float(input_text)
            result = calculate_arccos(value)

            self.result_label.config(
                text="arccos(" + str(value) + ") = "
                + format(result, ".10f")
                + " radians"
            )
            self.status_label.config(
                text="Calculation completed successfully.",
                fg="#147A3C"
            )

        except ValueError:
            self.status_label.config(
                text="Invalid input. Enter a number such as 0, 0.5, or -0.75."
            )

        except InputValidationError as error:
            self.status_label.config(text=str(error))

        except ConvergenceError as error:
            self.status_label.config(text=str(error))

    def clear_fields(self):
        """Clear all displayed input and feedback."""
        self.input_entry.delete(0, tk.END)
        self.result_label.config(
            text="Result will be displayed here.",
            fg="#1C437B"
        )
        self.status_label.config(text="")
        self.input_entry.focus_set()


def main():
    """Start the Tkinter application."""
    window = tk.Tk()
    ArccosCalculatorGUI(window)
    window.mainloop()


if __name__ == "__main__":
    main()