from pygame import*

class GameSprite(sprite.Sprite): #
   def __init__(self, image_player, img_x, img_y, speed, w_r,h_r):
       super().__init__()
       self.image = transform.scale(image.load(image_player),(w_r,h_r))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x = img_x
       self.rect.y = img_y
  
   def show_s(self):
       window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left_player(self):
        keys = key.ger_pres