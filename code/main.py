import pygame
import sys
from settings import *
from level import Level
from upgrade import Upgrade
from mode_selection import ModeSelection
from inventory import Inventory
from pause_handler import PauseHandler
from intro_screen import IntroScreen  # Ensure you have the correct import

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()
        self.upgrade = Upgrade(self.level.player)
        self.inventory = Inventory(self.level.player)
        self.mode_selection = ModeSelection(self.screen, self.clock)
        self.pause_handler = PauseHandler(self.screen, pygame.font.Font('graphics/font/joystix.ttf', 74))

        self.intro_screen = IntroScreen(self.screen, self.clock)  # Initialize IntroScreen

        # Initialize paused state
        self.paused = False

        # Initialize and play background music
        pygame.mixer.init()
        self.main_sound = pygame.mixer.Sound('audio/main.ogg')
        self.main_sound.set_volume(0.5)
        self.main_sound.play(loops=-1)

    def show_intro(self):
        self.intro_screen.show_intro()

    def run(self):
        self.show_intro()

        selected_mode = self.mode_selection.show_mode_selection()
        if selected_mode == 'single':
            while True:
                self.handle_events()

                if not self.paused:
                    if self.upgrade.active:
                        self.upgrade.display()
                    else:
                        self.screen.fill(WATER_COLOR)
                        self.level.run()  # Run the game level
                        self.inventory.display()  # Show inventory screen

                if self.paused:
                    self.pause_handler.display_pause_screen()

                pygame.display.update()
                self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_i:
                    self.inventory.toggle()
                elif event.key == pygame.K_m:
                    self.upgrade.toggle()

if __name__ == '__main__':
    game = Game()
    game.run()
