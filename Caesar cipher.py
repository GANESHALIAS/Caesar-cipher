import tkinter as tk 
from tkinter import messagebox


# ENCRYPT TEXT
def caesar_cipher_encrypt(text, shift):
    """
    This function takes in a plaintext string and a shift value and returns
    the Caesar cipher text by shifting each letter in the plaintext by the given shift value.
    """
    cipher_text = ""
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character by the shift value and wrap around the alphabet
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character by the shift value and wrap around the alphabet
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If the character is not a letter, add it to the cipher text as is
            cipher_text += char
    return cipher_text


def encrypt_text():
    try:
        plaintext = plaintext_entry.get()
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showinfo("ERROR", "Enter all the correct values.")
    else:
        ciphertext = caesar_cipher_encrypt(plaintext, shift)
        ciphertext_entry.delete(0, tk.END)
        ciphertext_entry.insert(0, ciphertext)


# Create a tkinter window
window = tk.Tk()
window.geometry("250x150")
window.title("Caesar Cipher Encryption")

# Create a label for the plaintext input field
plaintext_label = tk.Label(window, text="Plaintext:")
plaintext_label.grid(row=0, column=0)

# Create an input field for the plaintext
plaintext_entry = tk.Entry(window)
plaintext_entry.grid(row=0, column=1)

label = tk.Label(window, text="FOR DeCRYPTION PUT SHIFT VALUE ")
label.grid(row=1, column=0, columnspan=3)

label = tk.Label(window, text="NEGATIVE OF ENCRYPTED SHIFT VALUE")
label.grid(row=2, column=0, columnspan=3)

# Create a label for the shift input field
shift_label = tk.Label(window, text="Shift:")
shift_label.grid(row=3, column=0)

# Create an input field for the shift
shift_entry = tk.Entry(window)
shift_entry.grid(row=3, column=1)

# Create a button to encrypt the plaintext
encrypt_button = tk.Button(window, text="Encrypt/Decrypt", command=encrypt_text)
encrypt_button.grid(row=4, column=0, columnspan=3)

# Create a label for the ciphertext output field
ciphertext_label = tk.Label(window, text="Ciphertext:")
ciphertext_label.grid(row=5, column=0)

# Create an output field for the ciphertext
ciphertext_entry = tk.Entry(window)
ciphertext_entry.grid(row=5, column=1)

# Start the main event loop
window.mainloop()
