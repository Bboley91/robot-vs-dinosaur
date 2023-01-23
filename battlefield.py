from robot import Robot
from dinosaur import Dinosaur
class Battlefield:
    def __init__ (self):
        self.location = "A crater"
        self.robot = Robot("mecha ankylosaurus")
        self.dinosaur = Dinosaur("ankylosaurus")

    def run_game(self) -> None:
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Our match begins with",{self.dinosaur},"facing off aginst",{self.robot},"!")
        print("The battle begins in",{self.location})

    def battle_phase(self) -> None:
        self.robot.attack(self.dinosaur)
        self.dinosaur.attack(self.robot)
        



    def display_winner(self) -> None:
        if self.robot.health_points >= 0:
            print({self.dinosaur}," is the winner!")
        else:
            print({self.robot}," is the winner!")

