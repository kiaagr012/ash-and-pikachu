import pgzrun
from random import randint
WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

ash = Actor('Ash.png')
posA = pos('Ash.png')

pikachu = Actor('pikachu.png')
posP = pos('pikachu.png')

def draw():
    screen.blit('background', (0,0))
    ash.draw()
    pikachu.draw()
    screen.draw.text('score : '+ str(score), color = 'red', topleft = (10,10))

if game_over:
        screen.fill('red')
        screen.draw.text("Time's up! YOUR FINAL SCORE: "+ str(score), midpoint=(WIDTH/2, 10), fontzize=40, color='pink')
        

def place_pikachu():
    pikachu.x = randint(70,(WIDTH-70))
    pikachu.y = randint(70,(HEIGHT-70))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        ash.x = ash.x -2
    if keyboard.right:
        ash.x = ash.x +2
    if keyboard.up:
        ash.y = ash.y -2
    if keyboard.down:
        ash.y = ash.y +2

    pikachu_collected = ash.colliderect(pikachu)

    if pikachu_collected:
        score = score+10
        place_pikachu()

clock.schedule(time_up, 60.0)


pgzrun.go()