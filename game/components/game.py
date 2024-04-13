import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE
from game.components.spaceship import SpaceShip
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.utils import text_utils
from game.components.power_ups.power_up_handler import PowerUpHandler

WRENCH_POWER_UP = 'Wrench'
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.waiting = False
        self.endgame = False
        self.last_wave = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = SpaceShip(self.game_speed)
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.power_up_handler = PowerUpHandler()
        self.max_score = 0
        self.number_deaths = 0
        self.waves = [15,40,90,110]
        self.current_wave = 0

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.playing and not self.waiting and not self.endgame:
                self.reset()
                self.playing = True
            elif event.type == pygame.KEYDOWN and not self.playing and self.waiting and not self.endgame:
                self.playing = True
                self.waiting = False
                self.current_wave += 1
            elif event.type == pygame.KEYDOWN and not self.playing and not self.waiting and self.endgame:
                 self.endgame = False

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.bullet_handler, self.power_up_handler)
            self.enemy_handler.update(self.bullet_handler, self.last_wave)
            self.bullet_handler.update(self.player, self.enemy_handler)
            self.power_up_handler.update(self.player)
            if self.player.has_score_bonus:
                self.enemy_handler.bonus = True
            else:
                self.enemy_handler.bonus = False
            self.player.score = self.enemy_handler.enemies_destroyed
            if self.player.score > self.max_score:
                self.max_score = self.player.score
            if not self.player.is_alive:
                pygame.time.delay(300)
                self.playing = False
                self.number_deaths += 1
                if self.player.score > self.max_score:
                    self.max_score = self.player.score

    def draw(self):
        self.draw_background()
        if self.playing and not self.waiting and self.current_wave < (len(self.waves)-1):
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.draw_score()
            if self.player.score >= self.waves[self.current_wave]:
                self.playing = False
                self.waiting = True
                self.endgame = False
                self.draw_background()
        elif self.playing and not self.waiting and self.current_wave == (len(self.waves)-1):
            self.last_wave = True
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            try:
                if self.enemy_handler.enemies[0].lifes == 0:
                    self.playing = False
                    self.waiting = True
                    self.endgame = False
            except:
                pass
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.draw_score()
        elif not self.endgame and not self.playing and self.waiting:
            self.draw_lobby_wave()
            if self.current_wave == (len(self.waves)-1):
                self.playing = False
                self.waiting = False
                self.endgame = True
        elif not self.playing and not self.waiting and not self.endgame:
            self.draw_menu()
        elif not self.playing and not self.waiting and self.endgame:
            self.draw_endgame()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_menu(self):
        if self.number_deaths == 0:
            text, text_rect = text_utils.get_message('Press Any Key To start', 30, WHITE)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message('Press Any Key to Restart', 30, WHITE)
            score, score_rect = text_utils.get_message(f'Your score was {self.player.score}', 30, WHITE, height=SCREEN_HEIGHT//2 + 50)
            max_score, max_score_rect = text_utils.get_message(f'Your max score is {self.max_score}', 30, WHITE, height=SCREEN_HEIGHT//2 + 100)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(max_score, max_score_rect)

    def draw_endgame(self):
        text, text_rect = text_utils.get_message('Congratulations you have completed all waves!', 30, WHITE)
        score, score_rect = text_utils.get_message(f'Your score was {self.player.score}', 30, WHITE, height=SCREEN_HEIGHT//2 + 50)
        max_score, max_score_rect = text_utils.get_message(f'Your max score is {self.max_score}', 30, WHITE, height=SCREEN_HEIGHT//2 + 100)
        text2, text2_rect = text_utils.get_message('Press Any Key to Finish', 30, WHITE, height=SCREEN_HEIGHT//2 + 150)
        self.screen.blit(text, text_rect)
        self.screen.blit(score, score_rect)
        self.screen.blit(max_score, max_score_rect)
        self.screen.blit(text2, text2_rect)

    def draw_lobby_wave(self):
        wave_completed, text_wave_completed = text_utils.get_message(f'Wave {self.current_wave} Completed', 30, WHITE)
        self.screen.blit(wave_completed, text_wave_completed)
        score, score_rect = text_utils.get_message(f'Press Any Key to continue to the next wave', 30, WHITE, height=SCREEN_HEIGHT//2 + 50)
        self.screen.blit(score, score_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.player.score}',20, WHITE,1000,40)
        max_score, max_score_rect = text_utils.get_message(f'Your max score is: {self.max_score}', 20, WHITE, 980, 80)
        energy, energy_rect = text_utils.get_message(f'Spaceship energy: {self.player.energy}',20, WHITE,980,120)
        wave, score_wave = text_utils.get_message(f'Current wave: {self.current_wave}',20, WHITE,1000,500)
        objective, score_objective = text_utils.get_message(f'Wave objective: {self.waves[self.current_wave]}',20, WHITE,1000,530)
        self.screen.blit(score, score_rect)
        self.screen.blit(max_score, max_score_rect)
        self.screen.blit(energy, energy_rect)
        self.screen.blit(wave, score_wave)
        self.screen.blit(objective, score_objective)
        if len(self.power_up_handler.power_ups) > 0:
            if self.power_up_handler.power_ups[0].is_used:
                power_up, power_up_rect = text_utils.get_message(f'Active Power Up: {self.power_up_handler.power_ups[0].name}',20, WHITE,940,160)
                self.screen.blit(power_up, power_up_rect)
                if self.power_up_handler.power_ups[0].name != WRENCH_POWER_UP:
                    power_up_time, power_up_time_rect = text_utils.get_message(f'Power Up time left:',20, WHITE,900,190)
                    self.screen.blit(power_up_time, power_up_time_rect)
                    power_up_time_n, power_up_time_n_rect = text_utils.get_message(f'{self.player.time_power_up_left} seg.',20, WHITE,1050,190)
                    self.screen.blit(power_up_time_n, power_up_time_n_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_up_handler.reset()
        self.player.score = 0
        self.current_wave = 0
        self.playing = False
        self.waiting = False
        self.endgame = False
        self.last_wave = False
