from weapon import Weapon
class Robot:
    def __init__ (self,name):
        self.mecha_ankylosaurus = name
        self.health_points = 100
        self.active_weapon = Weapon("Hammer Fist")
    def attack(self,dinosaur)-> None:
        dinosaur.health_points -= self.active_weapon