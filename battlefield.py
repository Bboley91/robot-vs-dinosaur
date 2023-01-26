from robot import Robot
from dinosaur import Dinosaur
class Battlefield:
    def __init__ (self):
        self.location = "A crater"
        self.robot = Robot("mecha ankylosaurus",100)
        self.dinosaur = Dinosaur("ankylosaurus",125,20)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Our match begins with",{self.dinosaur},"facing off aginst",{self.robot},"!")
        print("The battle begins in",{self.location})

    def battle_phase(self):
        self.robot.attack(self.dinosaur)
        self.dinosaur.attack(self.robot)
        



    def display_winner(self):
        if self.robot.robot_health_points == 0:
            print({self.dinosaur}," is the winner!")
        elif self.dinosaur.dinosaur_health_points == 0:
            print({self.robot}," is the winner!")

