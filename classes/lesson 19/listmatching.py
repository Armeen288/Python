def matchwords(words):
    ctr= 0
    lst= []
    for word in words:
        if len(word) > 1 and word[0]==word[-1]:
            ctr +=1
            lst.append(word)
            print("List of matching characcters: ", lst)
            return ctr
count=matchwords(['aba','xyz','aa', 'x', 'bbb'])
print("Number of words matching are: ", count)