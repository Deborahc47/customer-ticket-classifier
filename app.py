import tkinter as tk
from tkinter import messagebox

from ticket_classifier import classify_ticket


def classify_message():
    message = ticket_text.get("1.0", tk.END).strip()

    if not message:
        messagebox.showwarning(
            "Missing messgae",
            "Please enter a customer support message"
        )
        return

    try:
        category, confidence = classify_ticket(message)

        result_label.config(
            text=(
                f"Predicted Category: {category}\n"
                f"Confidence: {confidence}%"
            )
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"Something went wrong:\n{error}"
        )


window = tk.Tk()
window.title("Customer Ticket Classifier")
window.geometry("650x500")

title_label = tk.Label(
    window,
    text="Customer Support Ticket Classifier",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=30)

instruction_label = tk.Label(
    window,
    text="Enter a customer support message below:",
    font=("Arial", 12)
)
instruction_label.pack(pady=10)

ticket_text = tk.Text(
    window,
    width=65,
    height=8,
    font=("Arial", 11)
)
ticket_text.pack(pady=10)

classify_button = tk.Button(
    window,
    text="Classify Ticket",
    command=classify_message,
    font=("Arial", 12),
    padx=20,
    pady=10
)
classify_button.pack(pady=20)

result_label = tk.Label(
    window,
    text="Predicted Category: --\nConfidence: --",
    font=("Arial", 15, "bold"),
    justify="left"
)
result_label.pack(pady=20)

window.mainloop()
       
