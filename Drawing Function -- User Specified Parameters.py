# Omar El-Sharif

def drawRectangle(color = "black", x = 0, y = 0, width = 30, height = 30):
    import turtle
    turtle.penup()
    turtle.goto(x+(width/2),y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.left(90)
    turtle.forward(height/2)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height/2)
    turtle.end_fill()
    turtle.hideturtle()

def drawCircle(color = "black", x = 0, y = 0, radius = 50):
    import turtle
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(radius)
    turtle.end_fill()
    turtle.hideturtle()

def main():
    import turtle
    color = input('Enter color of the rectangle: ')
    cx = int(input('Enter x center of the rectangle: '))
    cy = int(input('Enter y center of the rectangle: '))
    width = int(input('Enter width of the rectangle: '))
    height = int(input('Enter height of the rectangle: '))
    drawCircle()
    drawRectangle(color,cx,cy,width,height)

main()
