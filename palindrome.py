#homework number 12 Daniel Dyssegaard Kallick
def palindromecheck(word):
    """Check for palindromeness"""
    word=clean_word(word, palindromecheck)
    ctr=len(word)
    new_word=''
    while ctr>0:
        new_word+=word[ctr-1]
        ctr-=1
    return new_word==word
def clean_word(word, function):
    """
    Cleans a word (or a phrase) of all things that are not letters. if the function is word level,
    keep the apostrophes, otherwise don't. Get rid of all capitals
    """
    replacement_word=''
    replacement_word1=''
    #get rid of spaces and numbers and symbols. If it's word level, don't get rid of apostrophes
    if function==word_level_palindromes:
        for l in word:
            if l in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'":
                replacement_word+=l
    #get rid of spaces and numbers and symbols.
    if function==palindromecheck:
        for l in word:
            if l in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
                replacement_word+=l
    #get rid of uppercase
    for l in replacement_word:
        if ord(l)>64 and ord(l)<91:
            replacement_word1+=chr(ord(l)+32)
        else:
            replacement_word1+=l
    return replacement_word1
def word_level_palindromes(phrase):
    """Check for word level palindromeness"""
    ctr=len(phrase)
    new_phrase=''
    ltrs="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'"
    while ctr>0:
        length_of_word=0
        #get the length of each word.
        while ctr-1>=0 and phrase[ctr-1] in ltrs:
            length_of_word+=1
            ctr-=1
        #add the word to the new phrase. ctr is iterating backwards, so ctr will be the start point
        #of the word, and it will be length_of_word letters long
        new_phrase+=phrase[ctr:ctr+length_of_word]
        #go backwards until you get to a letter again.
        while ctr-1>=0 and not phrase[ctr-1] in ltrs:
            ctr-=1
    return clean_word(phrase, word_level_palindromes)==clean_word(new_phrase, word_level_palindromes)
def easy_word_level_palindromes(phrase):
   """I guess it's not actually that many fewer lines, but it's soooo much easier"""
   #split the phrase into a list of words.
   list_of_words=phrase.split()
   i=0
   for word in list_of_words:
       list_of_words[i]=clean_word(word, word_level_palindromes)
       i+=1
   #the extended slice operator goes [start:stop:step] the step is backwards.
   return list_of_words[::-1]==list_of_words
again='y'
while again=='y' or again=='Y':
    print palindromecheck(raw_input("Input a phrase or word to be checked for real palindromeness\n"))
    print word_level_palindromes(raw_input("Input a phrase or word to be checked for word level palindromeness\n"))
    again=raw_input("Again? (y/n)\n")
