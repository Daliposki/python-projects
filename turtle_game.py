import turtle
import random

screen = turtle.Screen()
screen.title("Trka zo zelki")
screen.setup(width=1000, height=800)

screen.bgcolor("black")

start = screen.textinput("dobredojde v igra!", "sto mislis koja zelka ke pobedi?")


zelki = []
boja_na_zelki = ["green", "red", "yellow", "orange", "gray", 'brown']
lokacija_na_zelki = [300, 200, 100, 0, -100, -200]

for i in range(6):
    tim = turtle.Turtle()
    tim.shape('turtle')
    tim.color(boja_na_zelki[i])
    tim.penup()
    tim.setposition(-300, lokacija_na_zelki[i])
    zelki.append(tim)


for j in range(100):
    for i in range(6):
        broj = random.randint(10, 100)
        zelki[i].forward(broj)
        if zelki[i].xcor() > 330:

            if zelki[i].fillcolor() == start:
                print("pobedivtre")
            else:
                print("izgubivte")
            screen.bye()

screen.mainloop()
