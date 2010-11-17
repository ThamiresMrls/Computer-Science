###THIS IS DANIEL'S CODE AND IT WORKS YEAAAAAAAAAAAH
###DANIEL DYSSEGAARD KALLICK THAT IS.
try:
    from letter_probabilities import letter_prob
except ImportError:
    print "You need letter_probabilities.py in the same directory"
    print "Ain't nothing gonna work without letter_probabilities.py"
def decipher(ciphertext, n):
    """
    Takes in a ciphertext and a number, 'n'. Every letter is then
    shifted n characters forward in the alphabet, modulo 26.
    Capitals are dealt with. If it's not a letter, it's just tacked
    on. (spaces and symbols are not shifted). Returns the enciphered
    (or deciphered text).
    """
    possible_plaintext=''
    for l in ciphertext:
        #lowercase
        if ord(l)>96 and ord(l)<123:
            #subtract 97 to get ord to be the posistion in the 
            #alphabet, add n, modulo 26 it, add 97 again to get
            #it back to the right ord for chr.
            possible_plaintext+=chr((ord(l)-97+n)%26+97)
        #uppercase
        elif ord(l)>64 and ord(l)<91:
            possible_plaintext+=chr((ord(l)-65+n)%26+65)
        else:
            possible_plaintext+=l
    return possible_plaintext

def probability_list(possible_plaintext,shift):
    """
    Takes in a phrase, returns a list of the
    relative frequencies of each letter's appearance.
    Capitals are treated as lowercase, and spaces and
    symbols are ignored. the ouput list has the relative frequency of
    a as the 0th value and the relative frequency of z as the 25th value.
    """
    letter_count=[0]*26
    for l in possible_plaintext:
        if ord(l)>96 and ord(l)<123:
            letter_count[(ord(l)-97)]+=1
        elif ord(l)>64 and ord(l)<91:
            letter_count[(ord(l)-65)]+=1

    probablities=[0]*27
    n=0
    while n<26:
        #number of letter in question over total number of letters
        probablities[n]=float(letter_count[n])/sum(letter_count)
        n+=1
    #keep track of which decryption it is (that is, how far it's shifted)
    probablities[26]=shift
    return probablities


def list_plaintexts(ciphertext):
    """
    takes in a ciphertext, returns a list
    of all of the possible relative
    letter frequency distributions
    of all of the possible plaintexts
    see also probability_list and decipher
    """
    plaintexts=[[0]*27]*26
    for n in range(26):
        plaintexts[n]=probability_list(decipher(ciphertext, n),n)
    return plaintexts


def compare(probability1, probability2):
    """
    Takes in two possible letter frequency distributions,
    returns the one that deviates least from the
    ideal english letter frequency distribution
    """
    #difference1 is the deviation from the ideal of 
    #probability1, difference2 is the deviation from 
    #the ideal of probability2.
    difference1=0
    difference2=0

    #get the ideal
    ideal=[0]*26
    ctr=0
    for l in 'abcdefghijklmnopqrstuvwxyz':
        ideal[ctr]=letter_prob(l)
        ctr+=1

    for n in range(26):
        #for each letter, see how far off it is from the ideal
        #distribution of that letter, and add it to the total
        #deviation for that decryption
        difference1+=abs(ideal[n]-probability1[n])
    for n in range(26):
        difference2+=abs(ideal[n]-probability2[n])
    if difference1>difference2:
        return probability2
    else:
        return probability1

def best_match(ciphertext):
    """
    Takes in a ciphertext, returns the most likely plaintext
    """
    plaintexts=list_plaintexts(ciphertext)
    match=plaintexts[0]
    n=1
    while n<26:
        match=compare(match, plaintexts[n])
        n+=1
    return match
phrase = raw_input("text here\n")
match_distribution = best_match(phrase)
#in the 26th element of each distribution the shift of that distribution
#is stored. This can then be used to decipher the text.
shift=match_distribution[26]
decryption=decipher(phrase, shift)
print "The shift was", shift
print "The decrypted text is"
print decryption
