import pygame
import random
from os import path

WIDTH = 1400
HEIGHT = 910
FPS = 60

#initialize pygame and create our window

#define colours
WHITE = (255)
BLACK = (0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (147, 128, 160)
ORANGE = (216, 79, 15)
YELLOW = (255, 212, 5)
GREY = (140)

#set up iomage folder
img_dir = path.join(path.dirname(__file__), 'img')

class Player(pygame.sprite.Sprite):
    #sprite for the player
    #a class is made up of multiple functions
    def __init__(self): #initializes the sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = HEIGHT - 20
       
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8   
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if (self.rect.left < 0):
            self.rect.left = 0
        if (self.rect.right > WIDTH):
             self.rect.right = WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        
        
        
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3,3)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,8)
            self.speedx = random.randrange(-3,3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -14
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

        
pygame.init() # initializes pygame
pygame.mixer.init() #gives the game sound
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Wolflet Game")
clock = pygame.time.Clock()

#load images
player_img = pygame.image.load(path.join(img_dir, "Rampion.png")).convert()
mob_img = pygame.image.load(path.join(img_dir, "Avada Kedavra.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "Stupefy.png")).convert()

#Game loop
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()
for i in range(7):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
bullets = pygame.sprite.Group()
    
running = True
while running:
    # keep the loop running at the right speed
    clock.tick(FPS)
    #process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    #update
    all_sprites.update()
    
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
        print("GAME OVER")
   
    
    #draw(render) given input
    screen.fill(BLACK)
    
    all_sprites.draw(screen)
    #after drawing everything flip the screen
    pygame.display.flip()
pygame.quit()
