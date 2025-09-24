import pygame as pg
import math

def calculate_acceleration(x, y, mass):
    dx = (sun_x-x)
    dy = (sun_y-y)
    r = math.hypot(dx, dy)

    F = (G*mass_sun*mass)/(r*r)

    F_x = F*dx/r
    F_y = F*dy/r

    ax = F_x/mass
    ay = F_y/mass

    return ax, ay

pg.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 950

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

running = True
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 69, 0)
PURPLE = (114, 9, 183)
BROWN = (205,133,63)
WHITE = (255, 255, 255)
SKY = (135, 206, 235)
AQUA = (60, 100, 200)

mass_sun = 330
G = 9.8
mass_earth = 1.3
mass_mars = 0.1
mass_mercury = 0.055
mass_venus = 1.0
mass_jupiter = 78
mass_saturn = 23
mass_uranus = 3.6
mass_neptune = 4.3

sun_x, sun_y = SCREEN_WIDTH//2, SCREEN_HEIGHT//2
earth_x, earth_y = sun_x+150, sun_y
mars_x, mars_y = sun_x+180, sun_y
mercury_x, mercury_y = sun_x+70, sun_y
venus_x, venus_y = sun_x+100, sun_y
jupiter_x, jupiter_y = sun_x+250, sun_y
saturn_x, saturn_y = sun_x+310, sun_y
uranus_x, uranus_y = sun_x+385, sun_y
neptune_x, neptune_y = sun_x+425, sun_y

vel_x, vel_y = 0, math.sqrt((G*mass_sun)/150)
mars_vel_x, mars_vel_y = 0, math.sqrt((G*mass_sun)/180)
mercury_vel_x, mercury_vel_y = 0, math.sqrt((G*mass_sun)/70)
venus_velx, venus_vely = 0, math.sqrt((G*mass_sun)/100)
jupiter_velX, jupiter_velY = 0, math.sqrt((G*mass_sun)/250)
saturn_velX, saturn_velY = 0, math.sqrt((G*mass_sun)/310)
uranus_velX, uranus_velY = 0, math.sqrt((G*mass_sun)/385)
neptune_velX, neptune_velY = 0, math.sqrt((G*mass_sun)/425)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill('black')
    
    a_x, a_y = calculate_acceleration(earth_x, earth_y, mass_earth)
    ra_x, ra_y = calculate_acceleration(mars_x, mars_y, mass_mars)
    ma_x, ma_y = calculate_acceleration(mercury_x, mercury_y, mass_mercury)
    v_x, v_y = calculate_acceleration(venus_x, venus_y, mass_venus)
    jx, jy = calculate_acceleration(jupiter_x, jupiter_y, mass_jupiter)
    sat_x, sat_y = calculate_acceleration(saturn_x, saturn_y, mass_saturn)
    ura_x, ura_y = calculate_acceleration(uranus_x, uranus_y, mass_uranus)
    neptuneX, neptuneY = calculate_acceleration(neptune_x, neptune_y, mass_neptune)

    # calculating velocity components
    vel_x += a_x
    vel_y += a_y
    mars_vel_x += ra_x
    mars_vel_y += ra_y
    mercury_vel_x += ma_x
    mercury_vel_y += ma_y
    venus_velx += v_x
    venus_vely += v_y
    jupiter_velX += jx
    jupiter_velY += jy
    saturn_velX += sat_x
    saturn_velY += sat_y
    uranus_velX += ura_x
    uranus_velY += ura_y
    neptune_velX += neptuneX
    neptune_velY += neptuneY

    earth_x += vel_x
    earth_y += vel_y
    mars_x += mars_vel_x
    mars_y += mars_vel_y
    mercury_x += mercury_vel_x
    mercury_y += mercury_vel_y
    venus_x += venus_velx
    venus_y += venus_vely
    jupiter_x += jupiter_velX
    jupiter_y += jupiter_velY
    saturn_x += saturn_velX
    saturn_y += saturn_velY
    uranus_x += uranus_velX
    uranus_y += uranus_velY
    neptune_x += neptune_velX
    neptune_y += neptune_velY

    pg.draw.circle(screen, YELLOW, (sun_x, sun_y), radius=45, width=0)

    pg.draw.circle(screen, WHITE, (sun_x, sun_y), radius=150, width=1)      # orbit
    pg.draw.circle(screen, BLUE, (earth_x, earth_y), radius=15, width=0)    # EARTH

    pg.draw.circle(screen, WHITE, (sun_x, sun_y), radius=180, width=1)      # orbit
    pg.draw.circle(screen, RED, (mars_x, mars_y), radius=8, width=0)        # MARS
    
    pg.draw.circle(screen, WHITE, (sun_x, sun_y), radius=70, width=1)       # orbit
    pg.draw.circle(screen, ORANGE, (mercury_x, mercury_y), radius=4, width=0) # MERCURY

    pg.draw.circle(screen, WHITE, (sun_x, sun_y), radius=100, width=1)       # orbit
    pg.draw.circle(screen, PURPLE, (venus_x, venus_y), radius=7, width=0)      # VENUS

    pg.draw.circle(screen, WHITE, (sun_x, sun_y), radius=250, width=1)       # orbit
    pg.draw.circle(screen, BROWN, (jupiter_x, jupiter_y), radius=30, width=0)   # JUPITER

    pg.draw.circle(screen, WHITE, (sun_x, sun_y), radius=310, width=1)       # orbit
    pg.draw.circle(screen, WHITE, (saturn_x, saturn_y), radius=23, width=0)  # SATURN

    pg.draw.circle(screen, WHITE, (sun_x, sun_y), radius=385, width=1)       # orbit
    pg.draw.circle(screen, SKY, (uranus_x, uranus_y), radius=18, width=0)  # URANUS

    pg.draw.circle(screen, WHITE, (sun_x, sun_y), radius=425, width=1)       # orbit
    pg.draw.circle(screen, AQUA, (neptune_x, neptune_y), radius=17, width=0)  # NEPTUNE


    pg.display.flip()
    pg.display.set_caption("Solar System")
    clock.tick(40)


pg.quit()