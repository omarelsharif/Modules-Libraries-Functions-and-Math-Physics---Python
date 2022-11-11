# Omar El-Sharif


def falling_distance(t):
    g = 9.8
    t = t**2
    d = (1/2) * (g*t)
    return d 


def main(n):
    print ("Time	   Falling Distance")
    print("---------------------------")
    
    for i in range(1,n+1):
        x = falling_distance(i)
        
        
        print ('{0:<10}'.format(i), '{0:<10.2f}'.format(x) )


main(10)
