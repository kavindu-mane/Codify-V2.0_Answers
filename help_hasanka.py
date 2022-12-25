def get_square_count(start , end):
    count = 0
    for i in range(start , end + 1):
        if((i**0.5).is_integer()):
            count += 1
    return count

cases = int(input())
for _ in range(cases):
    line = list(map(int , input().split(" ")))
    print(get_square_count(line[0] , line[1]))
    
#this solution not match for test case 2
