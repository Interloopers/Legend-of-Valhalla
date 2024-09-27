import pygame
import sys

class PauseHandler:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.paused = False

        # Pause background and text
        self.pause_bg = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.pause_bg.fill((0, 0, 0))
        self.pause_text = self.font.render('PAUSED', True, (255, 255, 255))
        self.pause_text_rect = self.pause_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

    def toggle_pause(self):
        """Toggle the pause state of the game."""
        self.paused = not self.paused

    def handle_pause_events(self):
        """Handle events while the game is paused."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Unpause
                    self.toggle_pause()
                elif event.key == pygame.K_ESCAPE:  # Quit game
                    pygame.quit()
                    sys.exit()

    def display_pause_screen(self):
        """Display the pause screen."""
        self.screen.blit(self.pause_bg, (0, 0))
        self.screen.blit(self.pause_text, self.pause_text_rect)
        pygame.display.update()
