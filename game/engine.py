import pygame
import random
import importlib
from game import vragen, monsters 
from game.monsters import monsterlijst
from game.items import basis_winkelvoorraad, eiland_winkels
from game.teken import teken_game
from game.shop import koop_item
from game.kladblok import toggle_kladblok, wis_kladblok
from game.inventaris import toggle_inventaris, verkoop_item, gebruik_item as gebruik_inventaris_item
import os

class Game:
    def __init__(self, scherm):
        self.scherm = scherm
        self.font = pygame.font.SysFont("consolas", 24)
        self.monsters = monsterlijst
        self.huidig_monster = self.monsters[0]
        self.vraagbron = []  # Nog geen vragen beschikbaar tot een eiland gekozen wordt
        self.vraag = {"vraag": "🗺️ Kies een eiland op de kaart!", "antwoord": "", "hint": ""}
        self.invoer = ""
        self.feedback = ""
        self.inventaris_open = False  # geeft aan of het inventarisvenster open is
        self.goud = 1000
        self.antwoord_gegeven = False
        # Start met de basisvoorraad tot een eiland gekozen wordt
        self.winkel = basis_winkelvoorraad
        self.winkel_actief = random.sample(self.winkel, min(3, len(self.winkel)))
        self.shop_zones = []  # lijst met item-rectangles
        self.inventory = []            # lijst met gekochte items
        self.symbolen = [
            {"symbool": "^"}, {"symbool": "√"}, {"symbool": "log"}, {"symbool": "ln"},
            {"symbool": "| |"}, {"symbool": "±"}, {"symbool": "∫"}, {"symbool": "+"}, {"symbool": "π"}, {"symbool": "∑"},]
        self.symbol_knoppen = []
        self.knoppen = {}  # Voor 'overslaan', 'hint', 'toon_antwoord'
        self.kladblok_open = False
        self.kladlijnpunten = []  # lijst van lijntjes [(start, eind), ...]
        self.laatste_kladpunt = None  # vorige positie van de muis
        self.kladknop = None      # wordt een pygame.Rect
        self.in_kaartscherm = True  # We starten in het kaartscherm
        def resource_path(rel_path):
            import sys
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, rel_path)
            return os.path.join(os.path.dirname(os.path.dirname(__file__)), rel_path)
        self.kaart_afbeelding = pygame.image.load(resource_path('Landkaart.png'))  # Relatief pad
        self.kaart_breedte, self.kaart_hoogte = self.kaart_afbeelding.get_size()
        self.reset_knop = None
        self.inventaris_knop_rect = pygame.Rect(700, 250, 200, 35)
        self.huidig_eiland = None
        self.eilanden = [
            {"naam": "Limitanie", "rect": pygame.Rect(437, 117, 350, 100)},
            {"naam": "Integralia", "rect": pygame.Rect(1100, 270, 350, 100)},
            {"naam": "Logaritimië", "rect": pygame.Rect(1140, 612, 333, 100)},
            {"naam": "Pimania", "rect": pygame.Rect(300, 819, 300, 100)},
            {"naam": "Cirkelosio", "rect": pygame.Rect(660, 801, 330, 100)},
            {"naam": "Gemengd", "rect": pygame.Rect(402, 579, 350, 100)}
        
]
        self.ideeenbord_open = False
        self.ideeenbord_tekst = ""
        self.xp = 0
        self.level = 1
        self.xp_voor_volgend_level = self.bereken_xp_voor_level(self.level)

    def laad_vragen_voor_eiland(self, eiland_naam):
        if eiland_naam.lower() == "gemengd":
            # Importeer alle vragenlijsten en voeg ze samen
            from game.vragen.limitanie import vragenlijst as lim_vragen
            from game.vragen.integralia import vragenlijst as int_vragen
            from game.vragen.logaritmie import vragenlijst as log_vragen
            from game.vragen.pimania import vragenlijst as pim_vragen
            from game.vragen.cirkelosio import vragenlijst as cir_vragen
            alle_vragen = lim_vragen + int_vragen + log_vragen + pim_vragen + cir_vragen
            import random
            random.shuffle(alle_vragen)
            self.vraagbron = alle_vragen
        else:
            vragenmodule = importlib.import_module(f"game.vragen.{eiland_naam}")
            self.vraagbron = vragenmodule.vragenlijst
        self.vraag = self.huidig_monster.geef_vraag(self.vraagbron)

    def laad_winkel_voor_eiland(self, eiland_naam):
        """Laad de winkelvoorraad afhankelijk van het gekozen eiland."""
        eiland_naam = eiland_naam.lower()
        voorraad = eiland_winkels.get(eiland_naam, basis_winkelvoorraad)
        self.winkel = voorraad
        self.winkel_actief = random.sample(self.winkel, min(3, len(self.winkel)))


    def update(self):
        from game.update import update_game
        update_game(self)

    def volgende_monster(self):
        # Volgende monster pakken (of random)
        self.huidig_monster = random.choice(self.monsters)
        # Gebruik de juiste vragenbron afhankelijk van het gekozen eiland
        if self.vraagbron:
            self.vraag = self.huidig_monster.geef_vraag(self.vraagbron)
        else:
            self.vraag = {"vraag": "🗺️ Kies een eiland op de kaart!", "antwoord": "", "hint": ""}
        self.invoer = ""
        self.feedback = ""
        self.antwoord_gegeven = False
   
    def teken(self):
        teken_game(self)

    def toggle_inventaris(self):
        toggle_inventaris(self)

    def toggle_kladblok(self):
        toggle_kladblok(self)

    def wis_kladblok(self):
        wis_kladblok(self)

    def koop_item(self, index):
        koop_item(self, index)

    def verkoop_item(self, item):
        verkoop_item(self, item)

    def gebruik_item(self, item):
        gebruik_inventaris_item(self, item)

    def bereken_xp_voor_level(self, level):
        # Exponentiële groei: bijv. 50 * (1.5 ** (level-1))
        return int(50 * (1.5 ** (level-1)))

    def geef_xp(self, hoeveelheid):
        self.xp += hoeveelheid
        while self.xp >= self.xp_voor_volgend_level:
            self.xp -= self.xp_voor_volgend_level
            self.level += 1
            self.xp_voor_volgend_level = self.bereken_xp_voor_level(self.level)
            self.feedback = f"🎉 Level omhoog! Je bent nu level {self.level}!"




