import pygame
import sys

class IntroScreen:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.font = pygame.font.Font('graphics/font/joystix.ttf', 74)

        # Load and scale background image
        self.intro_bg = pygame.image.load('graphics/img/bg2.png').convert()
        self.intro_bg = pygame.transform.scale(self.intro_bg, (self.screen.get_width(), self.screen.get_height()))

        # Initialize blinking parameters
        self.blink_interval = 1000  # Blink interval in milliseconds (5 seconds)
        self.last_blink_time = pygame.time.get_ticks()  # Time of the last blink
        self.blink_state = True  # Current state of blinking

    def show_intro(self):
        intro = True
        while intro:
            current_time = pygame.time.get_ticks()

            # Toggle blink state based on the interval
            if current_time - self.last_blink_time >= self.blink_interval:
                self.last_blink_time = current_time
                self.blink_state = not self.blink_state

            self.screen.blit(self.intro_bg, (0, 0))

            # Create title text with shadow
            title_text = self.font.render('LEGEND OF VALHALLA', True, (255, 255, 255))
            title_shadow = self.font.render('LEGEND OF VALHALLA', True, (0, 0, 0))

            # Draw shadow first (slightly offset)
            self.screen.blit(title_shadow, (self.screen.get_width() // 2 - title_text.get_width() // 2 + 2, self.screen.get_height() // 3 + 2))
            # Draw the white text on top
            self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, self.screen.get_height() // 3))

            # Blinking "Press SPACE to Start" text with shadow
            if self.blink_state:
                prompt_text = self.font.render('Press SPACE to Start', True, (255, 255, 255))
                prompt_shadow = self.font.render('Press SPACE to Start', True, (0, 0, 0))

                # Draw shadow first (slightly offset)
                self.screen.blit(prompt_shadow, (self.screen.get_width() // 2 - prompt_text.get_width() // 2 + 2, self.screen.get_height() // 2 + 2))
                # Draw the white text on top
                self.screen.blit(prompt_text, (self.screen.get_width() // 2 - prompt_text.get_width() // 2, self.screen.get_height() // 2))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        intro = False

            # Control the frame rate
            self.clock.tick(60)
