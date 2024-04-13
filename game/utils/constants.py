import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
WRENCH = pygame.image.load(os.path.join(IMG_DIR, 'Other/wrench.png'))
THRUSTER = pygame.image.load(os.path.join(IMG_DIR, 'Other/thruster.png'))
SCORE_BONUS = pygame.image.load(os.path.join(IMG_DIR, 'Other/score_bonus.png'))
SPACESHIP_CANNON = pygame.image.load(os.path.join(IMG_DIR, "Other/cannon.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_THRUSTERS =  pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_thrusters.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_CANNON = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_cannon.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_OVNI = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_ovni.png"))
ENEMY_BETRAYER = pygame.image.load(os.path.join(IMG_DIR, "Enemy/betrayer.png"))
ENEMY_FALCON = pygame.image.load(os.path.join(IMG_DIR, "Enemy/falcon.png"))
ENEMY_MARAUDER = pygame.image.load(os.path.join(IMG_DIR, "Enemy/marauder.png"))
ENEMY_LANCE = pygame.image.load(os.path.join(IMG_DIR, "Enemy/lance.png"))
ENEMY_ORBIT = pygame.image.load(os.path.join(IMG_DIR, "Enemy/orbit.png"))
ENEMY_PYLON = pygame.image.load(os.path.join(IMG_DIR, "Enemy/pylon.png"))
BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/boss.gif"))

FONT_STYLE = 'freesansbold.ttf'

LEFT = 'left'
RIGHT = 'right'

BULLET_ENEMY_TYPE = 'enemy'
BULLET_ALLY_TYPE = 'ally'
BULLET_ALLY_CANNON_TYPE = 'ally_cannon'

WHITE = (255,255,255)