from operator import attrgetter

class Users():
    def __init__ (self,x,y):
        self.name = x
        self.user_id = y

    def __repr__(self):  # Что означает __repr__
        return self.name + " : " + str(self.user_id)
users = [
    Users('Lebron',23), # Зачем в класс передавать значения?
    Users ('Kevin', 0),
    Users ('Russel', 0),
    Users ('Blake',32)
]

for user in sorted(users,key=attrgetter('user_id')):
    print(user)
