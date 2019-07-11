class Prent():

    def print_last_name(self):
        print("Phitzgerald")

class Child(Prent):
    def print_first_name(self):
        print("Ozi")

    def print_last_name(self):
        print("Gamburg")

David = Child()

David.print_first_name()
David.print_last_name()

