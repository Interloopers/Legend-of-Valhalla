import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

        # Intro screen flag
        self.intro = True

        # Pause flag
        self.paused = False

        # Custom Font (download a .ttf font and place it in your graphics folder)
        self.font = pygame.font.Font('graphics/font/joystix.ttf', 74)

        # Load and scale background image
        self.intro_bg = pygame.image.load('graphics/img/bg2.png').convert()
        self.intro_bg = pygame.transform.scale(self.intro_bg, (WIDTH, HEIGTH))  # Scale the image to screen size

        # Blink timer for "Press SPACE to Start" text
        self.blink_timer = 0  # Initialize a timer for blinking

        # Load pause screen background
        self.pause_bg = pygame.Surface((WIDTH, HEIGTH))
        self.pause_bg.fill((0, 0, 0))  # Black background
        self.pause_text = self.font.render('PAUSED', True, (255, 255, 255))
        self.pause_text_rect = self.pause_text.get_rect(center=(WIDTH // 2, HEIGTH // 2))

    def show_intro(self):
        while self.intro:
            self.screen.blit(self.intro_bg, (0, 0))  # Draw the scaled background image

            # Create title text with shadow
            title_text = self.font.render('LEGEND OF ZELDA', True, (255, 255, 255))  # White text
            title_shadow = self.font.render('LEGEND OF ZELDA', True, (0, 0, 0))  # Black shadow

            # Draw shadow first (slightly offset)
            self.screen.blit(title_shadow, (WIDTH // 2 - title_text.get_width() // 2 + 2, HEIGTH // 3 + 2))
            # Draw the white text on top
            self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGTH // 3))

            # Blinking "Press SPACE to Start" text with shadow
            self.blink_timer += 1
            if self.blink_timer % 60 < 30:  # Toggle blinking every half second (assuming 60 FPS)
                prompt_text = self.font.render('Press SPACE to Start', True, (255, 255, 255))  # White text
                prompt_shadow = self.font.render('Press SPACE to Start', True, (0, 0, 0))  # Black shadow

                # Draw shadow first (slightly offset)
                self.screen.blit(prompt_shadow, (WIDTH // 2 - prompt_text.get_width() // 2 + 2, HEIGTH // 2 + 2))
                # Draw the white text on top
                self.screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGTH // 2))

            pygame.display.update()

            # Wait for spacebar to exit the intro screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.intro = False  # Exit intro loop and start the game

            self.clock.tick(FPS)

    def show_pause_screen(self):
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.paused = False  # Unpause the game
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()  # Quit the game

            self.screen.blit(self.pause_bg, (0, 0))  # Draw the pause screen background
            self.screen.blit(self.pause_text, self.pause_text_rect)  # Draw the pause text
            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):
        self.show_intro()  # Show the intro screen first

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.paused = not self.paused  # Toggle pause state
                        if self.paused:
                            self.show_pause_screen()  # Show pause screen
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()  # Quit the game

            if not self.paused:
                self.screen.fill(WATER_COLOR)
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
