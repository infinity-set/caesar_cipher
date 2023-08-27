import pyperclip

# Print the ASCII art title

print("""  ______      ___       _______      _______.     ___      .______           ______  __  .______    __    __   _______ .______      
 /      |    /   \     |   ____|    /       |    /   \     |   _  \         /      ||  | |   _  \  |  |  |  | |   ____||   _  \     
|  ,----'   /  ^  \    |  |__      |   (----`   /  ^  \    |  |_)  |       |  ,----'|  | |  |_)  | |  |__|  | |  |__   |  |_)  |    
|  |       /  /_\  \   |   __|      \   \      /  /_\  \   |      /        |  |     |  | |   ___/  |   __   | |   __|  |      /     
|  `----. /  _____  \  |  |____ .----)   |    /  _____  \  |  |\  \----.   |  `----.|  | |  |      |  |  |  | |  |____ |  |\  \----.
 \______|/__/     \__\ |_______||_______/    /__/     \__\ | _| `._____|    \______||__| | _|      |__|  |__| |_______|| _| `._____|
                                                                                                                                    """)

# The string to be encrypted/decrypted:
message = input("Type your secret message: ")

# Check if the input for the key is a valid positive whole number
while True:
    try:
        key = int(input("Enter your key length. Must be a positive whole number: "))
        if key >= 0:
            break  # Exit the loop if input is a valid positive whole number
        else:
            print("Please enter a positive whole number for the key.")
    except ValueError:
        print("Invalid input. Please enter a positive whole number for the key.")

# Check whether the program encrypts or decrypts:
while True:
    operation_mode = input("You must type either 'encrypt' or 'decrypt': ").lower()
    if operation_mode == "encrypt" or operation_mode == "decrypt":
        break
    else:
        print("Incorrect entry!")

# Every possible symbol that can be encrypted:
ALLOWED_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Stores the encrypted/decrypted form of the message:
translated_message = ''

# Calculate the number of allowed symbols
num_symbols = len(ALLOWED_SYMBOLS)

# Loop through each symbol in the message:
for symbol in message:
    # Check if the symbol is in the allowed symbols:
    if symbol in ALLOWED_SYMBOLS:
        symbol_index = ALLOWED_SYMBOLS.find(symbol)

        # Perform encryption/decryption based on the operation mode and handle wrap-around with modulo:
        if operation_mode == 'encrypt':
            translated_index = (symbol_index + key) % num_symbols
        elif operation_mode == 'decrypt':
            translated_index = (symbol_index - key) % num_symbols

        # Append the encrypted/decrypted symbol to the result:
        translated_message += ALLOWED_SYMBOLS[translated_index]
    else:
        # Append the symbol without encrypting/decrypting:
        translated_message += symbol

# Output the translated string:
print(translated_message)

# Copy the translated string to the clipboard:
pyperclip.copy(translated_message)
