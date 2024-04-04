import tkinter as tk
import subprocess

def perform_command():
    input_value = input_entry.get()
    plaintext = subprocess.run(['python3','crypto.py',input_value],capture_output = True).stdout
    output_value = "Output: " + plaintext.decode("utf-8")
    output_label.config(text=output_value)

# Create the main window
root = tk.Tk()
root.title("Command GUI")

# Create input entry
input_entry = tk.Entry(root, width=30)
input_entry.pack(pady=10)

# Create button to perform command
perform_button = tk.Button(root, text="Perform Command", command=perform_command)
perform_button.pack()

# Create output label
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
