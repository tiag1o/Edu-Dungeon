class Monster:
    def __init__(self, naam, vraag_index, goud, loot, xp):
        self.naam = naam
        self.vraag_index = vraag_index
        self.verslagen = False
        self.goud = goud
        self.loot = loot
        self.xp = xp

    def geef_vraag(self, vragenlijst):
        return vragenlijst[self.vraag_index]


class BossMonster(Monster):
    """Speciale monsterklasse voor bazen."""

    def __init__(self, naam, vraag_indices, goud, loot, xp, special_item):
        super().__init__(naam, vraag_indices[0], goud, loot, xp)
        self.vraag_indices = vraag_indices
        self.special_item = special_item
        self.progress = 0
        self.is_boss = True

    def geef_vraag(self, vragenlijst):
        index = self.vraag_indices[self.progress]
        return vragenlijst[index]
monsterlijst = [
    Monster("Algebraïsche Gier", 0, 10, "Roestig Zwaard van Rekenkracht", 10),
    Monster("Haakjes-Hydra", 1, 15, "Verdedigende Breukenschild", 12),
    Monster("Wortel-Worm", 2, 12, "Scherpe Wortelsnijder", 14),
    Monster("Tangens-Trol", 3, 18, "Hoekige Helm van π", 16),
    Monster("Exponentiële Eekhoorn", 4, 20, "e-macht Excalibur", 18),
    Monster("Delta-Draak", 5, 25, "Driehoeks-Talisman", 20),
    Monster("Logaritmische Leeuw", 6, 22, "Logboek der Macht", 22),
    Monster("Matrix-Mammoet", 7, 28, "Determinant-Harnas", 24),
    Monster("Breuken-Basilisk", 8, 16, "Splijtende Staf van Vereenvoudiging", 26),
    Monster("Negatieve Naga", 9, 14, "Machteloos Medaillon", 28),
    Monster("Kettingslang", 10, 30, "Afgeleide Drietand", 30),
    Monster("Limieten-Lykanthroop", 11, 27, "Oneindige Maanring", 32),
    Monster("Parabool-Phoenix", 12, 35, "Toppunt Tiara", 34),
    Monster("Sinus-Sfinx", 13, 19, "Oscillerende Orakelsteen", 36),
    Monster("Raaklijn-Raaf", 14, 21, "Tangentiële Talon", 38),
    Monster("Gemene Middel-Manticore", 15, 23, "Aritmetisch Amulet", 40),
    Monster("Gelijkheids-Golem", 16, 17, "Evenwichtsbijl", 42),
    Monster("Differentiaal-Djinn", 17, 33, "Veranderlijkheidsvlam", 44),
    Monster("Kwadraat-Kraken", 18, 40, "Vierkantswortelvizier", 46),
    Monster("Oplos-Oger", 19, 24, "X-mark Zwaard", 48),

]

# Voeg drie bazen toe die meerdere vragen vereisen
monsterlijst.extend([
    BossMonster(
        "Kwadratuur Koning",
        [0, 1, 2],
        100,
        "Kroon der Congruentie",
        100,
        "Kroon Sleutel",
    ),
    BossMonster(
        "Integrale Ifrit",
        [3, 4, 5],
        150,
        "Vlam van Volledigheid",
        150,
        "Ifrit Amulet",
    ),
    BossMonster(
        "Logaritmische Lord",
        [6, 7, 8],
        200,
        "Scepter der Schalen",
        200,
        "Log Sleutel",
    ),
])
