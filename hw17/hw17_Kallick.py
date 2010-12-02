'''
File: hw17.py
Author: Daniel Dyssegaard Kallick
Description: goes through words.txt, creates alphabetized files
'''
import time
t1=time.time()
fin=open('words.txt','r')
#make a list of words from words.txt by reading line by line
wordlist=fin.readlines()
fin.close()

i=0
length=len(wordlist)
for n in range(26):
    fout=open(chr(n+97)+'.txt','w')
    #while the first letter of the word we are writing is correct
    while wordlist[i][0]==chr(n+97):
        #write the word
        fout.write(wordlist[i])
        #if we are not at the end of the file
        if i<length-1:
            #go to the next word
            i+=1
        #if we are at the end of the file
        else:
            #stop
            break
    fout.close()
t2=time.time()
print t2-t1
