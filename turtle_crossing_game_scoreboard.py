from turtle import Turtle


class Scoreboard(Turtle):
    """Scoreboard for the game."""

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-70, 300)
        self.update_scoreboard()

    def update_scoreboard(self):
        """method to update the scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "bold"))

    def level_up(self):
        """Increases the level once player finishes one level."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Game over sequence."""
        self.goto(0,0)
        self.color("red")
        self.write("Game Over", align="center", font=("Courier", 35, "bold"))



