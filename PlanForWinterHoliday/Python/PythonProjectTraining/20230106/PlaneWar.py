import pygame
from pygame import *
import time
import random

def main():
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50,40))
            self.image.fill((255,255,0))
            self.rect = self.image.get_rect()
            self.rect.centerx = 250
            self.rect.bottom = 600 - 40

        def update(self):
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                self.rect.x += 3
            if key_pressed[pygame.K_LEFT]:
                self.rect.x -= 3
            if key_pressed[pygame.K_UP]:
                self.rect.y -= 3
            if key_pressed[pygame.K_DOWN]:
                self.rect.y += 3
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > 600:
                self.rect.bottom = 600
            if self.rect.right > 500:
                self.rect.right = 500
            if self.rect.left <= 0:
                self.rect.left = 0

        def shoot(self):
            bullet = Bullet(self.rect.centerx,self.rect.centery)
            all_sprites.add(bullet)
            bullets.add(bullet)
    class Rock(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((30,30))
            self.image.fill((255,0,255))
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(0,500-self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,3)
            self.speedx = random.randrange(-2, 2)

        def update(self):
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            if self.rect.top>600 or self.rect.left>500 or self.rect.right < 0:
                self.rect.x = random.randrange(0, 500 - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 3)
                self.speedx = random.randrange(-2, 2)
    class Bullet(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((2,20))
            self.image.fill((0,255,255))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speedy = -10


        def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom <0:
                self.kill()
    # def main():
    pygame.init()
    screen = pygame.display.set_mode((500,600))
    pygame.display.set_caption("飞机大战")
    clock=pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    players = pygame.sprite.Group()
    player=Player()
    players.add(player)
    all_sprites.add(player)
    for i in range(8):
        rock=Rock()
        all_sprites.add(rock)
        rocks.add(rock)
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()


        all_sprites.update()
        hits_rockandbullet=pygame.sprite.groupcollide(rocks,bullets,True,True)
        for hit in hits_rockandbullet:
            r=Rock()
            all_sprites.add(r)
            rocks.add(r)
        hits_rockandbullet2 = pygame.sprite.spritecollide(player, rocks, False)
        print(hits_rockandbullet2)
        if hits_rockandbullet2:
            running=False
        # if hits_rockandbullet2=={}:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             running = False
        #         elif event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_r:
        #                 main()
        screen.fill((255,255,255))
        all_sprites.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        print('正常退出游戏')
        pass
