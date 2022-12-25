import random

def prime_or_not(num):
    if(num == 1 or num == 2 or num == 3):
        return True
    elif(num % 2 == 0):
        return False
    else:
        # using Miller - Rubing test         
        k, m = 0, num - 1
        while m % 2 == 0:
            k += 1
            m //= 2
                
        for j in range(5):
            a = random.randrange(2 , num -1)
            b = pow(a,int(m),num)
            if(b == 1 or (b - num) == -1):
                continue
            for i in range(k-1):
                b = pow(b,2,num)
                if((b - num) == -1):
                    break
            else:
                return False
        return True

def calculate_secret_number(n , k):
    test_value = n if n > k else k
    while True:
        facters = []
        count = 1
        test_value += 1
        
        for i in range(1 , test_value +1):
            if(test_value % i == 0):
                facters.append(i)
        for num in facters:
            if(prime_or_not(num)):
                count *= num
        if(count > k):
            return test_value
    
lines = int(input())
for k in range(lines):
    line = list(map(int , input().split(" ")))
    print(calculate_secret_number(line[0] , line[1]))
