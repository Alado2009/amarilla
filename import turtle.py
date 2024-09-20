import turtle
import math


screen = turtle.Screen()
screen.bgcolor("black")


t = turtle.Turtle()
t.speed(0)

# Función para dibujar un pétalo
def dibujar_petalo(t, radio, angulo):
    for _ in range(4):
        t.circle(radio, angulo)
        t.left(180 - angulo)

# Dibuja el girasol
def girasol(t, numero_petalos):
    for _ in range(numero_petalos):
        dibujar_petalo(t, 100, 60)  # Pétalos de tamaño y forma definidos
        t.left(360 / numero_petalos)

# Dibuja el centro del girasol
def centro(t, radio):
    t.color("brown")
    t.begin_fill()
    t.circle(radio)
    t.end_fill()

# Dibujar el girasol completo
t.color("yellow")
girasol(t, 30)  # 36 pétalos
t.penup()
t.goto(0, -50)
t.pendown()
centro(t, 50)

# Ocultar la tortuga
t.hideturtle()

# Mantener la ventana abierta
screen.mainloop()