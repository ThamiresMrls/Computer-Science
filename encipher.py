def encipher(plaintext, n):
    ciphertext=''
    for l in plaintext:
        if ord(l)==32:
            ciphertext+=l
        else:
            ciphertext+=chr(ord(l)+n%26)
    return ciphertext

n=int(raw_input("shift\n"))
plaintext=raw_input("ciphertext\n")

print encipher(plaintext, n)
