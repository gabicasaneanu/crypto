import tkinter as tk

import subprocess

import pyperclip



key_entry_val = ''

encrypted = False



color_names = ["Midnight Purple", "Dark Blue", "Dark Orange", "Crimson Red", "Forest Green", "Golden Yellow", "Turquoise", "Lavender"]

colors = ["#2E0854", "#00008B", "#FF4500", "#DC143C", "#228B22", "#FFD700", "#40E0D0", "#E6E6FA"]



def perform_command():

    global encrypted

    input_value = input_entry.get()

    if input_value:

        plaintext = subprocess.run(['python3', 'crypt.py', input_value, key_entry_val], capture_output=True).stdout

        encrypted_text = plaintext.decode("utf-8").strip()

        output_value = "Output: " + encrypted_text

        output_text.delete(1.0, tk.END)  # Clear previous output

        output_text.insert(tk.END, output_value)

        pyperclip.copy(encrypted_text)  # Copy encrypted text to clipboard

        encrypted = True

    else:

        output_text.delete(1.0, tk.END)  # Clear previous output

        output_text.insert(tk.END, "no plaintext entered")



def get_key():

    global key_entry_val

    key_entry_val = key_entry.get()



def decrypt():

    input_value = input_entry.get()

    if encrypted == False:

        output_text.delete(1.0, tk.END)  # Clear previous output

        output_text.insert(tk.END, "Have not encrypted")

    else:

        output_text.delete(1.0, tk.END)  # Clear previous output

        output_text.insert(tk.END, "Output: " + input_value)



def copy_output():

    pyperclip.copy(output_text.get(1.0, tk.END).split(": ")[1])



def change_color(selected_color):

    root.config(bg=selected_color)



# Create the main window

root = tk.Tk()

root.title("Command GUI")

root.geometry("500x400")



# Create input entry

plaintext_label = tk.Label(root, text="Plaintext", anchor="w", justify="left")

plaintext_label.grid(row=0, column=0, padx=10, pady=5)



input_entry = tk.Entry(root, width=30)

input_entry.grid(row=1, column=0, padx=10, pady=5)



key_label = tk.Label(root, text="Key", anchor="w", justify="left")

key_label.grid(row=2, column=0, padx=10, pady=5)



key_entry = tk.Entry(root, width=30)

key_entry.grid(row=3, column=0, padx=10, pady=5)



key_button = tk.Button(root, text="Input key", command=get_key)

key_button.grid(row=4, column=0, padx=10, pady=5)



# Create button to perform command

perform_button = tk.Button(root, text="Encrypt", command=perform_command)

perform_button.grid(row=5, column=0, padx=10, pady=5)



decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)

decrypt_button.grid(row=6, column=0, padx=10, pady=5)



# Create dropdown for theme selection

selected_color = tk.StringVar()

selected_color.set(color_names[0])  # default value



theme_dropdown = tk.OptionMenu(root, selected_color, *color_names, command=lambda color_name: change_color(colors[color_names.index(color_name)]))

theme_dropdown.grid(row=7, column=0, padx=10, pady=5)



# Create output text widget

output_text = tk.Text(root, height=2, width=40)

output_text.grid(row=8, column=0, columnspan=2, padx=10, pady=5)



# Create copy button

copy_button = tk.Button(root, text="Copy", command=copy_output)

copy_button.grid(row=9, column=0, columnspan=2, padx=10, pady=5)



# Run the Tkinter event loop

root.mainloop()
