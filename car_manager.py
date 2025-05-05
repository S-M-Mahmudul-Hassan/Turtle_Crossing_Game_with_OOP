from turtle import Turtle, Screen
from PIL import Image
import random

# Global variables
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 8
MOVE_INCREMENT = 7

# image size modification steps
image = Image.open("car_image_for_turtle_crossing_game.gif")
width, height = image.size
new_width = width // 8
new_height = height // 8
resized_image = image.resize((new_width, new_height))
resized_image.save("resized_car_image_for_turtle_crossing.gif", optimize=True, quality=60)

# registration of car for object shape
screen=Screen()
screen.register_shape("resized_car_image_for_turtle_crossing.gif")


class CarManager(Turtle):
    """Class for creating car object."""

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Method for creating car randomly along y-axis."""
        random_chance = random.randint(1, 12)
        if random_chance == 5:
            new_car = Turtle()
            new_car.shape("resized_car_image_for_turtle_crossing.gif")
            new_car.shapesize(stretch_wid=0.007, stretch_len=0.007)
            new_car.penup()
            # new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 265)
            new_car.goto(500, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        """Method to move all the cars at the same time upon car object creation."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Method to increase car speeds upon level completion."""
        self.car_speed += MOVE_INCREMENT



