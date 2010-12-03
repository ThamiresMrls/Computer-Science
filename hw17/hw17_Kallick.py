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
    currentletter=chr(n+97)
    fout=open(chr(n+97)+'.txt','w')
    #while the first letter of the word we are writing is correct
    try:
        while wordlist[i][0]==currentletter:
            fout.write(wordlist[i])
            i+=1
    except:
        pass
    fout.close()
print time.time()-t1
