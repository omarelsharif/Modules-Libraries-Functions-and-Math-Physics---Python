# Omar El-Sharif

def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    if (x1 - x0)*(y2-y0) - (x2-x0) * (y1-y0) > 0:
        return True

def onTheSameLine(x0, y0, x1, y1, x2, y2):
    if (x1 - x0)*(y2-y0) - (x2-x0) * (y1-y0) == 0:
        return True

def rightOfTheLine(x0, y0, x1, y1, x2, y2):
    if (x1 - x0)*(y2-y0) - (x2-x0) * (y1-y0) < 0:
        return True

def main():
    print('Enter coordinates for the three points p0, p1 and p2: ')
    x0 = float(input()) # Getting float inputs for the points 
    y0 = float(input())
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    if leftOfTheLine(x0, y0, x1, y1, x2, y2):
        print('({0:.1f},{1:.1f}) is on the left side of the line from ({2:.1f},{3:.1f}) to ({4:.1f},{5:.1f})'.format(x2,y2,x0,y0,x1,y1))
    elif onTheSameLine(x0, y0, x1, y1, x2, y2):
        print('({0:.1f},{1:.1f}) is on the same line from ({2:.1f},{3:.1f}) to ({4:.1f},{5:.1f})'.format(x2,y2,x0,y0,x1,y1))
    elif rightOfTheLine(x0, y0, x1, y1, x2, y2):
        print('({0:.1f},{1:.1f}) is on the right side of the line from ({2:.1f},{3:.1f}) to ({4:.1f},{5:.1f})'.format(x2,y2,x0,y0,x1,y1))

main()   
