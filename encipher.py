def encipher(plaintext, n):
    ciphertext=''
    for l in plaintext:
        if ord(l)>96 and ord(l)<123:
            ciphertext+=chr((ord(l)-97+n)%26+97)
        elif ord(l)>64 and ord(l)<91:
            ciphertext+=chr((ord(l)-65+n)%26+65)
        else:
            ciphertext+=l
    return ciphertext

n=int(raw_input("shift\n"))
plaintext=raw_input("ciphertext\n")

print encipher(plaintext, n)
