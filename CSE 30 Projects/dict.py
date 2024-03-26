def make_dict(x):
    mydict = {}
    len_words=[]
    mydict[10] = []
    for i in x:
        l=len(i)
        if l in len_words or l > 10:
            continue
        else:
            len_words.append(l)
    for i in len_words:
        mydict[i] = []
    for i in range(len(x)):
        f=len(x[i])
        if f>10:
            f=10
        mydict[f].append(x[i])
    return mydict
        

if __name__ == '__main__':
    
    d = {2: ['at', 'to', 'no'], 3: ['add', 'sun'], 10: ['Hello! How are you?']}
    dictionary = make_dict(['at', 'add', 'sun', 'to', 'no', 'Hello! How are you?'])
    print (dictionary)
    assert dictionary == d
    print('Everything works correctly!')
