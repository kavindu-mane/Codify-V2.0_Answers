def word_finder(word , sentences):
    sentences.replace(".", "")
    return sentences.split(" ").count(word)

try:
    count = int(input())
    for i in range(count):
        word = input()
        print(word_finder( word ,input()))
except:
    print("ERROR")
    
#test case 2 not match this solution
