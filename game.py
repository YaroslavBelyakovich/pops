from pygame import*

class GameSprite(sprite.Sprite): 
   def __init__(self, image_player, player_x, player_y, speed, w_r,h_r):
       super().__init__()
       self.image = transform.scale(image.load(image_player),(w_r,h_r))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
  
   def reset(self):
       window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_left_player(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_width - 80:
           self.rect.y += self.speed

   def update_right_player(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_width - 80:
           self.rect.y += self.speed

back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()

platform1 = Player('uuu.png',30,200,4,50,150)
platform2 = Player('uuu.png',520,200,4,50,150)
myach = GameSprite('unnamed.png',200,200,4,50,50)

font.init()
font = font.Font(None,35)
lose1 = font.render('Player 1 lose',True,(180,0,0))
lose2 = font.render('Player 2 lose',True,(180,0,0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        platform1.update_left_player()
        platform2.update_right_player()

        myach.rect.x += speed_x
        myach.rect.y += speed_y

        if sprite.collide_rect(platform1,myach) or sprite.collide_rect(platform2,myach):
            speed_x *= -1
            speed_y *= 1

        if myach.rect.y > win_height-50 or myach.rect.y < 0:
            speed_y *= -1

        if myach.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
            game_over = True

        if myach.rect.x > win_width:
            finish = True
            window.blit(lose2,(200,200))
            game_over = True

        platform1.reset()
        platform2.reset()
        myach.reset()


        display.update()
        clock.tick(60)