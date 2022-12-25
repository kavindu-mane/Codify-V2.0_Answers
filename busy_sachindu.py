def function(word):
    array1 =[]
    array2 =[]
    for i in range(len(word) - 1):
        array1.append(abs(ord(word[i]) - ord(word[i+1])))
    word.reverse()
    for i in range(len(word) - 1):
        array2.append(abs(ord(word[i]) - ord(word[i+1])))
    if(array1 == array2):
        return "FUNNY WORD"
    else:
        return "COMPLEX"
    
word_count = int(input())
for _ in range(word_count):
    print(function(list(input())))
