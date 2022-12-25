default_array = [0 , 0 , 0 , 0 , 0 ]

def calculation(array):
    global default_array
        
    index = 0
    for x , y in zip(default_array , array):
        default_array[index] = x + y
        index += 1 
    
weeks = int(input())
for _ in range(weeks):
    calculation(list(map(int ,  input().split(" "))))

for i in range(len(default_array) -  1):
    print(default_array[i] , end = " ")
print(default_array[-1])

# Test case 0 (sample test case) has wrong output
