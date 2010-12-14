'''
File: hw19_Kallick.py
Author: Daniel Dyssegaard Kallick
Description:counts word frequency
'''
def word_frequency(filename):
    """Takes a filename(string) as a parameter, returns a dictionary of
    word frequencies"""
    fin=open(filename,'r')
    wordlist=fin.read().split()
    fin.close()
    wordfrequency={}
    #clean the list
    cleanwordlist=[]
    for word in wordlist:
        newword=''
        for letter in word:
            if letter.isalpha():
                newword+=letter
        newword=newword.lower()
        cleanwordlist.append(newword)
    #make the dictionary
    for word in cleanwordlist:
        if word in wordfrequency:
            wordfrequency[word]+=1
        else:
            wordfrequency[word]=1
    return wordfrequency

###################################################
###############good code for testing###############
###################################################

#output=word_frequency('moby_dick.txt')
#print 'sperm',output['sperm']

#output=word_frequency('moby_dick.txt').items()
#output.sort(key=lambda x: x[1],reverse=True)
#topwords=output[:200]
#for word in topwords:
#    print word
