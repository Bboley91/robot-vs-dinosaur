from weapon import Weapon
class Robot:
    def __init__ (self,name,health_points):
        self.mecha_ankylosaurus = name
        self.robot_health_points = health_points
        self.active_weapon = Weapon("Hammer Fist")
    def attack(self,dinosaur)-> None:
        dinosaur.health_points -= self.active_weapon.attack_power
        return dinosaur