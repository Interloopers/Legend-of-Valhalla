# game setup
WIDTH = 1280
HEIGHT = 720  # Corrected typo
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0
}

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'graphics/font/joystix.ttf'
UI_FONT_SIZE = 18  # Ensure consistency

# general colors
WATER_COLOR = (113, 221, 238)  # Converted to RGB tuple
UI_BG_COLOR = (34, 34, 34)     # Converted to RGB tuple
UI_BORDER_COLOR = (17, 17, 17) # Converted to RGB tuple
TEXT_COLOR = (238, 238, 238)   # Converted to RGB tuple

# ui colors
HEALTH_COLOR = (255, 0, 0)     # Converted to RGB tuple
ENERGY_COLOR = (0, 0, 255)     # Converted to RGB tuple
UI_BORDER_COLOR_ACTIVE = (255, 215, 0)  # Converted to RGB tuple

# upgrade menu
TEXT_COLOR_SELECTED = (17, 17, 17)  # Converted to RGB tuple
BAR_COLOR = (238, 238, 238)         # Converted to RGB tuple
BAR_COLOR_SELECTED = (17, 17, 17)   # Converted to RGB tuple
UPGRADE_BG_COLOR_SELECTED = (238, 238, 238)  # Converted to RGB tuple

# inventory
INVENTORY_BG_COLOR = (51, 51, 51)  # Converted to RGB tuple
INVENTORY_BORDER_COLOR = (85, 85, 85)  # Converted to RGB tuple
INVENTORY_FONT_SIZE = 24  # Font size for inventory items
INVENTORY_ITEM_COLOR = (255, 255, 255)  # Converted to RGB tuple

# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': 'graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': 'graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': 'graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': 'graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': 'graphics/weapons/sai/full.png'}
}

# magic
magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': 'graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic': 'graphics/particles/heal/heal.png'}
}

# enemy
monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': 'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 'attack_sound': 'audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': 'audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound': 'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}
