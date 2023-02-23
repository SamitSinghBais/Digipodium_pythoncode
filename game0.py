import pgzrun

b = Rect((50,50),(100,100))

vx, vy = 5,5 # global variable

def draw():
    screen.fill('skyblue')
    screen.draw.filled_rect(b,'darkgreen')

def update():
    global vx, vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left < 0:
        vx = -vx
        

    if b.bottom > 600 or b.top < 0:
        vy = -vy
       
pgzrun.go()