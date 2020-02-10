
class Lifter:
    def __init__(self, name, snatch, cj, biatlon):
        self.name = name
        self.snatch = snatch
        self.cj = cj
        self.biatlon = biatlon

    def make_lifter(name, snatch, cj):

        biatlon_cal = int(snatch) + int(cj)
        lifter = Lifter(name, str(snatch), str(cj), str(biatlon_cal))
        return lifter




