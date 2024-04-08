import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Race")
screen.setup(width=1000, height=800)

screen.bgcolor("black")

start = screen.textinput("welcome to the game!", "which turtle do you think will win? red, yellow, gray, green, orange or brown?")


turtles = []
color_of_turtles = ["green", "red", "yellow", "orange", "gray", 'brown']
location_of_turtles = [300, 200, 100, 0, -100, -200]

for i in range(6):
    tim = turtle.Turtle()
    tim.shape('turtle')
    tim.color(color_of_turtles[i])
    tim.penup()
    tim.setposition(-300, location_of_turtles[i])
    turtles.append(tim)


for j in range(100):
    for i in range(6):
        number = random.randint(10, 100)
        turtles[i].forward(number)
        if turtles[i].xcor() > 330:

            if turtles[i].fillcolor() == start:
                print("you won!")
            else:
                print("you lost!")
            screen.bye()

screen.mainloop()
# when the program ends, scroll up, And you will see did you win or not.
