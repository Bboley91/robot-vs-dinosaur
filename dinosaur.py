class Dinosaur:
    def __init__ (self,name):
        self.ankylosaurus = name
        self.attack_power = 20
        self.health_points = 125

    def attack(self,robot) -> None:
        robot.health_points -= self.attack_power