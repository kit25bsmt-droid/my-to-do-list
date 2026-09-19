
import tkinter as tk

# -----------------------------
# Create the calculator window
# -----------------------------

window = tk.Tk()
window.title("Burgundy & Gold Calculator")
window.geometry("350x500")
window.resizable(False, False)

# Burgundy and gold colors
burgundy = "#800020"
dark_burgundy = "#5C0018"
gold = "#D4AF37"
light_gold = "#F5E6A8"
white = "#FFFFFF"

# Window background
window.configure(bg=burgundy)


# -----------------------------
# Display
# -----------------------------

display = tk.Entry(
    window,
    font=("Arial", 28, "bold"),
    justify="right",
    bg=light_gold,
    fg=dark_burgundy,
    insertbackground=dark_burgundy,
    relief="sunken",
    bd=5
)

display.pack(
    padx=15,
    pady=20,
    fill="x",
    ipady=10
)


# -----------------------------
# Functions
# -----------------------------

def add_to_display(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    try:
        expression = display.get()

        # Convert calculator symbols to Python operators
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        answer = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, answer)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# -----------------------------
# Button layout
# -----------------------------

buttons = [
    ["C", "⌫", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", "."]
]


# -----------------------------
# Create buttons
# -----------------------------

for row in buttons:

    frame = tk.Frame(
        window,
        bg=burgundy
    )

    frame.pack(
        expand=True,
        fill="both"
    )

    for button in row:

        if button == "C":
            command = clear

        elif button == "⌫":
            command = backspace

        elif button == "=":
            command = calculate

        else:
            command = lambda value=button: add_to_display(value)

        tk.Button(
            frame,
            text=button,
            font=("Arial", 18, "bold"),
            bg=gold,
            fg=dark_burgundy,
            activebackground=light_gold,
            activeforeground=burgundy,
            relief="raised",
            bd=3,
            command=command
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=3,
            pady=3
        )


# -----------------------------
# Start calculator
# -----------------------------

window.mainloop()