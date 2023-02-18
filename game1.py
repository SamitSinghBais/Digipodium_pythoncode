import pgzrun

#music.play('sound1')
b = Rect((50,50),(100,100))
vx, vy = 3,5 # global variable

def draw():
    screen.fill('black')
    screen.draw.filled_rect(b,'green')
    #b.draw()
def update():
    global vx, vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left < 0:
        vx = -vx
        #sounds.s1.play()
    if b.bottom > 600 or b.top < 0:
        vy = -vy
        #sounds.si.play()
pgzrun.go()