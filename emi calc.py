import tkinter as tk
from tkinter import ttk

def greet_user():
    user_name = name_entry.get()
    greeting_label.config(text=f"Hello, {user_name}! Welcome to the EMI Calculator.")
    notebook.tab(1, state="normal")  # Enable the second tab (Reasons to Calculate EMI)

def reason_selected():
    selected_reason = reason_var.get()
    reason_label.config(text=f"Calculating EMI for: {selected_reason}")
    notebook.tab(2, state="normal")  # Enable the third tab (EMI Calculation)

def calculate_emi(principal, rate, time):
    rate = rate / 1200  # converting annual interest rate to monthly and percentage to decimal
    emi = (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
    return emi

def calculate_button_clicked():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = int(time_entry.get())

        emi_result = calculate_emi(principal, rate, time)
        result_label.config(text=f"EMI: ${emi_result:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("EMI Calculator")

# Create notebook (tabbed interface)
notebook = ttk.Notebook(window)

# First page - Greeting
greeting_frame = ttk.Frame(notebook)
notebook.add(greeting_frame, text="Greeting")

greeting_label = ttk.Label(greeting_frame, text="Hello! Please enter your name:")
greeting_label.grid(row=0, column=0, padx=10, pady=10)

name_entry = ttk.Entry(greeting_frame)
name_entry.grid(row=1, column=0, padx=10, pady=10)

continue_button = ttk.Button(greeting_frame, text="Continue", command=greet_user)
continue_button.grid(row=2, column=0, pady=10)

# Second page - Reasons to Calculate EMI
reason_frame = ttk.Frame(notebook)
notebook.add(reason_frame, text="Reasons to Calculate EMI")
notebook.tab(1, state="disabled")  # Disable the second tab initially

reason_label = ttk.Label(reason_frame, text="Select a reason to calculate EMI:")
reason_label.grid(row=0, column=0, padx=10, pady=10)

reasons = ["Home Loan", "Car Loan", "Education Loan", "Personal Loan"]
reason_var = tk.StringVar(value=reasons[0])

reason_combobox = ttk.Combobox(reason_frame, values=reasons, textvariable=reason_var)
reason_combobox.grid(row=1, column=0, padx=10, pady=10)

reason_continue_button = ttk.Button(reason_frame, text="Continue", command=reason_selected)
reason_continue_button.grid(row=2, column=0, pady=10)

# Third page - EMI Calculation
emi_frame = ttk.Frame(notebook)
notebook.add(emi_frame, text="EMI Calculation")
notebook.tab(2, state="disabled")  # Disable the third tab initially

# Widgets for EMI Calculation
principal_label = ttk.Label(emi_frame, text="Principal Amount:")
principal_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

principal_entry = ttk.Entry(emi_frame)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

rate_label = ttk.Label(emi_frame, text="Annual Interest Rate (%):")
rate_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

rate_entry = ttk.Entry(emi_frame)
rate_entry.grid(row=1, column=1, padx=10, pady=10)

time_label = ttk.Label(emi_frame, text="Loan Term (Months):")
time_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

time_entry = ttk.Entry(emi_frame)
time_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = ttk.Button(emi_frame, text="Calculate EMI", command=calculate_button_clicked)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(emi_frame, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
notebook.pack(expand=True, fill="both")
window.mainloop()
