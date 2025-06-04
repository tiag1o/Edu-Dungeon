import pygame

def update_game(game):
    for event in pygame.event.get():
        # Ideeënbord event handling
        if getattr(game, 'ideeenbord_open', False):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    game.ideeenbord_tekst = game.ideeenbord_tekst[:-1]
                elif event.key == pygame.K_RETURN:
                    game.ideeenbord_tekst += "\n"
                else:
                    game.ideeenbord_tekst += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if hasattr(game, 'sluit_ideeenbord_rect') and game.sluit_ideeenbord_rect.collidepoint(event.pos):
                    game.ideeenbord_open = False
            return  # blokkeer andere events als bord open is
        elif event.type == pygame.QUIT:
            import sys
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            game.volgende_monster()
            pygame.time.set_timer(pygame.USEREVENT, 0)  # timer uitzetten
        elif event.type == pygame.MOUSEBUTTONDOWN:
            muis_pos = pygame.mouse.get_pos()
            # Ideeënbord openen (deze check moet vóór andere returns komen)
            if hasattr(game, 'idee_knop_rect') and game.idee_knop_rect.collidepoint(muis_pos):
                game.ideeenbord_open = True
                return
            # Kaart-terugknop (alleen binnen deze event, want alleen dan bestaat muis_pos)
            if hasattr(game, 'terug_naar_kaart_knop') and game.terug_naar_kaart_knop:
                if game.terug_naar_kaart_knop.collidepoint(muis_pos):
                    game.in_kaartscherm = True
                    game.feedback = "🗺️ Terug naar de kaart!"
                    return  # Stop verdere verwerking zodat andere knoppen niet triggeren
            # 🗺️ Kaartscherm checken
            if game.in_kaartscherm:
                for eiland in game.eilanden:
                    if eiland["rect"].collidepoint(muis_pos):
                        game.huidig_eiland = eiland["naam"]
                        if eiland["naam"] == "Limitanie":
                            key = "limitanie"
                        elif eiland["naam"] == "Integralia":
                            key = "integralia"
                        elif eiland["naam"] == "Logaritimië":
                            key = "logaritmie"
                        elif eiland["naam"] == "Pimania":
                            key = "pimania"
                        elif eiland["naam"] == "Cirkelosio":
                            key = "cirkelosio"
                        elif eiland["naam"] == "Gemengd":
                            key = "gemengd"
                        else:
                            key = "gemengd"
                        game.laad_vragen_voor_eiland(key)
                        game.laad_winkel_voor_eiland(key)
                        game.in_kaartscherm = False  # Zet direct kaartscherm uit
                        game.feedback = f"🗺️ Je hebt {game.huidig_eiland} gekozen!"
                        break
            # 📒 Kladblokknop checken
            if game.kladknop and game.kladknop.collidepoint(muis_pos):
                game.toggle_kladblok()
            # 🎒 Item interactie in de inventaris
            if game.inventaris_open:
                for rect, item in game.inventory_rects:
                    if rect.collidepoint(muis_pos):
                        if event.button == 1:
                            game.gebruik_item(item)
                        elif event.button == 3:
                            game.verkoop_item(item)
                        break
            #resetknop
            if game.reset_knop and game.reset_knop.collidepoint(muis_pos):
                game.wis_kladblok()
            game.laatste_kladpunt = None
            # ➕ Symboolknoppen
            for rect, symbool in game.symbol_knoppen:
                if rect.collidepoint(muis_pos):
                    game.invoer += symbool.replace("| |", "|")  # of extra logica voor speciale gevallen
            # 🛒 Shopzones checken
            for rect, index in game.shop_zones:
                if rect.collidepoint(muis_pos):
                    game.koop_item(index)
            #inventrarisknop
            if game.inventaris_knop_rect.collidepoint(muis_pos):
                game.toggle_inventaris()
            # 📦 Speciale knoppen
            for naam, rect in game.knoppen.items():
                if rect.collidepoint(muis_pos):
                    if naam == "Sla over":
                        game.feedback = "⏭️ Vraag overgeslagen."
                        pygame.time.set_timer(pygame.USEREVENT, 1000)
                    elif naam == "Hint":
                        game.feedback = f"💡 Hint: {game.vraag['hint']}"
                    elif naam == "Toon antwoord":
                        game.feedback = f"📖 Antwoord was: {game.vraag['antwoord']}"
                        game.goud = max(0, game.goud - 3)
                        pygame.time.set_timer(pygame.USEREVENT, 1500)
        elif event.type == pygame.MOUSEMOTION:
            if game.kladblok_open and event.buttons[0]:  # Linkermuisknop ingedrukt
                huidige_pos = event.pos
                if game.laatste_kladpunt:
                    game.kladlijnpunten.append((game.laatste_kladpunt, huidige_pos))
                game.laatste_kladpunt = huidige_pos
        elif event.type == pygame.MOUSEBUTTONUP:
            game.laatste_kladpunt = None  # Stop tekenen
        elif event.type == pygame.KEYDOWN:
            print("KEY:", event.key, "UNICODE:", event.unicode)
            if event.key == pygame.K_RETURN:
                # Controleer het antwoord
                juist_antwoord = game.vraag["antwoord"].replace(" ", "").lower()
                speler_antwoord = game.invoer.replace(" ", "").lower()
                if speler_antwoord == juist_antwoord:
                    game.feedback = f"✅ Correct! Je hebt {game.huidig_monster.goud} goud verdiend!"
                    game.huidig_monster.verslagen = True
                    game.antwoord_gegeven = True
                    game.goud += game.huidig_monster.goud
                    # Geef XP voor monster
                    if hasattr(game.huidig_monster, 'xp'):
                        game.geef_xp(game.huidig_monster.xp)
                    pygame.time.set_timer(pygame.USEREVENT, 1500)  # 1.5 sec wachten op nieuw monster
                else:
                    game.feedback = "❌ Helaas, dat is niet juist..."
            elif event.key == pygame.K_BACKSPACE:
                game.invoer = game.invoer[:-1]
            else:
                game.invoer += event.unicode
