import pygame
from game.engine import Game

def main():
    pygame.init()
    scherm = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("🧠 Wiskunde Dungeon Crawler")
    clock = pygame.time.Clock()

    spel = Game(None)  # tijdelijk geen scherm, eerst breedte/hoogte ophalen
    pygame.display.set_mode((spel.kaart_breedte, spel.kaart_hoogte))
    spel.scherm = pygame.display.get_surface()  # nu pas koppelen


    running = True
    while running:
        spel.update()

        if any(event.type == pygame.QUIT for event in pygame.event.get()):
            running = False

        spel.teken()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
