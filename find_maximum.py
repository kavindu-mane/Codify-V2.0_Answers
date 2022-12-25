def max(arr):
    max_value = 0
    for num in arr:
        try:
            if(int(num) > 0 and int(num) <= 100):
                if((int(num) > max_value)):
                    max_value = int(num)
            else:
                return "ERROR"
        except:
            return "ERROR"
    return max_value

try:
    iterations = int(input())
    if(iterations < 1 or iterations > 50):
        print("ERROR")
    else:
        for i in range(iterations):
            print(max(input().split(" ")))
except:
    print("ERROR")
