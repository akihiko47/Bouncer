import pygame
import random

pygame.init()

display_width = 800
display_height = 800

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Bouncer!")

try:
    icon = pygame.image.load("bouncer_icon.png")
    pygame.display.set_icon(icon)
except:
    print("Не получилось загрузить иконку игры!")

plr_height = 20
plr_width = 20
p_x = display_width // 2
p_y = display_height // 1.2

b_x = display_width // 2
b_y = display_height // 2

plr_speed = 5
b_speed = 5

b_move_x, b_move_y = random.randint(-b_speed, b_speed), random.randint(-b_speed, b_speed)
b_radius = 50

score = 0
score_mult = 0

difficulty = 0

font = pygame.font.SysFont('silkscreen.ttf', 32)


def print_score(msg):
    screen_text = font.render(msg, True, (255, 255, 255))
    display.blit(screen_text, [15, 15])


def check_hit(p_x, p_y, b_x, b_y):
    if p_x + plr_width >= b_x - b_radius//2:
        if p_x - plr_width <= b_x + b_radius//2:
            if p_y + plr_height >= b_y - b_radius//2:
                if p_y - plr_height <= b_y + b_radius//2:
                    game_over()
                    return True
    return False


def game_over():
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("game over")
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()


clock = pygame.time.Clock()

in_game = True

while in_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_game = False
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if 10 <= p_y <= 790:
            p_y -= plr_speed
    if keys[pygame.K_DOWN]:
        if 10 <= p_y <= 790:
            p_y += plr_speed
    if keys[pygame.K_LEFT]:
        if 10 <= p_x <= 790:
            p_x -= plr_speed
    if keys[pygame.K_RIGHT]:
        if 10 <= p_x <= 790:
            p_x += plr_speed

    if p_x <= 10:
        p_x = 10
    if p_x >= 770:
        p_x = 770
    if p_y <= 10:
        p_y = 10
    if p_y >= 770:
        p_y = 770

    if score == 10 and difficulty == 0:
        difficulty = 1
        b_move_x = round(b_move_x * 1.5)
        b_move_y = round(b_move_y * 1.5)
    if score == 20 and difficulty == 1:
        difficulty = 2
        b_move_x = round(b_move_x * 1.3)
        b_move_y = round(b_move_y * 1.3)
    if score == 30 and difficulty == 2:
        difficulty = 3
        b_move_x = round(b_move_x * 1.3)
        b_move_y = round(b_move_y * 1.3)
    if score == 40 and difficulty == 3:
        difficulty = 4
        b_move_x = round(b_move_x * 1.2)
        b_move_y = round(b_move_y * 1.2)
    if score == 50 and difficulty == 4:
        difficulty = 5
        b_move_x = round(b_move_x * 1.5)
        b_move_y = round(b_move_y * 1.5)

    b_x += b_move_x
    b_y += b_move_y

    if b_x <= 10 + b_radius or b_x >= 790 - b_radius:
        b_move_x = -b_move_x
    if b_y <= 10 + b_radius or b_y >= 790 - b_radius:
        b_move_y = -b_move_y

    display.fill((255, 255, 255))
    pygame.draw.rect(display, (50, 0, 255), (10, 10, 780, 780))
    score_area = pygame.draw.rect(display, (0, 0, 150), (200, 200, 400, 400))

    pygame.draw.rect(display, (255, 255, 255), (int(p_x), int(p_y), plr_width, plr_height))

    pygame.draw.circle(display, (200, 0, 0), (b_x, b_y), b_radius)

    if 200 <= p_x <= 580 and 200 <= p_y <= 580:
        score_mult = score_mult + 1

    if score_mult >= 100:
        score = score + 1
        score_mult = 0
    print_score("Score: " + str(score))

    if check_hit(p_x, p_y, b_x, b_y):
        in_game = False

    pygame.display.update()
    clock.tick(100)
