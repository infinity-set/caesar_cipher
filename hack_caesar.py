ciphertext = input("Type your encrypted message: ")
ALLOWED_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Iterate through all possible keys:
for decryption_key in range(len(ALLOWED_SYMBOLS)):
    # Set the decrypted message to an empty string at the start of each iteration
    decrypted_message = ''

    # Decrypt the message using the current key:
    for symbol in ciphertext:
        if symbol in ALLOWED_SYMBOLS:
            # If the symbol is within the defined character set, find its index
            symbol_index = ALLOWED_SYMBOLS.find(symbol)

            # Calculate the index of the symbol after decryption
            decrypted_index = symbol_index - decryption_key

            # Handle the wrap-around:
            if decrypted_index < 0:
                decrypted_index = decrypted_index + len(ALLOWED_SYMBOLS)

            # Append the decrypted symbol:
            decrypted_message = decrypted_message + ALLOWED_SYMBOLS[decrypted_index]
        else:
            # Append the symbol without decrypting:
            decrypted_message = decrypted_message + symbol

    # Display the decrypted message for the current key:
    print(f'Decryption with Key {decryption_key}: {decrypted_message}')

