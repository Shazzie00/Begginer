import pygame
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (245, 141, 66)
MERCURY = (231, 232, 236)
VENUS = (255, 198, 73)
EARTH = (0, 100, 91)
MARS = (188, 39, 50)
JUPITER = (172, 129, 129)
SATURN = (250, 229, 191)
URANUS = (225, 238, 238)
NEPTUNE = (213, 213, 236)
GREY = (128, 128, 128)
RED = (253, 207, 88)
YELLOW = (255, 255, 0)
GREYED = (90, 90, 90)
SOLID_RED = (255, 0, 0)

pygame.init()

# Screen size
screen_width = 1200
screen_height = 700
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Sharon's Solar System")

done = False
clock = pygame.time.Clock()
angle = 0
angle_2 = 0
angle_3 = 0
angle_4 = 0
angle_5 = 0
angle_6 = 0
angle_7 = 0
angle_8 = 0


# Asteroid


# control for mouse
#shotting star function
def shooting_star(screen, x, y):
    pygame.draw.polygon(screen, ORANGE, [[1103 + x, 639 + y], [1114 + x, 599 + y], [1145 + x, 658 + y]], 25)
    pygame.draw.circle(screen, GREY, [1095 + x, 580 + y], 35, 35)
    pygame.draw.circle(screen, BLACK, [1077 + x, 590 + y], 7, 7)
    pygame.draw.circle(screen, BLACK, [1090 + x, 602 + y], 5, 1)


# control for keyboard
#rocket function
def rocket(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [50 + x, 94 + y, 100, 100], 0)
    pygame.draw.circle(screen, BLACK, [100 + x, 145 + y], 20, 20)
    pygame.draw.line(screen, WHITE, [106 + x, 94 + y], [90 + x, 72 + y], 50)
    pygame.draw.polygon(screen, ORANGE, [[73 + x, 80 + y], [46 + x, 99 + y], [45 + x, 77 + y]], 25)
    pygame.draw.line(screen, WHITE, [106 + x, 194 + y], [90 + x, 216 + y], 50)
    pygame.draw.polygon(screen, ORANGE, [[73 + x, 200 + y], [46 + x, 220 + y], [45 + x, 190 + y]], 25)
    pygame.draw.polygon(screen, MARS, [[175 + x, 140 + y], [151 + x, 92 + y], [151 + x, 182 + y]], 25)


# Planets
radius_one = 100
radius_two = 10

y = 100
x = 100

# Stars
star_x = 0
star_y = 1
SIZE = 2

Amount_Stars = 300
star_list = []

for i in range(Amount_Stars):
    stars_x = random.randrange(screen_width)
    stars_y = random.randrange(screen_height)
    size = random.randrange(1, 5)
    stars = [stars_x, stars_y, size]
    star_list.append(stars)

keyboard_x = 0
keyboard_y = 0

y_speed = 0
x_speed = 0

pygame.mouse.set_visible(True)

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print(mouseX, mouseY)

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
                elif event.key == pygame.K_ESCAPE:
                    done = True

        # --- Game logic should go here

    mouse_position = pygame.mouse.get_pos()
    mouse_x = mouse_position[0] - 1105
    mouse_y = mouse_position[1] - 638

    keyboard_y += y_speed
    keyboard_x += x_speed

    # --- Game logic should go here

    # rocket boundvaries
    #screenlimit for rocket
    if keyboard_x > screen_width - 190:
        keyboard_x = screen_width - 190
    elif keyboard_x < -30:
        keyboard_x = -30
    if keyboard_y < -68:
        keyboard_y = -68
    elif keyboard_y > screen_height - 220:
        keyboard_y = screen_height - 220

    # shooting star boundvaries
    #  screenlimit for asteriod
    if mouse_x > screen_width - 1176:
        mouse_x = screen_width - 1176
    elif mouse_x < -1055:
        mouse_x = -1030
    if mouse_y > screen_height - 681:
        mouse_y = screen_height - 681
    elif mouse_y < -555:
        mouse_y = -530



    screen.fill(BLACK)

    for suns in star_list:
        pygame.draw.circle(screen, WHITE, [suns[star_x], suns[star_y]], suns[SIZE])

    pygame.draw.circle(screen, ORANGE, (600, 360), 75, 75)

    # Moving circle from : https://www.youtube.com/watch?v=xPCnc19aJQ8
    # MERCURY
    mercury_stay = pygame.draw.circle(screen, MERCURY, (600, 360), radius_one, 1)
    mercury_moving = pygame.draw.circle(screen, RED, (x * math.cos(angle) + 600, y * math.sin(angle) + 360), radius_two)
    angle += 0.06

    # VENUS
    venus_stay = pygame.draw.circle(screen, WHITE, (600, 364), radius_one + 40, 1)
    venus_moving = pygame.draw.circle(screen, VENUS,
                                      (x + 140 * math.cos(angle_2) + 500, y + 140 * math.sin(angle_2) + 264),
                                      radius_two + 4, )
    angle_2 += 0.05

    # EARTH
    earth_stay = pygame.draw.circle(screen, WHITE, (600, 364), radius_one + 80, 1)
    earth_moving = pygame.draw.circle(screen, EARTH, (x + 180 * math.cos(angle_3) + 500, y + 180 * math.sin(angle_3)
                                                      + 264), radius_two + 6, )
    angle_3 += 0.04

    # MARS
    mars_stay = pygame.draw.circle(screen, WHITE, (600, 364), radius_one + 120, 1)
    mars_moving = pygame.draw.circle(screen, MARS,
                                     (x + 220 * math.cos(angle_4) + 500, y + 220 * math.sin(angle_4) + 264),
                                     radius_two + 10, )
    angle_4 += 0.03

    # JUPITER
    jupiter_stay = pygame.draw.circle(screen, WHITE, (600, 364), radius_one + 160, 1)
    jupiter_moving = pygame.draw.circle(screen, JUPITER, (x + 260 * math.cos(angle_5) + 500, y + 260 *
                                                          math.sin(angle_5) + 264), radius_two + 15, )
    angle_5 += 0.01

    # SATURN
    saturn_stay = pygame.draw.circle(screen, WHITE, (600, 364), radius_one + 200, 1)
    saturn_moving = pygame.draw.circle(screen, SATURN, (x + 300 * math.cos(angle_6) + 500, y +
                                                        300 * math.sin(angle_6) + 264), radius_two + 15, )
    angle_6 += 0.007

    # URANUS
    uranus_stay = pygame.draw.circle(screen, WHITE, (600, 364), radius_one + 240, 1)
    uranus_moving = pygame.draw.circle(screen, URANUS, (x + 340 * math.cos(angle_7) + 500,
                                                        y + 340 * math.sin(angle_7) + 264), radius_two + 15, )
    angle_7 += 0.005

    # NEPTUNE
    neptune_stay = pygame.draw.circle(screen, WHITE, (600, 360), radius_one + 280, 1)
    neptune_moving = pygame.draw.circle(screen, NEPTUNE, (x + 380 * math.cos(angle_8) + 500,
                                                          y + 350 * math.sin(angle_8) + 264), radius_two + 17, )
    angle_8 += 0.003

    # calling teh functions
    shooting_star(screen, mouse_x, mouse_y)

    rocket(screen, keyboard_x, keyboard_y)

    # --- Drawing code should go here

    # notes on coordinates rectangles: going (left) first one 500 to 0 opposite
    # notes on coordinates rectangles: going (down) first one 350 to 0 opposite
    # end
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
