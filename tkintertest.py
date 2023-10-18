import tkinter as tk

# Function to evaluate the expression and update the display
def calculate():
    try:
        result = eval(entry.get())
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget for user input
entry = tk.Entry(window, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operators
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Function to handle button clicks
def button_click(event):
    current_text = entry.get()
    clicked_text = event.widget.cget("text")

    if clicked_text == "=":
        calculate()
    elif clicked_text == "C":
        entry.delete(0, tk.END)
        result_label.config(text="Result: ")
    else:
        entry.insert(tk.END, clicked_text)

row, col = 1, 0
for text in button_texts:
    if text == "=":
        button = tk.Button(window, text=text, width=10, height=2, command=calculate)
    elif text == "C":
        button = tk.Button(window, text=text, width=10, height=2, command=lambda t=text: entry.delete(0, tk.END))
    else:
        button = tk.Button(window, text=text, width=5, height=2)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create a button to clear the entry
clear_button = tk.Button(window, text="C", width=5, height=2, command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=row, column=col)
col += 1
if col > 3:
    col = 0
    row += 1


# Create a label to display the result
result_label = tk.Label(window, text="Result: ", font=("Arial", 16))
result_label.grid(row=row, column=0, columnspan=4)

window.mainloop()
