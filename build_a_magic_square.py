def re_arrange(array):
    count = 10000
    all_posible_squares = [
                            [2 , 9 , 4 , 7 , 5 , 3 , 6 , 1 , 8],
                            [2 , 7 , 6 , 9 , 5 , 1 , 4 , 3 , 8],
                            [4 , 9 , 2 , 3 , 5 , 7 , 8 , 1 , 6],
                            [4 , 3 , 8 , 9 , 5 , 1 , 2 , 7 , 6],
                            [6 , 1 , 8 , 7 , 5 , 3 , 2 , 9 , 4],
                            [6 , 7 , 2 , 1 , 5 , 9 , 8 , 3 , 4],
                            [8 , 3 , 4 , 1 , 5 , 9 , 6 , 7 , 2],
                            [8 , 1 , 6 , 3 , 5 , 7 , 4 , 9 , 2]]
    
    for arr in all_posible_squares:
        temp_count = 0
        for k , j in zip(arr , array):
            temp_count += abs(k-j)
        if(temp_count < count):
            count = temp_count
    return count

array = []
for i in range(3):
    array += list(map(int , input().split(" ")))
print(re_arrange(array))
