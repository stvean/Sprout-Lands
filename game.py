import random
import pgzrun
from pgzhelper import *

HEIGHT = 800
WIDTH = 1000

bg = Actor('map')
bg.scale = 2
bg.pos =(WIDTH/2, HEIGHT/2)

apple_img= 'plant/tile020'
bush_img = 'plant/tile027'
strawberry_img = 'plant/tile031'


apple_list = []
bush_list = []
strawberry_list = []

player_down = [
'player/tile000',
'player/tile001',
'player/tile002',
'player/tile003',
]
player_up = [
'player/tile004',
'player/tile005',
'player/tile006',
'player/tile007',
]

player_left = [
'player/tile008',
'player/tile009',
'player/tile010',
'player/tile011',
]

player_right = [
    'player/tile012',
    'player/tile013',
    'player/tile014',
    'player/tile015',
]

player = Actor(player_down[0])
player.pos = (WIDTH/2, HEIGHT/2)
player.images = player_down
player.scale = 3
player.score = 0

chicken_img = [
    'chicken/tile000',
    'chicken/tile001', 
    'chicken/tile004',    
    'chicken/tile005',    
    'chicken/tile006',
    'chicken/tile007',
]
chicken_list = []

def update():
    player.animate()
    if keyboard.UP:
        player.y -= 5
        if player.images != player_up:   
            player.images = player_up
    if keyboard.DOWN:
        player.y += 5
        if player.images != player_down:
            player.images = player_down
    if keyboard.LEFT:
        player.x -= 5
        if player.images != player_left:
            player.images = player_left
    if keyboard.RIGHT:
        player.x += 5
        if player.images != player_right:
            player.images = player_right

    if player.top <0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    if random.randint(0,100)<1:
        apple = Actor(apple_img)
        apple.scale = 2
        apple.pos = (random.randint(50, WIDTH-50), random.randint(100, HEIGHT-100))
        apple_list.append(apple)

    if random.randint(0,100)<1:
        bush = Actor(bush_img)
        bush.scale = 3
        bush.pos = (random.randint(50, WIDTH-50), random.randint(100, HEIGHT-100))
        bush_list.append(bush)

    if random.randint(0,100)<1:
        strawberry = Actor(strawberry_img)
        strawberry.scale = 2
        strawberry.pos = (random.randint(50, WIDTH-50), random.randint(100, HEIGHT-100))
        strawberry_list.append(strawberry)

    if random.randint(0,100)<1:
        chicken= Actor(chicken_img[0])
        chicken.images = chicken_img
        chicken.scale = 2
        chicken.pos = (random.randint(50, WIDTH-50), random.randint(100, HEIGHT-100))
        chicken_list.append(chicken)
    
    for c in chicken_list:
        c.animate()
        if player.collide_pixel(c):
            player.score += 1
            sounds.coin_sound.play()
            chicken_list.remove(c)
            break
    
    for a in apple_list:
        if player.collide_pixel(a):
            player.score += 1
            sounds.coin_sound.play()
            apple_list.remove(a)
            break
    
    for b in bush_list:
        if player.collide_pixel(b):
            player.score += 2
            sounds.coin_sound.play()
            bush_list.remove(b)
            break

    for s in strawberry_list:
        if player.collide_pixel(s):
            player.score += 1
            sounds.coin_sound.play()
            strawberry_list.remove(s)
            break
        
     

def draw():
    screen.clear()
    bg.draw() 
    screen.draw.text(str(player.score), (35, 95), align = 'center', fontsize = 60)  
    for a in apple_list:
        a.draw()
    for b in bush_list:
        b.draw()
    for s in strawberry_list:
        s.draw()
    for c in chicken_list:
        c.draw()
    player.draw()
    
pgzrun.go()

