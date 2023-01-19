from weapon import Weapon
class Robot:
    def __init__ (self,name,health_points,active_weapon):
        self.mecha_ankylosaurus = name
        self.health_points = 100
        self.active_weapon = Weapon
    def attack(self,dinosaur)-> None:
        dinosaur.health_points -= self.active_weapon