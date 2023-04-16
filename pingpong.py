from pygame import *
'''Необходимые классы'''


#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


#игровая сцена:
win_width = 600
win_height = 500
img_bg = "background.jpg"
back = transform.scale(image.load(img_bg), (win_width, win_height))

window = display.set_mode((win_width, win_height))

#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60


#создания мяча и ракетки   
racket1 = Player('player.png', 30, 200, 4, 50, 150) 
racket2 = Player('player.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 70, 50)


font.init()
font = font.Font(None, 45)
tcount1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
tcount2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

count1 = 0
count2 = 0

speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if finish != True:
        window.blit(back, (0,0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
      
       #если мяч достигает границ экрана, меняем направление его движения
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1


        #если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
        if ball.rect.x < 0:
            count2+=1
            ball.rect.x = 300
            ball.rect.y = 250
           

        #если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
        if ball.rect.x > win_width:
            count1+=1
            ball.rect.x = 300
            ball.rect.y = 250
           

        
        racket1.reset()
        racket2.reset()
        ball.reset()
        tcount1 = font.render(str(count1), True, (180, 0, 0))
        tcount2 = font.render(str(count2), True, (180, 0, 0))
        window.blit(tcount1, (260, 25))
        window.blit(tcount2, (325, 25))

    display.update()
    clock.tick(FPS)
