class Town:
    'Base class for Towns'
    townCount = 0

    def __init__(self, name, faction, size, climate, threat):
        self.name = name
        self.faction = faction
        self.size = size
        self.climate = climate
        self.threat = threat
        Town.townCount += 1

    def displayCount(self):
        print("Total Towns %d" % Town.townCount)

    def displayTown(self):
        print("Name: ", self.name,
              ", Faction: ", self.faction,
              ", Size: ", self.size,
              ", Climate: ", self.climate,
              ", Threat: ", self.threat)


