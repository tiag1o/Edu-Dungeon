import pygame
import random
from game import vragen, monsters 
from game.monsters import monsterlijst
from game.items import winkelvoorraad

class Game:
    def __init__(self, scherm):
        self.scherm = scherm
        self.font = pygame.font.SysFont("consolas", 24)
        self.monsters = self.monsters = monsterlijst
        self.huidig_monster = self.monsters[0]
        self.vraag = self.huidig_monster.geef_vraag(vragen.vragenlijst)
        self.invoer = ""
        self.feedback = ""
        self.inventaris_open = False  # geeft aan of het inventarisvenster open is
        self.goud = 0
        self.antwoord_gegeven = False
        self.winkel = winkelvoorraad
        self.winkel_actief = random.sample(self.winkel, 3)  # 👈 3 unieke shopitems
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



    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.USEREVENT:
                self.volgende_monster()
                pygame.time.set_timer(pygame.USEREVENT, 0)  # timer uitzetten
            elif event.type == pygame.MOUSEBUTTONDOWN:
                muis_pos = pygame.mouse.get_pos()

                
                # 📒 Kladblokknop checken
                if self.kladknop and self.kladknop.collidepoint(muis_pos):
                    self.kladblok_open = not self.kladblok_open  # toggle aan/uit
                # 🎒 Verkoop bij klik op een item in de inventaris
                if self.inventaris_open:
                    for rect, item in self.inventory_rects:
                        if rect.collidepoint(muis_pos):
                            verkoop_percentage = random.randint(10, 300)
                            verkoopprijs = int(item["prijs"] * verkoop_percentage / 100)
                            self.goud += verkoopprijs
                            self.inventory.remove(item)
                            self.feedback = f"💰 Verkocht voor {verkoopprijs} goud ({verkoop_percentage}%)"
                            break
                #resetknop
                if self.reset_knop and self.reset_knop.collidepoint(muis_pos):
                    self.kladlijnpunten = []
                self.laatste_kladpunt = None

                

                # ➕ Symboolknoppen
                for rect, symbool in self.symbol_knoppen:
                    if rect.collidepoint(muis_pos):
                        self.invoer += symbool.replace("| |", "|")  # of extra logica voor speciale gevallen
              


                # 🛒 Shopzones checken
                for rect, index in self.shop_zones:
                    if rect.collidepoint(muis_pos):
                        self.koop_item(index)
                #inventrarisknop
                if self.inventaris_knop_rect.collidepoint(muis_pos):
                    self.inventaris_open = not self.inventaris_open


                # 📦 Speciale knoppen
                for naam, rect in self.knoppen.items():
                    if rect.collidepoint(muis_pos):
                        if naam == "Sla over":
                            self.feedback = "⏭️ Vraag overgeslagen."
                            pygame.time.set_timer(pygame.USEREVENT, 1000)
                        elif naam == "Hint":
                            self.feedback = f"💡 Hint: {self.vraag['hint']}"
                        elif naam == "Toon antwoord":
                            self.feedback = f"📖 Antwoord was: {self.vraag['antwoord']}"
                            self.goud = max(0, self.goud - 3)
                            pygame.time.set_timer(pygame.USEREVENT, 1500)
            elif event.type == pygame.MOUSEMOTION:
                if self.kladblok_open and event.buttons[0]:  # Linkermuisknop ingedrukt
                    huidige_pos = event.pos
                    if self.laatste_kladpunt:
                        self.kladlijnpunten.append((self.laatste_kladpunt, huidige_pos))
                    self.laatste_kladpunt = huidige_pos

            elif event.type == pygame.MOUSEBUTTONUP:
                self.laatste_kladpunt = None  # Stop tekenen



            elif event.type == pygame.KEYDOWN:
                print("KEY:", event.key, "UNICODE:", event.unicode)

                if event.key == pygame.K_RETURN:
                    # Controleer het antwoord
                    juist_antwoord = self.vraag["antwoord"].replace(" ", "").lower()
                    speler_antwoord = self.invoer.replace(" ", "").lower()

                    if speler_antwoord == juist_antwoord:
                        self.feedback = f"✅ Correct! Je hebt {self.huidig_monster.goud} goud verdiend!"
                        self.huidig_monster.verslagen = True
                        self.antwoord_gegeven = True
                        self.goud += self.huidig_monster.goud
                        pygame.time.set_timer(pygame.USEREVENT, 1500)  # 1.5 sec wachten op nieuw monster
                    else:
                        self.feedback = "❌ Helaas, dat is niet juist..."

                elif event.key == pygame.K_BACKSPACE:
                    self.invoer = self.invoer[:-1]

                else:
                    self.invoer += event.unicode


    def volgende_monster(self):
    # Volgende monster pakken (of random)
        self.huidig_monster = random.choice(self.monsters)
        self.vraag = self.huidig_monster.geef_vraag(vragen.vragenlijst)

        self.invoer = ""
        self.feedback = ""
        self.antwoord_gegeven = False
   
    def teken(self):
        self.scherm.fill((25, 25, 50))

        # Monster + vraag
        vraag_tekst = self.font.render(f"{self.huidig_monster.naam}: {self.vraag['vraag']}", True, (255, 255, 255))
        self.scherm.blit(vraag_tekst, (50, 100))

        # Invoerveld
        invoer_tekst = self.font.render("Jouw antwoord: " + self.invoer, True, (200, 200, 50))
        pygame.draw.rect(self.scherm, (255, 255, 255), (45, 145, 900, 35), 2)  # witte rand
        self.scherm.blit(invoer_tekst, (50, 150))

        # Feedback na Enter
        if self.feedback:
            feedback_tekst = self.font.render(self.feedback, True, (0, 255, 0) if "✅" in self.feedback else (255, 50, 50))
            self.scherm.blit(feedback_tekst, (50, 200))
        #Goud
        goud_tekst = self.font.render(f"Goud: {self.goud}", True, (255, 215, 0))  # goudkleurig
        self.scherm.blit(goud_tekst, (50, 250))
        
        self.inventaris_knop_rect = pygame.Rect(700, 250, 200, 35)
        pygame.draw.rect(self.scherm, (100, 100, 200), self.inventaris_knop_rect)
        tekst = self.font.render("📦 Inventaris", True, (255, 255, 255))
        self.scherm.blit(tekst, (self.inventaris_knop_rect.x + 10, self.inventaris_knop_rect.y + 5))


        # Winkel tekenen
        y = 300
        self.scherm.blit(self.font.render("🛒 Winkel:", True, (255, 255, 255)), (50, y))

        self.shop_zones = []  # leegmaken bij elke frame
        for i, item in enumerate(self.winkel_actief):
            y += 40
            tekst = f"{item['naam']} - {item['prijs']} goud"

            muis_pos = pygame.mouse.get_pos()
            kleur = (255, 255, 255) if pygame.Rect(70, y, 800, 30).collidepoint(muis_pos) else (200, 200, 200)

            tekst_render = self.font.render(tekst, True, kleur)
            rect = tekst_render.get_rect(topleft=(70, y))
            self.scherm.blit(tekst_render, rect.topleft)
            self.shop_zones.append((rect, i))
        #Inventaris
        if self.inventaris_open:
            y = 300
            self.scherm.blit(self.font.render("🎒 Inventaris:", True, (255, 255, 255)), (600, y))
            for item in self.inventory:
                y += 30
                tekst = f"- {item['naam']}"
                self.scherm.blit(self.font.render(tekst, True, (180, 180, 180)), (620, y))
        
        # ➕ Symboolmenu
        self.symbol_knoppen = []  # leegmaken voor elke frame
        x = 50
        y = 620
        self.scherm.blit(self.font.render("🔣 Symbolen:", True, (255, 255, 255)), (x, y))

        for i, item in enumerate(self.symbolen):
            tekst = item["symbool"]
            tekst_render = self.font.render(tekst, True, (180, 180, 255))
            rect = tekst_render.get_rect(topleft=(x + i*80, y + 30))
            self.scherm.blit(tekst_render, rect.topleft)
            self.symbol_knoppen.append((rect, tekst))  # bewaar rect + symbool
        #knoppen
        # ⏹️ Knoppen tekenen
        knop_y = 500
        self.knoppen = {}  # Resetten

        for i, (naam, kleur) in enumerate([
            ("Sla over", (100, 100, 100)), 
            ("Hint", (0, 150, 255)), 
            ("Toon antwoord", (255, 100, 0))
        ]):
            rect = pygame.Rect(50 + i * 220, knop_y, 200, 40)
            pygame.draw.rect(self.scherm, kleur, rect)
            tekst = self.font.render(naam, True, (255, 255, 255))
            self.scherm.blit(tekst, (rect.x + 10, rect.y + 8))
            self.knoppen[naam] = rect
        # Alleen tonen als inventaris open is
        if self.inventaris_open:
            y_inv = 100
            pygame.draw.rect(self.scherm, (40, 40, 70), (500, y_inv, 420, 400))  # achtergrondvak
            self.scherm.blit(self.font.render("🎒 Inventaris", True, (255, 255, 255)), (520, y_inv + 10))

            self.inventory_rects = []  # resetten elke frame
            for i, item in enumerate(self.inventory):
                tekst = self.font.render(f"- {item['naam']}", True, (220, 220, 220))
                rect = tekst.get_rect(topleft=(520, y_inv + 40 + i * 30))
                self.scherm.blit(tekst, rect.topleft)
                self.inventory_rects.append((rect, item))

        # 🔘 Kladblokknop
        klad_tekst = self.font.render("📝 Kladblok", True, (255, 255, 255))
        klad_rect = klad_tekst.get_rect(topleft=(800, 80))  # onder de inventaris-knop
        self.scherm.blit(klad_tekst, klad_rect.topleft)
        self.kladknop = klad_rect
        if self.kladblok_open:
            pygame.draw.rect(self.scherm, (255, 255, 255), (50, 100, 900, 500))  # wit vlak

            # Teken alle lijnen
            for lijn in self.kladlijnpunten:
                pygame.draw.line(self.scherm, (0, 0, 0), lijn[0], lijn[1], 2)
        # 🔘 Kladblok resetknop
        reset_tekst = self.font.render("🧽 Wis kladblok", True, (255, 255, 255))
        reset_rect = reset_tekst.get_rect(topleft=(800, 120))  # onder de kladknop
        self.scherm.blit(reset_tekst, reset_rect.topleft)
        self.reset_knop = reset_rect









    def koop_item(self, index):
        item = self.winkel_actief[index]
        
        if self.goud >= item["prijs"]:
            self.goud -= item["prijs"]
            self.feedback = f"✅ Je hebt '{item['naam']}' gekocht!"
            self.inventaris.append(item)

            # 🔄 Vervang met nieuw item (als er nog andere beschikbaar zijn)
            overgebleven = [i for i in self.winkel if i not in self.winkel_actief]
            if overgebleven:
                nieuw_item = random.choice(overgebleven)
                self.winkel_actief[index] = nieuw_item
            else:
                self.winkel_actief.pop(index)  # niks meer over

        else:
            self.feedback = f"❌ Niet genoeg goud voor '{item['naam']}'"




