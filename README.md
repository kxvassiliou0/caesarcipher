# Caesar Cipher Encryption and Decryption
This Python program implements the Caesar cipher algorithm, a classical encryption technique that has historical significance in the field of cryptography. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet. This shift value is the key used for both encryption and decryption.

## How it works
The program provides two main functions: 'encrypt' and 'decrypt'. The 'encrypt' function takes a plaintext message and a shift value as input, then returns the encrypted ciphertext. On the other hand, the 'decrypt' function reverses the process, taking a ciphertext and the same shift value to produce the original plaintext.

The core of the encryption and decryption is the encryptDecryptChar function. This function is responsible for handling individual characters, ensuring that only alphabetic characters are shifted, and preserving the case of the original letters.

## Output
![image](https://github.com/kxvassiliou0/caesarcipher/assets/34982747/d149f0f3-23b9-4978-9dc8-7e66e189b806)

*The above image shows the plaintext input provided by the user: 'Hello World', representing both upper and lower case characters. The program accepts this input, alongside a shift value in the form of an integer, and computes the ciphertext. The program then decrypts this back into plaintext that is human-readable.*
