import pygame
import sys
import traceback

pygame.init()
bg_size=width,height=400,700
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战")

class MyPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        self.image1=pygame.Surface((40,40))
        self.image1.fill((30,144,255))
        self.image2=pygame.Surface((30.30))
        self.image1.fill((30, 144, 255))
        self.destory_image=[]
        self.destory_image.extend([
            pygame.Surface((20, 20)),
            pygame.Surface((10, 10)),
            pygame.Surface((5, 5)),
            pygame.Surface((0, 0))
        ])
        for i in self.destory_image:
            i.fill((30,144,255))
        self.width=bg_size[0]
        self.height=bg_size[1]
        self.rect=self.image1.get_rect()
        self.rect.left=(self.width-self.rect.width)//2
        self.rect.top=self.height-self.rect.height-60
        self.myPlaneSpeed=10
        self.active=True
        self.invincible=True
        self.mask=pygame.mask.from_surface(self.image1)

    def moveUp(self):
        if self.rect.top>0:
            self.rect.top-=self.myPlaneSpeed
        else:
            self.rect.top=0

    def moveDown(self):
        if self.rect.bottom<self.height-60:
            self.rect.bottom+=self.myPlaneSpeed
        else:
            self.rect.bottom=self.height-60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.myPlaneSpeed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.myPlaneSpeed
        else:
            self.rect.right = self.width

    def reset(self):
        self.active=True
        self.invincible=True
        self.rect.left=(self.width-self.rect.width)//2
        self.rect.top = self.height - self.rect.height - 60

def main():
    clock=pygame.time.Clock()
    me=MyPlane(bg_size)
    lift_num=3
    paused=False
    switch_image=True
    delay=100
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            me.moveUp()
        if key_pressed[pygame.K_DOWN]:
            me.moveDown()
        if key_pressed[pygame.K_LEFT]:
            me.moveLeft()
        if key_pressed[pygame.K_RIGHT]:
            me.moveRight()
        screen.fill((255, 255, 255))
        if paused==False and lift_num>0:
            if me.active:
                if switch_image:
                    screen.blit(me.image1,me.rect)
                else:
                    screen.blit(me.image2,me.rect)
            else:
                print("飞机损毁")
            delay -= 1
            if delay==0:
                delay=100
            if delay%5==0:
                switch_image=not switch_image
        screen.blit(me.image1,me.rect)
        pygame.display.flip()
        clock.tick(60)

if __name__=="__mian__":
    try:
        main()
    except SystemExit:
        print("游戏正常退出")
        pass
    except:
        traceback.print_exc()
        pygame.quit()