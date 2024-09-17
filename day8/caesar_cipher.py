print("""
  ____                             ____ _       _               
 / ___|__ _  ___  ___  ___ _ __   / ___(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _ \ '__| | |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \  __/ |    | |___| | |_) | | | |  __/ |   
 \____\__,_|\___||___/\___|_|     \____|_| .__/|_| |_|\___|_|   
                                         |_|                    
""")


def encode(plain: str, key: int):
    cipher = ""
    if key > 26:
        key = key % 26

    if ord(plain) in range(ord("a"), ord("z") + 1):
        cipher = chr(ord(plain) + key)
        if ord(cipher) not in range(ord("a"), ord("z") + 1):
            cipher = chr(ord(cipher) - 26)

    if ord(plain) in range(ord("A"), ord("Z") + 1):
        cipher = chr(ord(plain) + key)
        if ord(cipher) not in range(ord("A"), ord("Z") + 1):
            cipher = chr(ord(cipher) - 26)

    return cipher


def decode(cipher: str, key: int):
    plain = ""
    if key > 26:
        key = key % 26

    if ord(cipher) in range(ord("a"), ord("z") + 1):
        plain = chr(ord(cipher) - key)
        if ord(plain) not in range(ord("a"), ord("z") + 1):
            plain = chr(ord(plain) + 26)

    if ord(cipher) in range(ord("A"), ord("Z") + 1):
        plain = chr(ord(cipher) - key)
        if ord(plain) not in range(ord("A"), ord("Z") + 1):
            plain = chr(ord(plain) + 26)

    return plain


mode = ""
while mode != "quit":
    mode = input("Do you want to ENCODE or DECODE or QUIT?\n").lower()

    if mode == "encode":
        plain_text = input("Enter the text you want to encode.\n")
        p_shift_key = int(input("Enter the shift key (Number) you want to use.\n")) % 26
        cipher_text = ""

        for letter in plain_text:
            if not letter.isalpha():
                cipher_text += letter
                continue
            cipher_text += encode(letter, p_shift_key)
        print(cipher_text)

    if mode == "decode":
        cipher_text = input("Enter the text you want to decode.\n")
        p_shift_key = int(input("Enter the shift key (Number).\n")) % 26
        plain_text = ""

        for letter in cipher_text:
            if not letter.isalpha():
                plain_text += letter
                continue
            plain_text += decode(letter, p_shift_key)
        print(plain_text)
