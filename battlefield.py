from robot import Robot
from dinosaur import Dinosaur
class Battlefield:
    def __init__ (self):
        self.location = "A crater"

    def run_game(self) -> None:
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self) -> None:
        print("Our match begins with ankylosaurus facing off aginst mecha ankylosaurus!")
        print("The battle begins in",{self.location})

    def battle_phase(self) -> None:
        



    def display_winner(self) -> None:
