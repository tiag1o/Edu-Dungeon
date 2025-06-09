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

# Speciale items om bazen te verslaan
basis_winkelvoorraad.extend([
    {"naam": "Kroon Sleutel", "prijs": 50},
    {"naam": "Ifrit Amulet", "prijs": 70},
    {"naam": "Log Sleutel", "prijs": 90},
])

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

# ------------------------------------------------------------
# Itemeffecten definiëren

import re
from fractions import Fraction

try:
    from sympy import symbols, sympify, simplify, expand
except Exception:  # sympy optioneel
    sympify = simplify = expand = lambda x: x
    symbols = lambda x: x


def gebruik_hint_token(game):
    """Geef de hint van de huidige vraag."""
    game.feedback = f"💡 Hint: {game.vraag.get('hint', '')}"


def gebruik_volgende_vraag(game):
    """Sla de huidige vraag over."""
    game.feedback = "⏭️ Volgende vraag!"
    game.volgende_monster()


def gebruik_zwaard_versimpeling(game):
    """Probeer de uitdrukking in de vraag te versimpelen."""
    m = re.search(r":\s*(.*)", game.vraag.get("vraag", ""))
    if m:
        expr = m.group(1)
        try:
            game.feedback = f"🤺 Versimpeld: {simplify(sympify(expr))}"
        except Exception:
            game.feedback = "🤺 Kan niet versimpelen."
    else:
        game.feedback = "🤺 Geen uitdrukking gevonden."


def gebruik_schild_substitutie(game):
    """Laat de uitdrukking zien voor x=1."""
    m = re.search(r":\s*(.*)", game.vraag.get("vraag", ""))
    if m:
        expr = m.group(1)
        try:
            x = symbols("x")
            waarde = sympify(expr).subs(x, 1)
            game.feedback = f"🛡️ x=1 ⇒ {waarde}"
        except Exception:
            game.feedback = "🛡️ Kan niet substitueren."
    else:
        game.feedback = "🛡️ Geen uitdrukking gevonden."


def gebruik_amulet_antwoorden(game):
    """Toon direct het antwoord."""
    game.feedback = f"🔮 Antwoord: {game.vraag.get('antwoord', '')}"


def gebruik_wortelhelm(game):
    """Bereken een eenvoudige wortel in de vraag."""
    m = re.search(r"√\((\d+)\)", game.vraag.get("vraag", ""))
    if m:
        import math
        waarde = int(m.group(1))
        game.feedback = f"🪖 √{waarde} = {int(math.sqrt(waarde))}"
    else:
        game.feedback = "🪖 Geen wortel gevonden."


def gebruik_toverstaf_herleiding(game):
    """Voer een herleiding/expand uit op de uitdrukking."""
    m = re.search(r":\s*(.*)", game.vraag.get("vraag", ""))
    if m:
        expr = m.group(1)
        try:
            game.feedback = f"✨ Herleiding: {expand(sympify(expr))}"
        except Exception:
            game.feedback = "✨ Kan niet herleiden."
    else:
        game.feedback = "✨ Geen uitdrukking gevonden."


def gebruik_scroll_skippen(game):
    """Skip de vraag zonder straf."""
    game.feedback = "⏭️ Vraag geskipt!"
    game.volgende_monster()


def gebruik_breukenbreker(game):
    """Vereenvoudig een breuk in de vraag."""
    m = re.search(r"(\d+)/(\d+)", game.vraag.get("vraag", ""))
    if m:
        breuk = Fraction(int(m.group(1)), int(m.group(2)))
        game.feedback = f"⚔️ Vereenvoudigd: {breuk}"
    else:
        game.feedback = "⚔️ Geen breuk gevonden."


def gebruik_ring_rekenregels(game):
    """Geef een algemene rekenregel."""
    game.feedback = "🔔 Somregel: (f+g)' = f' + g'"


def gebruik_ketting_ketenregels(game):
    """Herinner aan de kettingregel."""
    game.feedback = "⛓️ (f(g(x)))' = f'(g(x)) * g'(x)"


def gebruik_elixer_exactheid(game):
    """Vergelijk huidige invoer met het antwoord."""
    antw = game.vraag.get("antwoord", "").replace(" ", "").lower()
    invoer = game.invoer.replace(" ", "").lower()
    if invoer == antw:
        game.feedback = "🥤 Exact goed!"
    else:
        game.feedback = f"🥤 Bijna! Correct is {game.vraag.get('antwoord', '')}"


def gebruik_boek_buigpunten(game):
    """Korte tip over buigpunten."""
    game.feedback = "📚 Tip: zoek waar f''(x) = 0"


def gebruik_kap_kwadraten(game):
    """Herinner aan het kwadraat van een som."""
    game.feedback = "🎩 (a+b)^2 = a^2 + 2ab + b^2"


def gebruik_sceptor_stelsels(game):
    """Geef een tip voor lineaire stelsels."""
    game.feedback = "⚖️ Gebruik substitutie of eliminatie bij stelsels"


item_effects = {
    "Hint Token": gebruik_hint_token,
    "Volgende Vraag": gebruik_volgende_vraag,
    "Zwaard van Versimpeling": gebruik_zwaard_versimpeling,
    "Schild van Substitutie": gebruik_schild_substitutie,
    "Amulet der Antwoorden": gebruik_amulet_antwoorden,
    "Wortelhelm": gebruik_wortelhelm,
    "Toverstaf van Herleiding": gebruik_toverstaf_herleiding,
    "Scroll van Skippen": gebruik_scroll_skippen,
    "Breukenbreker": gebruik_breukenbreker,
    "Ring der Rekenregels": gebruik_ring_rekenregels,
    "Ketting van Ketenregels": gebruik_ketting_ketenregels,
    "Elixer van Exactheid": gebruik_elixer_exactheid,
    "Boek der Buigpunten": gebruik_boek_buigpunten,
    "Kap van Kwadraten": gebruik_kap_kwadraten,
    "Sceptor van Stelsels": gebruik_sceptor_stelsels,
}


def gebruik_item(game, item):
    """Gebruik een item en verwijder het uit de inventaris."""
    func = item_effects.get(item.get("naam"))
    if func:
        func(game)
        if item in game.inventory:
            game.inventory.remove(item)
    else:
        game.feedback = f"{item.get('naam')} heeft geen effect."

