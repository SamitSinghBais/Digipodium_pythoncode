import pgzrun

music.play('m1')

b = Rect((15,15),(100,100))
b = Actor ('i1' , (200,200))


vx, vy = 3,3 # global variable

def draw():
    screen.fill('skyblue')

    #screen.draw.filled_rect(b,'darkgreen')

    b.draw()

def update():
    global vx, vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left < 0:
        vx = -vx
        sounds.s1.play()

    if b.bottom > 600 or b.top < 0:
        vy = -vy
        sounds.s1.play()

pgzrun.go()