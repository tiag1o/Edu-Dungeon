import os
import pygame

def resource_path(rel_path):
    import sys
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), rel_path)

def teken_game(game):
    # 🗺️ Kaartscherm tonen
    if game.in_kaartscherm:
        game.scherm.blit(game.kaart_afbeelding, (0, 0))
        for eiland in game.eilanden:
            pygame.draw.rect(game.scherm, (0, 0, 0), eiland["rect"], 2)  # Debugrand
        return  # Stop hier, rest pas als spel actief is

    game.scherm.fill((25, 25, 50))

    # Monster + vraag
    vraag_tekst = game.font.render(f"{game.huidig_monster.naam}: {game.vraag['vraag']}", True, (255, 255, 255))
    game.scherm.blit(vraag_tekst, (50, 100))

    # Invoerveld
    invoer_tekst = game.font.render("Jouw antwoord: " + game.invoer, True, (200, 200, 50))
    pygame.draw.rect(game.scherm, (255, 255, 255), (45, 145, 900, 35), 2)  # witte rand
    game.scherm.blit(invoer_tekst, (50, 150))

    # Feedback na Enter
    if game.feedback:
        feedback_tekst = game.font.render(game.feedback, True, (0, 255, 0) if "✅" in game.feedback else (255, 50, 50))
        game.scherm.blit(feedback_tekst, (50, 200))
    #Goud
    goud_tekst = game.font.render(f"Goud: {game.goud}", True, (255, 215, 0))  # goudkleurig
    game.scherm.blit(goud_tekst, (50, 250))
    # Goudstukken-afbeelding naast de goudcounter
    try:
        if not hasattr(game, '_goud_img'):
            game._goud_img = pygame.image.load(resource_path('Goudstukken.png'))
            game._goud_img = pygame.transform.scale(game._goud_img, (32, 32))
        game.scherm.blit(game._goud_img, (50 + goud_tekst.get_width() + 10, 245))
    except Exception as e:
        pass  # Geen crash als plaatje ontbreekt
    
    game.inventaris_knop_rect = pygame.Rect(1200, 250, 200, 35)
    pygame.draw.rect(game.scherm, (100, 100, 200), game.inventaris_knop_rect)
    tekst = game.font.render("📦 Inventaris", True, (255, 255, 255))
    game.scherm.blit(tekst, (game.inventaris_knop_rect.x + 10, game.inventaris_knop_rect.y + 5))

    # Winkel tekenen
    y = 270
    game.scherm.blit(game.font.render("🛒 Winkel:", True, (255, 255, 255)), (50, y))
    # Winkelier-afbeelding rechts van de winkel
    try:
        if not hasattr(game, '_winkelier_img'):
            game._winkelier_img = pygame.image.load(resource_path('winkelier.png'))
            game._winkelier_img = pygame.transform.scale(game._winkelier_img, (201, 201))
        game.scherm.blit(game._winkelier_img, (600, y + 20))
    except Exception as e:
        pass  # Geen crash als plaatje ontbreekt

    game.shop_zones = []  # leegmaken bij elke frame
    for i, item in enumerate(game.winkel_actief):
        y += 40
        tekst = f"{item['naam']} - {item['prijs']} goud"
        muis_pos = pygame.mouse.get_pos()
        kleur = (255, 255, 255) if pygame.Rect(70, y, 800, 30).collidepoint(muis_pos) else (200, 200, 200)
        tekst_render = game.font.render(tekst, True, kleur)
        rect = tekst_render.get_rect(topleft=(70, y))
        game.scherm.blit(tekst_render, rect.topleft)
        game.shop_zones.append((rect, i))
    # ➕ Symboolmenu
    game.symbol_knoppen = []  # leegmaken voor elke frame
    x = 50
    y = 620
    game.scherm.blit(game.font.render("🔣 Symbolen:", True, (255, 255, 255)), (x, y))
    for i, item in enumerate(game.symbolen):
        tekst = item["symbool"]
        tekst_render = game.font.render(tekst, True, (180, 180, 255))
        rect = tekst_render.get_rect(topleft=(x + i*80, y + 30))
        game.scherm.blit(tekst_render, rect.topleft)
        game.symbol_knoppen.append((rect, tekst))  # bewaar rect + symbool
    #knoppen
    # ⏹️ Knoppen tekenen
    knop_y = 500
    game.knoppen = {}  # Resetten
    for i, (naam, kleur) in enumerate([
        ("Sla over", (100, 100, 100)), 
        ("Hint", (0, 150, 255)), 
        ("Toon antwoord", (255, 100, 0))
    ]):
        rect = pygame.Rect(50 + i * 220, knop_y, 200, 40)
        pygame.draw.rect(game.scherm, kleur, rect)
        tekst = game.font.render(naam, True, (255, 255, 255))
        game.scherm.blit(tekst, (rect.x + 10, rect.y + 8))
        game.knoppen[naam] = rect
    # Alleen tonen als inventaris open is
    if game.inventaris_open:
        y_inv = 300
        pygame.draw.rect(game.scherm, (40, 40, 70), (900, y_inv, 420, 400))  # achtergrondvak
        game.scherm.blit(game.font.render("🎒 Inventaris", True, (255, 255, 255)), (900, y_inv + 10))
        game.inventory_rects = []  # resetten elke frame
        for i, item in enumerate(game.inventory):
            tekst = game.font.render(f"- {item['naam']}", True, (220, 220, 220))
            rect = tekst.get_rect(topleft=(520, y_inv + 40 + i * 30))
            game.scherm.blit(tekst, rect.topleft)
            game.inventory_rects.append((rect, item))
    # 🔘 Kladblokknop
    klad_tekst = game.font.render("📝 Kladblok", True, (255, 255, 255))
    klad_rect = klad_tekst.get_rect(topleft=(1200, 80))  # onder de inventaris-knop
    game.scherm.blit(klad_tekst, klad_rect.topleft)
    game.kladknop = klad_rect
    if game.kladblok_open:
        pygame.draw.rect(game.scherm, (255, 255, 255), (50, 100, 900, 500))  # wit vlak
        # Teken alle lijnen
        for lijn in game.kladlijnpunten:
            pygame.draw.line(game.scherm, (0, 0, 0), lijn[0], lijn[1], 2)
    # 🔘 Kladblok resetknop
    reset_tekst = game.font.render("🧽 Wis kladblok", True, (255, 255, 255))
    reset_rect = reset_tekst.get_rect(topleft=(1200, 120))  # onder de kladknop
    game.scherm.blit(reset_tekst, reset_rect.topleft)
    game.reset_knop = reset_rect

    # Voeg knop toe om terug te keren naar de kaart (alleen als je NIET in het kaartscherm bent)
    if not game.in_kaartscherm:
        terug_rect = pygame.Rect(1302, 20, 120, 40)
        pygame.draw.rect(game.scherm, (120, 120, 255), terug_rect)
        terug_tekst = game.font.render("Kaart", True, (255, 255, 255))
        game.scherm.blit(terug_tekst, (terug_rect.x + 20, terug_rect.y + 8))
        game.terug_naar_kaart_knop = terug_rect
    else:
        game.terug_naar_kaart_knop = None

    # Voeg Ideeënbord-knop toe rechtsboven
    idee_knop_rect = pygame.Rect(1050, 20, 180, 40)
    pygame.draw.rect(game.scherm, (120, 120, 255), idee_knop_rect)
    idee_tekst = game.font.render("Ideeënbord", True, (255, 255, 255))
    game.scherm.blit(idee_tekst, (idee_knop_rect.x + 20, idee_knop_rect.y + 8))
    game.idee_knop_rect = idee_knop_rect

    # Teken het ideeënbord als het open is
    if getattr(game, 'ideeenbord_open', False):
        game.scherm.fill((255, 255, 255))
        # Multiline tekst weergeven
        y_text = 100
        for regel in game.ideeenbord_tekst.split("\n"):
            tekstvlak = game.font.render(regel, True, (0, 0, 0))
            game.scherm.blit(tekstvlak, (60, y_text))
            y_text += 32
        # Sluit-knop
        sluit_rect = pygame.Rect(1050, 20, 180, 40)
        pygame.draw.rect(game.scherm, (200, 80, 80), sluit_rect)
        sluit_tekst = game.font.render("Sluit bord", True, (255, 255, 255))
        game.scherm.blit(sluit_tekst, (sluit_rect.x + 20, sluit_rect.y + 8))
        game.sluit_ideeenbord_rect = sluit_rect
        return  # rest van het spel niet tekenen

    # XP-bar tekenen onder goud
    bar_x = 50
    bar_y = 801
    bar_w = 400
    bar_h = 28
    # Bepaal percentage
    xp = getattr(game, 'xp', 0)
    level = getattr(game, 'level', 1)
    xp_next = getattr(game, 'xp_voor_volgend_level', 100)
    perc = min(xp / xp_next, 1.0)
    # Achtergrond
    pygame.draw.rect(game.scherm, (60, 60, 60), (bar_x, bar_y, bar_w, bar_h), border_radius=8)
    # Gevuld deel
    pygame.draw.rect(game.scherm, (80, 180, 255), (bar_x, bar_y, int(bar_w * perc), bar_h), border_radius=8)
    # Rand
    pygame.draw.rect(game.scherm, (0, 0, 0), (bar_x, bar_y, bar_w, bar_h), 2, border_radius=8)
    # Tekst
    xp_tekst = game.font.render(f"Level {level}  XP: {xp} / {xp_next}", True, (0, 0, 0))
    game.scherm.blit(xp_tekst, (bar_x + 10, bar_y + 2))
