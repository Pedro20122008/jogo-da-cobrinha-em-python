import turtle
import random
import time
# Configurações
WIDTH, HEIGHT = 400, 400
SPEED = 0.1

# Criar a janela
win = turtle.Screen()
win.setup(WIDTH, HEIGHT)
win.bgcolor("white")
win.title("Snake Game")

# Criar a cobrinha
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()

# Criar a comida
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()

# Criar a lista de segmentos da cobrinha
segments = []

# Função para mover a cobrinha
def move_snake():
    x, y = snake.xcor(), snake.ycor()
    snake.forward(20)
    if snake.xcor() > WIDTH/2 or snake.xcor() < -WIDTH/2 or snake.ycor() > HEIGHT/2 or snake.ycor() < -HEIGHT/2:
        game_over()
    for segment in segments:
        if snake.distance(segment) < 10:
            game_over()

# Função para comer a comida
def eat_food():
    if snake.distance(food) < 10:
        food.goto(random.randint(-WIDTH/2, WIDTH/2), random.randint(-HEIGHT/2, HEIGHT/2))
        return True
    return False

# Função para game over
def game_over():
    win.clear()
    win.bgcolor("black")
    win.write("Game Over!", align="center", font=("Arial", 24, "bold"))
    win.update()

# Função para mover a cobrinha para cima
def up():
    snake.setheading(90)

# Função para mover a cobrinha para baixo
def down():
    snake.setheading(270)

# Função para mover a cobrinha para esquerda
def left():
    snake.setheading(180)

# Função para mover a cobrinha para direita
def right():
    snake.setheading(0)

# Bindings de teclado
win.listen()
win.onkey(up, "Up")
win.onkey(down, "Down")
win.onkey(left, "Left")
win.onkey(right, "Right")

# Inicializar a comida
food.goto(random.randint(-WIDTH/2, WIDTH/2), random.randint(-HEIGHT/2, HEIGHT/2))

# Loop principal
while True:
    move_snake()
    if eat_food():
        segments.append(turtle.Turtle())
        segments[-1].shape("square")
        segments[-1].color("green")
        segments[-1].penup()
        segments[-1].goto(snake.xcor(), snake.ycor())
    win.update()
    time.sleep(SPEED)