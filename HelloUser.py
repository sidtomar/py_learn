import tkinter as tk

# This function runs when the Submit button is clicked.
def show_greeting():
    # Read the current text from the name input box.
    username = name_entry.get()

    # Show a validation message if the user did not type a real name.
    if username == "" or username == placeholder_text:
        result_label.config(text="Please enter your name")
    else:
        # Display the greeting in the window and also print it in the console.
        result_label.config(text=f'Hello {username} How are you doing?')
        print(f'Hello {username}, How are you doing?')

# This function removes the placeholder text when the user clicks inside the input box.
def clear_placeholder(event):
    if name_entry.get() == placeholder_text:
        name_entry.delete(0, tk.END)
        name_entry.config(fg="black")

# This function adds the placeholder back if the user leaves the input box empty.
def add_placeholder(event):
    if name_entry.get() == "":
        name_entry.insert(0, placeholder_text)
        name_entry.config(fg="gray")

# Create the main application window.
root = tk.Tk()
root.title("Hello User")
root.geometry("350x200")

# Text shown inside the input box before the user types their name.
placeholder_text = "Please enter your name"

# Create the name input box and show placeholder text in gray.
name_entry = tk.Entry(root, width=30, fg="gray")
name_entry.insert(0, placeholder_text)
name_entry.pack(pady=20)

# Connect focus events to the placeholder helper functions.
name_entry.bind("<FocusIn>", clear_placeholder)
name_entry.bind("<FocusOut>", add_placeholder)

# Create the Enter button and connect it to the greeting function.
button = tk.Button(root, text="Enter", command=show_greeting)
button.pack(pady=10)

# Create a label that will show validation messages or the greeting.
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start the Tkinter event loop so the window stays open and responds to user actions.
root.mainloop()
