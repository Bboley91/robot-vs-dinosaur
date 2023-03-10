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
        print(f"Our match begins with",self.dinosaur.ankylosaurus,"facing off aginst",self.robot.mecha_ankylosaurus,"!")
        print(f"The battle begins in",self.location)

    def battle_phase(self):
        while (self.dinosaur.dinosaur_health_points >= 0 and self.robot.robot_health_points >= 0):
            print(f"mecha ankylosaurus' health is at: {self.robot.robot_health_points}")
            print(f"ankylosaurus' health is at: {self.dinosaur.dinosaur_health_points}")
            print(f"{self.robot.mecha_ankylosaurus} attacked {self.dinosaur.ankylosaurus} with {self.robot.active_weapon.name} doing {self.robot.active_weapon.attack_power} damage!")
            self.robot.attack(self.dinosaur)
            print(f"{self.dinosaur.ankylosaurus} attacked {self.robot.mecha_ankylosaurus} doing {self.dinosaur.dinosaur_attack_power} damage!")
            self.dinosaur.attack(self.robot)
            if self.dinosaur.dinosaur_health_points == 0:
                print(f"Mecha ankylosaurus' health is at: {self.robot.robot_health_points}")
                print(f"Ankylosaurus' health is at: {self.dinosaur.dinosaur_health_points}")
                break
            elif self.robot.robot_health_points == 0:
                print(f"Mecha ankylosaurus' health is at: {self.robot.robot_health_points}")
                print(f"Ankylosaurus' health is at: {self.dinosaur.dinosaur_health_points}")
                break



    def display_winner(self):
        if self.robot.robot_health_points == 0:
            print(self.dinosaur.ankylosaurus," is the winner!")
        elif self.dinosaur.dinosaur_health_points == 0:
            print(self.robot.mecha_ankylosaurus," is the winner!")

