# Omar El-Sharif


def getPentagonalNumber(n):
    split = -9 
    for i in range(1,n+1):
        
        n = i*(3*i - 1)/2
        n = int(n)
        n = '{:6}'.format(n) 
        print(n, end = ' ')
    
        if split %10 ==0:
            print("  ")
        split += 1

    

def main(n):
    getPentagonalNumber(n)

    
        
        

main(100)







