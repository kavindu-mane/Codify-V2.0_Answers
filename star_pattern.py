def pattern(rows):
    for i in range(rows):
        for _ in range(rows - i):
            print(" " , end= "")
        for _ in range(i+1):
            print("*" , end=" ")
        print("")
        
pattern(int(input()))
