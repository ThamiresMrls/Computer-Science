from letter_probabilities import letter_prob


def decipher(ciphertext, n):
    possible_plaintext=''
    for l in ciphertext:
        possible_plaintext+=chr(ord(l)+n%26)
    return possible_plaintext

def probability_list(possible_plaintext):
    letter_count=[0]*27
    for l in possible_plaintext:
        if ord(l)==32:
            letter_count[26]+=1
        else:
            letter_count[(ord(l)-97)]+=1

    probablities=[0]*27
    n=0
    while n<27:
        probablities[n]=sum(letter_count)/float(letter_count[n])
    return probablities


def list_plaintexts(ciphertext):
    plaintexts=[[0]*27]*26
    for n in range(26):
        plaintexts[n]=probability_list(decipher(ciphertext, n))
    return plaintexts


def compare(ideal, probability1, probability2):
    difference1=0
    difference2=0
    for n in range(27):
        difference1+=abs(ideal[n]-probability1[n])
    for n in range(27):
        difference1+=abs(ideal[n]-probability2[n])
    if difference1>difference2:
        return difference2
    elif difference2>difference1:
        return difference1

def best_match(ciphertext):
    ideal=[0]*27
    ctr=0
    for l in 'abcdefghijklmnopqrstuvwxyz ':
        ideal[ctr]=letter_prob(l)

    plaintexts=list_plaintexts(ciphertext)
    match=plaintexts[0]
    n=1
    z=0
    while n<26:
        match=compare(ideal, match, plaintexts[n])
        z+=1
phrase = raw_input("text here")
print list_plaintexts(phrase)

