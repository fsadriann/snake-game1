import turtle
import time

posponer = 0.1


# configuramos la ventana
window = turtle.Screen()
window.title("Snake 1")
window.bgcolor("gray5")
window.setup(width=500, height=500)
window.tracer(0)

 # cabeza serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"

#funciones
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#teclado
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
    

#creamos el bucle principal
while True:
    window.update()

    mov()
    time.sleep(posponer)
