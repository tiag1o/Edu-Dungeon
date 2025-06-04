"""Voorraadgegevens voor de winkels in het spel."""

# Standaard items die in het gemengde eiland verkrijgbaar zijn.
basis_winkelvoorraad = [
    {"naam": "Hint Token", "prijs": 5},
    {"naam": "Volgende Vraag", "prijs": 7},
    {"naam": "Zwaard van Versimpeling", "prijs": 15},
    {"naam": "Schild van Substitutie", "prijs": 12},
    {"naam": "Amulet der Antwoorden", "prijs": 20},
    {"naam": "Wortelhelm", "prijs": 10},
    {"naam": "Toverstaf van Herleiding", "prijs": 17},
    {"naam": "Scroll van Skippen", "prijs": 8},
    {"naam": "Breukenbreker", "prijs": 14},
    {"naam": "Ring der Rekenregels", "prijs": 9},
    {"naam": "Ketting van Ketenregels", "prijs": 16},
    {"naam": "Elixer van Exactheid", "prijs": 6},
    {"naam": "Boek der Buigpunten", "prijs": 18},
    {"naam": "Kap van Kwadraten", "prijs": 11},
    {"naam": "Sceptor van Stelsels", "prijs": 13}
]

# Unieke items per eiland. Elke lijst bevat voorbeelden uit de
# categorieën wapens, voedsel, trinkets, armor en draken.
eiland_winkels = {
    "limitanie": [
        {"naam": "Limiet-Zwaard", "prijs": 25, "categorie": "wapens"},
        {"naam": "Oneindige Appel", "prijs": 3, "categorie": "voedsel"},
        {"naam": "Grenzeloos Amulet", "prijs": 12, "categorie": "trinkets"},
        {"naam": "Eindhelm", "prijs": 18, "categorie": "armor"},
        {"naam": "Baby Delta Draak", "prijs": 100, "categorie": "draken"},
    ],
    "integralia": [
        {"naam": "Integratie-Bijl", "prijs": 28, "categorie": "wapens"},
        {"naam": "Riemann-Rooster", "prijs": 4, "categorie": "voedsel"},
        {"naam": "Oploskraal", "prijs": 10, "categorie": "trinkets"},
        {"naam": "Differentiaal Pants", "prijs": 22, "categorie": "armor"},
        {"naam": "Integrale Draak", "prijs": 120, "categorie": "draken"},
    ],
    "logaritmie": [
        {"naam": "Log-Zwaard", "prijs": 22, "categorie": "wapens"},
        {"naam": "Exp Brood", "prijs": 5, "categorie": "voedsel"},
        {"naam": "Tienlog Talisman", "prijs": 9, "categorie": "trinkets"},
        {"naam": "Logschild", "prijs": 17, "categorie": "armor"},
        {"naam": "Log Draak", "prijs": 150, "categorie": "draken"},
    ],
    "pimania": [
        {"naam": "Pi-lan", "prijs": 20, "categorie": "wapens"},
        {"naam": "Taart π", "prijs": 7, "categorie": "voedsel"},
        {"naam": "Cirkelhanger", "prijs": 8, "categorie": "trinkets"},
        {"naam": "Radius Pants", "prijs": 12, "categorie": "armor"},
        {"naam": "Pi Draak", "prijs": 140, "categorie": "draken"},
    ],
    "cirkelosio": [
        {"naam": "Compas-Zwaard", "prijs": 23, "categorie": "wapens"},
        {"naam": "Donut", "prijs": 4, "categorie": "voedsel"},
        {"naam": "Hoekige Ketting", "prijs": 11, "categorie": "trinkets"},
        {"naam": "Cirkelharnas", "prijs": 19, "categorie": "armor"},
        {"naam": "Hoepel Draak", "prijs": 160, "categorie": "draken"},
    ],
    # Gemengd krijgt alle standaard items plus een selectie van de andere
    # eilanden zodat er altijd iets beschikbaar is.
    "gemengd": basis_winkelvoorraad,
}

