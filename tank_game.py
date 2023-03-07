import pgzrun
import random

WIDTH=800
HEIGHT=600

tank = Actor('tank_top')
tank.y = 575
tank.x = 400
tank.angle = 90

background = Actor('grass')

walls = []
for x in range(10):
    for y in range(6):
        if random.randint(0, 100) < 50:
            wall = Actor('wall')
            wall.x = x * 50 + 25
            wall.y = y * 50 + 25 + 50
            walls.append(wall)

bullets = []
bullet_holdoff = 0

def update():
    global bullet_holdoff

    # This part is for the tank
    original_x = tank.x
    original_y = tank.y

    if keyboard.left:
        tank.x = tank.x - 1
        tank.angle = 360
        sounds.s4.play()
    elif keyboard.right:
        tank.x = tank.x + 1
        tank.angle = 180
        sounds.s4.play()
    elif keyboard.up:
        tank.y = tank.y - 1
        tank.angle = 270
        sounds.s4.play()
    elif keyboard.down:
        tank.y = tank.y + 1
        tank.angle = 90
        sounds.s4.play()

    if tank.collidelist(walls) != -1:
        tank.x = original_x
        tank.y = original_y

    if tank.x < 0 or tank.x > 800 or tank.y < 0 or tank.y > 600:
        tank.x = original_x
        tank.y = original_y

    # This part is for the bullet
    if bullet_holdoff == 0:
        if keyboard.space:
            bullet = Actor('bullet-tank')
            bullet.angle = tank.angle
            print(bullet.angle)
            bullet.x = tank.x
            bullet.y = tank.y
            bullets.append(bullet)
            bullet_holdoff = 100
            sounds.bullet_sound.play()
    else:
        bullet_holdoff = bullet_holdoff - 1

    for bullet in bullets:
        if bullet.angle == 360:
            bullet.x -= 5
        elif bullet.angle == 90:
            bullet.y = bullet.y + 5
        elif bullet.angle == 180:
            bullet.x = bullet.x + 5
        elif bullet.angle == 270:
            bullet.y = bullet.y - 5

    for bullet in bullets:
        wall_index = bullet.collidelist(walls)
        if wall_index != -1:
            del walls[wall_index]
            bullets.remove(bullet)
        if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
            bullets.remove(bullet)


def draw():
    screen.fill((0,0,0))
    background.draw()
    tank.draw()
    for bullet in bullets:
        bullet.draw()
    for wall in walls:
        wall.draw()

pgzrun.go()