def encryptDecryptChar(plaintextChar, shift, mode='encrypt'):
    """
    Encrypts or decrypts a single character based on the Caesar cipher algorithm
    - param plaintextChar: The character to be encrypted or decrypted
    - param shift: The number of positions to shift the character
    - param mode: 'encrypt' for encryption, 'decrypt' for decryption
    """
    if plaintextChar.isalpha():
        firstAlphabetLetter = 'a'
        # Allows upper and mixed case input
        if plaintextChar.isupper():
            firstAlphabetLetter = 'A'

        oldCharPosition = ord(plaintextChar) - ord(firstAlphabetLetter)  # Position of the current plain text character

        if mode == 'encrypt':
            newCharPosition = (oldCharPosition + shift) % 26 # MOD 26 since there are 26 characters in the English alphabet
        else:
            newCharPosition = (oldCharPosition - shift) % 26

        return chr(newCharPosition + ord(firstAlphabetLetter))
    return plaintextChar  # If not in the alphabet


def encrypt(plaintext, shift):
    """
    Encrypts plaintext using params :
    - param plaintext: The input text to be encrypted
    - param shift: The number of positions to shift each character
    """
    ciphertext = ''

    for plaintextChar in plaintext:
        ciphertext += encryptDecryptChar(plaintextChar, shift)
    return ciphertext # Returns the encrypted ciphertext


def decrypt(ciphertext, shift):
    """
    Decrypts ciphertext using params: 
    - param ciphertext: The input text to be decrypted
    - param shift: The number of positions to shift each character
    """
    plaintext = ''

    for ciphertextChar in ciphertext:
        plaintext += encryptDecryptChar(ciphertextChar, shift, mode='decrypt')
    return plaintext # Return the decrypted plaintext

# Accepts user inputs
plaintext = input('Enter a message: ')
shift = int(input('Shift number: ')) # User input as an integer

ciphertext = encrypt(plaintext, shift)
decryptedPlaintext = decrypt(ciphertext, shift)

# Print statements for visual feedback
print(f'Ciphertext: {ciphertext}')
print(f'Decrypted Plaintext: {decryptedPlaintext}')