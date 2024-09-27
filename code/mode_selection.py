import pygame
import sys

class ModeSelection:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.font = pygame.font.Font('graphics/font/joystix.ttf', 60)  # Larger font for options
        self.intro_bg = pygame.image.load('graphics/img/bg2.png').convert()
        self.intro_bg = pygame.transform.scale(self.intro_bg, (self.screen.get_width(), self.screen.get_height()))

        # Calculate the option box size to be 60% of the screen width and centered
        self.option_width = int(self.screen.get_width() * 0.6)
        self.option_height = 70  # Increase height for better visual appeal

    def draw_option(self, text, x, y, hover):
        text_color = (200, 0, 0) if hover else (0, 0, 0)  # Light red on hover, black otherwise
        text_surface = self.font.render(text, True, text_color)  # Render text
        self.screen.blit(text_surface, (x, y))

    def show_mode_selection(self):
        # Define the centered positions for the text
        center_x = self.screen.get_width() // 2 - self.option_width // 2

        # Rects for the options (60% width, 70px height, centered)
        single_text_rect = pygame.Rect(center_x, self.screen.get_height() // 2 - 80, self.option_width, self.option_height)
        multiplayer_text_rect = pygame.Rect(center_x, self.screen.get_height() // 2 + 30, self.option_width, self.option_height)

        while True:
            self.screen.blit(self.intro_bg, (0, 0))  # Draw the scaled background image

            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Single option hover and movement
            single_hover = single_text_rect.collidepoint(mouse_pos)
            single_y = self.screen.get_height() // 2 - 80 - (5 if single_hover else 0)  # Move slightly up if hovered
            self.draw_option('Single', single_text_rect.x + self.option_width // 2 - self.font.size('Single')[0] // 2, single_y, single_hover)

            # Multiplayer option hover and movement
            multiplayer_hover = multiplayer_text_rect.collidepoint(mouse_pos)
            multiplayer_y = self.screen.get_height() // 2 + 30 - (5 if multiplayer_hover else 0)  # Move slightly up if hovered
            self.draw_option('Multiplayer', multiplayer_text_rect.x + self.option_width // 2 - self.font.size('Multiplayer')[0] // 2, multiplayer_y, multiplayer_hover)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()  # Quit the game
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if single_text_rect.collidepoint(event.pos):
                        return 'single'  # Return 'single' to indicate single-player mode
                    if multiplayer_text_rect.collidepoint(event.pos):
                        pass  # Multiplayer not implemented yet

            self.clock.tick(60)
