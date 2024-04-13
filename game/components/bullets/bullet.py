class Bullet:
    def __init__(self, image, center):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.is_alive = True

    def update(self, object):
        if self.rect.colliderect(object.rect):
            object.energy -= 1
            self.is_alive = False
        if object.energy == 0:
            object.is_alive = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
