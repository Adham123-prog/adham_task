import itertools
import string
import tkinter as tk
from tkinter import filedialog, messagebox

# Hardcoded correct passwords for multiple users
USER_CREDENTIALS = {
    "user1": "abcDe",
    "admin": "passX",
    "test": "hello"
}

# Function to perform Dictionary Attack
def dictionary_attack(username, password, wordlist):
    output_text.insert(tk.END, f"\nTrying Dictionary Attack for {username}...\n")
    
    for word in wordlist:
        word = word.strip()  # Remove any spaces or newlines
        if word == password:
            output_text.insert(tk.END, f"✅ Success! Password found: {password}\n")
            return True
    
    output_text.insert(tk.END, "❌ Dictionary Attack Failed. Moving to Brute Force Attack...\n")
    return False

# Function to perform Brute Force Attack
def brute_force_attack(password):
    output_text.insert(tk.END, "\n🔄 Starting Brute Force Attack...\n")
    
    chars = string.ascii_letters  # A-Z, a-z
    attempts = 0
    
    for guess in itertools.product(chars, repeat=5):  # Generate all 5-letter passwords
        attempts += 1
        guess_password = ''.join(guess)
        
        if guess_password == password:
            output_text.insert(tk.END, f"✅ Success! Password cracked: {password} in {attempts} attempts.\n")
            return True
    
    output_text.insert(tk.END, "❌ Brute Force Attack Failed.\n")
    return False

# Function to start the attack
def start_attack():
    username = username_entry.get().strip()
    
    if username not in USER_CREDENTIALS:
        messagebox.showerror("Error", "Username not found!")
        return
    
    password = USER_CREDENTIALS[username]
    
    # Load dictionary file
    file_path = filedialog.askopenfilename(title="Select Dictionary File",
                                           filetypes=[("Text Files", "*.txt")])
    
    if not file_path:
        messagebox.showwarning("Warning", "No dictionary file selected. Skipping dictionary attack.")
        dictionary_wordlist = []
    else:
        with open(file_path, "r") as file:
            dictionary_wordlist = file.readlines()
    
    output_text.insert(tk.END, f"\n🔍 Attempting to crack password for user: {username}\n")
    
    # Try Dictionary Attack first
    if not dictionary_attack(username, password, dictionary_wordlist):
        # If dictionary attack fails, perform brute force attack
        brute_force_attack(password)

# GUI Setup
root = tk.Tk()
root.title("Password Cracker")
root.geometry("500x400")

# UI Components
tk.Label(root, text="Enter Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

attack_button = tk.Button(root, text="Start Attack", command=start_attack, bg="red", fg="white")
attack_button.pack(pady=10)

output_text = tk.Text(root, height=15, width=60)
output_text.pack()

# Run GUI
root.mainloop()
