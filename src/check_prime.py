#function to check if current number is prime
def check_Prime(i):
    if(i > 1):
        for j in range(2, i-1):
            if i % j == 0:
                 return False
        return True
    return False