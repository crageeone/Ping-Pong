from pygame import *
from random import randint
init()
#добавление файлов
img_bg = "background.jpg"
img_ball = "ball.jpg"
img_player = "player.jpg"
#создание окна
win_width = 800
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_bg), (win_width, win_height))
#создание классов
class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      sprite.Sprite.__init__(self)
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
#метод, отрисовывающий героя на окне
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
  #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
#цикл игры
game = True
finish = False
#загрузка спрайтов и фона
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        display.update()