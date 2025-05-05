import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from turtle_crossing_game_scoreboard import Scoreboard

# screen created
screen = Screen()
screen.setup(width=700, height=800)
screen.bgpic("road_image_for_turtle_game.gif")
screen.tracer(0)

# Player turtle created
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Screen is listening for up & down keys
screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
