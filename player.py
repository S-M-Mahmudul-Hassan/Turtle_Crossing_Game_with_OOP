from turtle import Turtle

# Global variables
STARTING_POSITION = (0, -310)
MOVE_DISTANCE = 13
FINISH_LINE_Y = 290


class Player(Turtle):
    """Class to create player object."""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("DarkGreen")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        """Method for up motion."""
        self.forward(MOVE_DISTANCE)

    def down(self):
        """Method for down motion."""
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        """Method for reset position upon one level completion."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Finish sequence to compelte one level."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
