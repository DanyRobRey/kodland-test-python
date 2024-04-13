import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ALLY_TYPE, BULLET_ALLY_CANNON_TYPE, SPACESHIP_SHIELD, SPACESHIP_THRUSTERS
from game.components.power_ups.shield import Shield
from game.components.power_ups.wrench import Wrench
from game.components.power_ups.thrusters import Thruster
from game.components.power_ups.score_bonus import ScoreBonus
from game.components.power_ups.cannon import Cannon


class SpaceShip:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH//2) - WIDTH
    Y_POS = 500
    SHOOTING_TIME = 5
    SHIELD = 'shield'
    THRUSTER = 'thruster'
    SCORE_BONUS = 'score_bonus'
    WRENCH = 'wrench'
    CANNON = 'cannon'
    REPAIR = 5

    def __init__(self, game_speed):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.shooting_time = 0
        self.has_shield = False
        self.has_wrench = False
        self.has_score_bonus = False
        self.has_thrusters = False
        self.has_cannon = False
        self.time_up = 0
        self.max_energy = 20
        self.energy = 20
        self.speed = game_speed
        self.original_speed = game_speed
        self.bonus_speed = 0
        self.score = 0
        self.time_power_up_left = 0

    def update(self, user_input, bullet_handler, power_up_handler):
        if user_input[pygame.K_LEFT]:
            self.move_left(self.speed)
        if user_input[pygame.K_RIGHT]:
            self.move_right(self.speed)
        if user_input[pygame.K_UP]:
            self.move_up(self.speed)
        if user_input[pygame.K_DOWN]:
            self.move_down(self.speed)
        if user_input[pygame.K_SPACE]:
            self.shoot(bullet_handler)
            self.shooting_time += 1
        if self.has_shield:
            self.time_power_up_left = round((self.time_up - pygame.time.get_ticks())/1000,2)
            if self.time_power_up_left < 0:
                power_up_handler.power_ups[0].is_used = False
                self.deactivate_power_up(self.SHIELD)
        if self.has_thrusters:
            self.time_power_up_left = round((self.time_up - pygame.time.get_ticks())/1000,2)
            if self.time_power_up_left < 0:
                power_up_handler.power_ups[0].is_used = False
                self.deactivate_power_up(self.THRUSTER)
        if self.has_score_bonus:
            self.time_power_up_left = round((self.time_up - pygame.time.get_ticks())/1000,2)
            if self.time_power_up_left < 0:
                power_up_handler.power_ups[0].is_used = False
                self.deactivate_power_up(self.SCORE_BONUS)
        if self.has_wrench:
            self.time_power_up_left = round((self.time_up - pygame.time.get_ticks())/1000,2)
            if self.time_power_up_left < 0:
                power_up_handler.power_ups[0].is_used = False
                self.deactivate_power_up(self.WRENCH)
        if self.has_cannon:
            self.time_power_up_left = round((self.time_up - pygame.time.get_ticks())/1000,2)
            if self.time_power_up_left < 0:
                power_up_handler.power_ups[0].is_used = False
                self.deactivate_power_up(self.CANNON)
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self, speed):
        self.rect.x -= speed
        if self.rect.left <= 0:
            self.rect.x = SCREEN_WIDTH - self.rect.width

    def move_right(self, speed):
        self.rect.x += speed
        if self.rect.right > SCREEN_WIDTH:
            self.rect.x = 0

    def move_up(self, speed):
        if self.rect.top > (SCREEN_HEIGHT//2):
            self.rect.y -= speed

    def move_down(self, speed):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += speed

    def shoot(self, bullet_handler):
        if (self.shooting_time % self.SHOOTING_TIME) == 0:
            if self.has_cannon:
                bullet_handler.add_bullet(BULLET_ALLY_CANNON_TYPE, self.rect.topleft)
                bullet_handler.add_bullet(BULLET_ALLY_CANNON_TYPE, self.rect.center)
                bullet_handler.add_bullet(BULLET_ALLY_CANNON_TYPE, self.rect.topright)
            else:
                bullet_handler.add_bullet(BULLET_ALLY_TYPE, self.rect.center)

    def activate_power_up(self, power_up):
        self.time_up = power_up.time_up
        if type(power_up) == Shield:
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (self.WIDTH+17, self.HEIGHT-13))
            self.has_shield = True
        elif type(power_up) == Wrench:
            self.has_wrench = True
            if (self.REPAIR+self.energy) > self.max_energy:
                self.energy = self.max_energy
            else:
                self.energy += self.REPAIR
        elif type(power_up) == Thruster:
            self.image = SPACESHIP_THRUSTERS
            self.image = pygame.transform.scale(self.image, (self.WIDTH+10, self.HEIGHT-10))
            self.has_thrusters = True
            self.bonus_speed = 30
            self.speed += self.bonus_speed
        elif type(power_up) == ScoreBonus:
            self.has_score_bonus = True
        elif type(power_up) == Cannon:
            self.has_cannon = True

    def deactivate_power_up(self, power_up):
        if power_up == self.SHIELD:
            self.has_shield = False
            self.image = SPACESHIP
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.WIDTH))
        if power_up == self.THRUSTER:
            self.has_thrusters = False
            self.speed = self.original_speed
            self.image = SPACESHIP
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.WIDTH))
        if power_up == self.SCORE_BONUS:
            self.has_score_bonus = False
        if power_up == self.WRENCH:
            self.has_wrench = False
        if power_up == self.CANNON:
            self.has_cannon = False


    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.energy = 20
        self.is_alive = True
        self.shooting_time = 0
        self.has_shield = False
        self.has_wrench = False
        self.has_thrusters = False
        self.has_score_bonus = False
        self.has_cannon = False
        self.time_power_up_left = 0

