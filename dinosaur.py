class Dinosaur:
    def __init__ (self,name,health_points,attack_power):
        self.ankylosaurus = name
        self.dinosaur_attack_power = attack_power
        self.dinosaur_health_points = health_points

    def attack(self,robot) -> None:
        robot.robot_health_points -= self.dinosaur_attack_power
        return robot