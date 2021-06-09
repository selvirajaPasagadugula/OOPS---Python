class Player:
    teamName = 'India'
    teamMembers = []
    # here we are able to access the teamMembers why can't we access it inside __init__ method
    print(teamMembers)

    def __init__(self, name):
        self.name = name
        # why do we need self.teamMembers here why teamMembers is not enough
        self.teamMembers.append(self.name)


p1 = Player('KL Rahul')
p2 = Player('Mohammad Siraj')

print(p1.name)
print(p2.name)
print(Player.teamMembers)
print(p1.teamMembers)
print(p2.teamMembers)
