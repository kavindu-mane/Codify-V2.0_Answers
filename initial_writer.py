def initial_writer(array):
    return_name = ""
    for i in range(len(array) - 1):
        return_name += array[i][0].upper() + ". "
    return_name += array[-1][0].upper() + array[-1][1:].lower()
    
    return return_name

names_count = int(input())
for _ in range(names_count):
    print(initial_writer(input().split(" ")))
