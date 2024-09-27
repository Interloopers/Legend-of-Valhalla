import pygame
from settings import *

class Inventory:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.font = pygame.font.Font(UI_FONT, INVENTORY_FONT_SIZE)
        self.is_active = False

        # Load weapon and magic images
        self.weapon_images = {weapon: pygame.image.load(weapon_data[weapon]['graphic']).convert_alpha() for weapon in weapon_data}
        self.magic_images = {magic: pygame.image.load(magic_data[magic]['graphic']).convert_alpha() for magic in magic_data}

    def display(self):
        if self.is_active:
            self.display_surface.fill((0, 0, 0))  # Clear screen

            # Display weapons
            for i, weapon in enumerate(self.player.weapons):
                weapon_image = self.weapon_images[weapon]
                weapon_rect = pygame.Rect(50, 50 + i * 100, 80, 80)
                self.display_surface.blit(weapon_image, weapon_rect.topleft)
                weapon_text = self.font.render(weapon, True, (255, 255, 255))
                self.display_surface.blit(weapon_text, (150, 50 + i * 100))

            # Display magic
            for i, magic in enumerate(self.player.magic_list):
                magic_image = self.magic_images[magic]
                magic_rect = pygame.Rect(300, 50 + i * 100, 80, 80)
                self.display_surface.blit(magic_image, magic_rect.topleft)
                magic_text = self.font.render(magic, True, (255, 255, 255))
                self.display_surface.blit(magic_text, (400, 50 + i * 100))

            # Remove X button code
            # No need to draw or handle events for the X button here

    def toggle(self):
        self.is_active = not self.is_active
