import pygame
import random

colour=[(127, 127, 127), (255, 255, 255), (255, 0, 0), (0, 0, 255), (255, 255, 0),(0, 255, 255),(255, 0, 255)]
color_change=random.choice(colour)
color_changee=random.choice(colour)
 

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BIRD_SIZE = 20
BIRD_COLOR = color_change
BIRD_X = 50
bird_y = SCREEN_HEIGHT // 2

PIPE_WIDTH = 50
PIPE_GAP = 150
PIPE_COLOR = color_changee
pipe_x = SCREEN_WIDTH
pipe_height = random.randint(150, 400)
GRAVITY = 2.5
JUMP_VELOCITY = -50

score = 0


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")


clock = pygame.time.Clock()


def draw_bird(x, y):
    pygame.draw.circle(screen, BIRD_COLOR, (x, y), BIRD_SIZE)

def draw_pipe(x, height):
    pygame.draw.rect(screen, PIPE_COLOR, (x, 0, PIPE_WIDTH, height))
    pygame.draw.rect(screen, PIPE_COLOR, (x, height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - height - PIPE_GAP))

def check_collision(x, y):
    if y < 0 or y > SCREEN_HEIGHT:
        return True
    if x + BIRD_SIZE > pipe_x and x - BIRD_SIZE < pipe_x + PIPE_WIDTH:
        if y - BIRD_SIZE < pipe_height or y + BIRD_SIZE > pipe_height + PIPE_GAP:
            return True
    return False


def bird_color():
    BIRD_COLOR
    
def update_score():
    global score
    score += 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y += JUMP_VELOCITY

    bird_y += GRAVITY

    if check_collision(BIRD_X, bird_y):
        running = False

    
    if BIRD_X > pipe_x + PIPE_WIDTH:
        update_score()
        bird_color()

  
    pipe_x -= 5
    if pipe_x < -PIPE_WIDTH:
        pipe_x = SCREEN_WIDTH
        pipe_height = random.randint(150, 400)


    screen.fill(WHITE)
    
    draw_bird(BIRD_X, int(bird_y))
    draw_pipe(pipe_x, pipe_height)

    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))
    x=45
    if score >= 20:
        x+=10
    elif score >= 200:
        x+=20
    elif score >= 300:
        x+=40
                   

   
    pygame.display.flip()

   
    clock.tick(x)

pygame.quit()
