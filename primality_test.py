import random

def PrimeOrNot(num):
    if(num == 2 or num == 3):
        return "PRIME"
    elif(num < 2 or num % 2 == 0):
        return "NOT PRIME"
    else:
        # using Miller - Rubing test         
        k, m = 0, num - 1
        while m % 2 == 0:
            k += 1
            m //= 2
                
        for j in range(5):
            a = random.randrange(2 , num-1)
            b = pow(a,int(m),num)
            if(b == 1 or (b - num) == -1):
                continue
            for i in range(k-1):
                b = pow(b,2,num)
                if((b - num) == -1):
                    break
            else:
                return "NOT PRIME"
        return "PRIME"

print(PrimeOrNot(int(input())))
