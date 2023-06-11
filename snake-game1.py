import turtle
import time
import random

posponer = 0.1
# marcador
score = 0
high_score = 0

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

#comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# cuerpo serpiente
body = []

# texto
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,210)
text.write("Score: 0  High Score: 0", align="center", font=("courier",20, "normal"))

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

    # colision bordes
    if head.xcor() > 230 or head.xcor() < -230 or head.ycor() > 290 or head.ycor()< -230:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        # eliminar cuerpo
        for new_body in body:
            new_body.goto(1000,1000)

        # limpiar lista
        body.clear()
        #resetear marcador
        score = 0
        text.clear()
        text.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier",20, "normal"))

    # colision comida
    if head.distance(food)<20:
        # mover la comida a un lugar random
        x=random.randint(-230,230)
        y=random.randint(-230,230)
        food.goto(x,y)

        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("yellow green")
        new_body.penup()
        body.append(new_body)

        # aumentar marcador
        score +=10
        if score > high_score:
            high_score = score
        text.clear()
        text.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier",20, "normal"))

    #mover cuerpo
    totalBody = len(body)
    for i in range(totalBody-1,0,-1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    if totalBody > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    mov()

    # colisiones con el cuerpo
    for new_body in body:
        if new_body.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # eliminar cuerpo
            for new_body in body:
                new_body.goto(1000,1000)

            # limpiar lista
            body.clear()

            #resetear marcador
            score = 0
            text.clear()
            text.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier",20, "normal"))
    time.sleep(posponer)
