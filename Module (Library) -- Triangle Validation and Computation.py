
# Omar El-Sharif

def isValid(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
        
        return True 
    else:
        return False 
    
def area(side1, side2, side3):
    s = (side1+ side2 + side3)/2
    area = (s*(s-side1)*(s-side2)*(s-side3))**(1/2)
    return area 
