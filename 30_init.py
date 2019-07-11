class Enemy:
    def __init__(self, x):
        self.energyammount = x

    def get_energy (self):
        print(self.energyammount)

trooper = Enemy(1)
jason = Enemy(3000)

trooper.get_energy()
jason.get_energy()