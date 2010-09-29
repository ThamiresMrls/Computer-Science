def backwards(string):
    i=len(string)
    while i>0:
        letter = string[i-1]
        print letter
        i-=1
def find(word, letter, begin):
    index = begin
    while index < len(word):
        if word[index]==letter:
            return index
        index+=1
    return -1
def counter(word, letter):
    count =0
    for l in word:
        if l==letter:
            count+=1
    print count
counter('hippopotamus', 'o')
def chop(list):
    f=len(list)
    del list[0]
    del list[f-2]
