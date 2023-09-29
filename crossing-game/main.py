import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.creat_car()
    car_manager.move_car()

    for car in car_manager.all_car:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False
    if player.win():
        player.go_to_start()
        car_manager.level_up()
        score.level_up()


screen.exitonclick()

