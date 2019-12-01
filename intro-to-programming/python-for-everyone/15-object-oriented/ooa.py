class PartyAnimal:
    """
    class PartyAnimal, sample for learning object oriented python.
    """
    x = 0
    name = ""

    def __init__(self, name):
        self.name = name
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

    def __del__(self):
        print("I am destructed", self.x)


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)


an = PartyAnimal("Sunil")

an.party()
an.party()
an.party()

fn = FootballFan("Udupi")
fn.party()
