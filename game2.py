import pgzrun

music.play('m1')
alien = Actor('images')
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20


def draw():
    screen.clear()
    alien.draw()


def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


score = 0


def on_mouse_down(pos):
    global score
    if alien.collidepoint(pos):
        sounds.s1.play()
        alien.images.image = 'alien_hurt'
        score += 1
    else:
        score -= 1
        print("Nothing here")
    print(score)

pgzrun.go()