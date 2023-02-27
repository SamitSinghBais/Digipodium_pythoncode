import pgzrun


WIDTH = 800
HEIGHT = 600


image = Actor('i2')
image.x = 400
image.y = HEIGHT-100

vx,vy = 20,20

def update():
    if keyboard.left:
        image.x -=vx 
    elif keyboard.right:
        image.x +=vx
    elif keyboard.up:
        image.y -=vy
    elif keyboard.down:
        image.y +=vy


    if image.x <= 75:
        image.x = 75
        sounds.s2.play()
    elif image.x >= 725:
        image.x = 725
        sounds.s2.play()
    if image.y <= 75:
        image.y = 75
        sounds.s2.play()
    elif image.y >= 520:
        image.y = 520
        sounds.s2.play()


     
def draw():
    #screen.fill("black")
    screen.blit("ks1", pos=(0,0))
    image.draw()


pgzrun.go()
     