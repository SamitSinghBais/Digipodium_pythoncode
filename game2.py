import pgzrun

music.play('m1')
alien = Actor('i1')
alien.topright = 0, 100

WIDTH = 800
HEIGHT = alien.height + 200


def draw():
    screen.clear()
    alien.draw()


def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


score = 0


def keyboard_right(pos):
    global score
    if alien.collidepoint(pos):
        sounds.s1.play()
        alien.i1.image = 'alien_hurt'
        score += 1
    else:
        score -= 1
        print("Nothing here")
    print(score)

pgzrun.go()