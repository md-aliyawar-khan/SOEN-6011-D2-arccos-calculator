"""
SOEN 6011 - Deliverable 2
Problem 5: From-Scratch arccos(x) Tkinter GUI

The program calculates arccos(x) in radians using:
arccos(x) = pi / 2 - arcsin(x)

arcsin(x) is computed with a Taylor-series recurrence.
No math library or built-in inverse-trigonometric function is used.
"""

import tkinter as tk


PI = 3.141592653589793
TOLERANCE = 1e-10
MAX_ITERATIONS = 1000


class InputValidationError(Exception):
    """Raised when the input is invalid."""


class ConvergenceError(Exception):
    """Raised when the Taylor series fails to converge."""


def absolute_value(value):
    """Return the absolute value without using abs()."""
    if value < 0:
        return -value
    return value


def is_finite_number(value):
    """Return True only if value is not NaN, inf, or -inf."""
    if value != value:
        return False

    if value == float("inf") or value == float("-inf"):
        return False

    return True


def calculate_arcsin(x):
    """
    Calculate arcsin(x) with a Taylor-series recurrence.

    Precondition: x is finite and belongs to [-1, 1].
    """
    if x == 1.0:
        return PI / 2.0

    if x == -1.0:
        return -PI / 2.0

    result = 0.0
    coefficient = 1.0
    power = x
    iteration = 0

    while True:
        term = coefficient * power

        if absolute_value(term) <= TOLERANCE:
            return result

        if iteration >= MAX_ITERATIONS:
            raise ConvergenceError(
                "Calculation did not converge within "
                + str(MAX_ITERATIONS)
                + " iterations."
            )

        result = result + term
        iteration = iteration + 1

        coefficient = (
            coefficient
            * (2 * iteration - 1)
            * (2 * iteration - 1)
            / ((2 * iteration) * (2 * iteration + 1))
        )

        power = power * x * x


def calculate_arccos(x):
    """
    Calculate arccos(x) in radians.

    The result belongs to the principal range [0, pi].
    """
    if not is_finite_number(x):
        raise InputValidationError(
            "Enter a finite number. Values such as nan and inf are not allowed."
        )

    if x < -1.0 or x > 1.0:
        raise InputValidationError(
            "Input is outside the valid domain. Enter a value from -1 to 1."
        )

    if x == 1.0:
        return 0.0

    if x == -1.0:
        return PI

    return (PI / 2.0) - calculate_arcsin(x)


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
            # Used only for conversion of text entered in the GUI.
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