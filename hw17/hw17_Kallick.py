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
def Function(wordlist):
    i=0
    length=len(wordlist)
    for n in 'abcdefghijklmnopqrstuvwxyz':
        fout=open(n+'.txt','w')
        write=fout.write
        #while the first letter of the word we are writing is correct
        try:
            while wordlist[i][0]==n:
                write(wordlist[i])
                i+=1
        except:
            pass
        fout.close()
Function(wordlist)
print time.time()-t1
