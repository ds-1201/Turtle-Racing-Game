import turtle as t
import random
import tkinter.messagebox

screen = t.Screen()

screen.setup(width=500, height=400)
screen.title("Get Set Gooo!!!")
user_bet = screen.textinput(title="Place your BET!!", prompt="Enter the color of turtle you place your bet on ").lower()

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_postions = [-150, -100, -50, 0, 50, 100, 150]
racers = []
game_start = False

for number in range(7):
    racer = t.Turtle()
    racer.shape("turtle")
    racer.penup()
    racer.color(colors[number])
    racer.goto(-230, y_postions[number])
    racer.speed("slowest")
    racers.append(racer)

if user_bet:
    game_start = True

while game_start:
    for racer in racers:
        random_distance = random.randint(1, 10)
        if racer.xcor() > 230:
            winner = racer.fillcolor()
            if winner == user_bet:
                tkinter.messagebox.showinfo("Winner Of Race", f"You Win, The winner is {winner} turtle")
            else:
                tkinter.messagebox.showinfo("Winner Of Race", f"You Lose, The winner is {winner} turtle")
            game_start = False
            break
        racer.fd(random_distance)

screen.exitonclick()