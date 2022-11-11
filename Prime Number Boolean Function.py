# Omar El-Sharif

def is_prime(n):
    factors = 0 
    for i in range (1,n+1):
        if n%i == 0:
            factors +=1
    if factors/2== 1:
        return True
    else:
        return False



def main():
    i = int(input("Enter an integer: "))
    if is_prime(i) == True:
        print ("The number you entered is a prime number.")
    else:
        print("The number you entered is not a prime number.")

main()
