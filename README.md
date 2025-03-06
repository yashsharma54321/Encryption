Encryption Program

Overview

This encryption program converts plaintext into an encrypted format that can only be decrypted using a specific key. The encryption algorithm ensures that only those who possess the exact key can successfully retrieve the original message.

Features

Secure encryption of plaintext

Decryption only possible with a specific key

Uses a predefined character set for encryption and decryption

Encryption Key

The program utilizes a predefined encryption key to encode and decode text. The key is as follows:

key = ['f', 't', 'W', 'q', '"', 'j', 'L', '$', '+', '3', '8', 'D', '/', 'Z',
       '>', '_', 'r', 'w', 'V', 'x', 'o', '|', '?', 'i', 'Y', '=', 'z', 'U',
       '5', 'E', '{', 'u', '.', 'b', 'T', ' ', '}', 'H', '*', 'v', ';', 'J',
       'e', 'l', '&', '0', '<', 'Q', '\\', 'F', '4', 'S', '!', 'O', 'p', 'n',
       'm', '-', 'N', 's', 'X', ':', 'y', ')', 'k', 'I', 'a', 'K', '^', '~',
       '2', '`', '(', ',', '@', '1', 'B', '%', 'h', "'", '7', '[', 'A', '6',
       'd', 'g', ']', 'P', 'R', 'C', 'G', 'c', '9', '#', 'M']

Installation

Clone the repository:

```
git clone https://github.com/yashsharma54321/Encryption.git
cd encryption-program
```

Ensure you have Python installed (version 3.x recommended).

Install required dependencies:

```
pip install -r requirements.txt
```

Usage

Encrypting Text

To encrypt text, run the encryption script with the plaintext input:

```
python encrypt.py "Your message here"
```

This will output the encrypted text.

Decrypting Text

To decrypt, use the decryption script with the encrypted text:

```
python decrypt.py "YourEncryptedMessage"
```

Only the correct key will allow successful decryption.

Example

```
$ python encrypt.py "Hello World!"
Encrypted: @c9a %UjRfT

$ python decrypt.py "@c9a %UjRfT"
Decrypted: Hello World!
```

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contributing

Feel free to submit pull requests or report issues in the repository.

Author

Yash Sharma

