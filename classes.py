class character:
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.power = 40
    
    def pattack(self,zombie):
        zombie.hp -= self.power
        print(f"you attack ({zombie.name}) for {self.power} damage")
        if zombie.hp <= 0:
            print (f"you killed the zombie ({zombie.name})")
        return zombie
            
    def hp_up(self,hp):
        self.hp += hp
        return hp

    def drink(self,up):
        self.hp += up.hd
        print(f"you've just drunk {up.name} ")


class zombie:
    def __init__(self,name,hp,power):
        # self.zombies = []
        self.name = name
        self.hp = hp
        self.power = power
    # def add_zombie(self):
    #     zombies.append(self.zombies)
    
    # def get_zombie(self):
    #     return self.zombies

    def zattack(self, char):   
        char.hp -= self.power
        print(f"{self.name} attack you for {self.power} damage")
        if char.hp <= 0:
            print ("you're dead")
        return char


class hp_up1:
    def  __init__(self,name):
        self.name = name
        self.hd = 50

        
# zombies = Zombie_list() You need to create a Zombie_list class
# zombie2= zombie("zombie king", 70, 50)
# z=zombie("zom",10,30)
# z2=zombie("zobla",45,30)
# z1=zombie("cona",50,30)
# zombie.add_zombie(zombie2)
# zombie.add_zombie(z)
# zombie.add_zombie(z2)
# zombie.add_zombie(z1)

# print(zombie.get_zombie())


# char1 = character("d")
# zombie2= char1.pattack(zombie2)
# print(zombie2.hp)
# zombie2= char1.pattach(zombie2)
# print(zombie2.hp)
# zombie2= char1.pattach(zombie2)
# print(zombie2.hp)
# char1.hp_up(50)
# char1 = zombie2.zattack(char1)
# char1 = zombie2.zattack(char1)
# char1 = z.zattack(char1)
# print(char1.hp)
# print(zombie2.hp)
# z = char1.pattach(z)

        
# player1 = character("mo")
# chuj_jjug = player1.hp_up(50) # it just a number # return hp

# print(player1.hp)

# chug_jug = hp_up1("{Chug Jug}")


# char1 = character("d")

# char1.hp_up(50)
# print(f"char1  {char1.hp}")
# char1.drink(chug_jug)
# print(char1.hp)