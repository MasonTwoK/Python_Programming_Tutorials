class Some_class:

    amount_of_life = 3

    def strike (self):
        print('aiaiai!')
        self.amount_of_life -= 1

    def life_counter(self):
        if self.amount_of_life <= 0:
            print("You are dead")
        else:
            print("You life = " + str(self.amount_of_life))

badguy1 = Some_class()

badguy1.strike()
badguy1.life_counter()
