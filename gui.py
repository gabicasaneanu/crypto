import tkinter as tk
import subprocess

key_entry_val = ''
encrypted = False

def perform_command():
    global encrypted
    input_value = input_entry.get()
    if input_value:
        plaintext = subprocess.run(['python3','crypt.py',input_value,key_entry_val],capture_output = True).stdout
        output_value = "Output: " + plaintext.decode("utf-8")
        output_label.config(text=output_value)
        encrypted = True
    else:
        output_label.config(text="no plaintext entered")
    
def get_key():
    global key_entry_val
    key_entry_val = key_entry.get()
    
def decrypt():
    input_value = input_entry.get()
    if encrypted == False:
        output_label.config(text = "Have not encrypted")
    else:
        out_val = "Output:" + input_value
        output_label.config(text=out_val)
# Create the main window
root = tk.Tk()
root.title("Command GUI")
root.geometry("400x400")

# Create input entry
plaintext_label = tk.Label(root,text= "Plaintext").place(x = 175,y = 0)
input_entry = tk.Entry(root, width=30)
input_entry.pack(pady=20)

key_label = tk.Label(root,text = "Key").place(x = 180,y = 80)
key_entry = tk.Entry(root,width = 30)
key_entry.pack(pady = 40)

key_button = tk.Button(root, text = "Input key", command = get_key)
key_button.pack()
# Create button to perform command
perform_button = tk.Button(root, text="Encrypt", command=perform_command)
perform_button.pack(pady= 10)


decrypt_button = tk.Button(root, text = "Decrypt", command= decrypt)
decrypt_button.pack(pady = 10)

# Create output label
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
