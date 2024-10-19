import pygame, random, sys

pos_data = [(10, 523), (70, 523), (130, 523), (190, 523), (250, 523), (310, 523), (370, 523), (430, 523), (490, 523), (550, 523), 
        (550, 466), (490, 466), (430, 466), (370, 466), (310, 466), (250, 466), (190, 466), (130, 466), (70, 466), (10, 466), 
        (10, 409), (70, 409), (130, 409), (190, 409), (250, 409), (310, 409), (370, 409), (430, 409), (490, 409), (550, 409), 
        (550, 352), (490, 352), (430, 352), (370, 352), (310, 352), (250, 352), (190, 352), (130, 352), (70, 352), (10, 352), 
        (10, 295), (70, 295), (130, 295), (190, 295), (250, 295), (310, 295), (370, 295), (430, 295), (490, 295), (550, 295), 
        (550, 238), (490, 238), (430, 238), (370, 238), (310, 238), (250, 238), (190, 238), (130, 238), (70, 238), (10, 238), 
        (10, 181), (70, 181), (130, 181), (190, 181), (250, 181), (310, 181), (370, 181), (430, 181), (490, 181), (550, 181), 
        (550, 124), (490, 124), (430, 124), (370, 124), (310, 124), (250, 124), (190, 124), (130, 124), (70, 124), (10, 124), 
        (10, 67), (70, 67), (130, 67), (190, 67), (250, 67), (310, 67), (370, 67), (430, 67), (490, 67), (550, 67), 
        (550, 10), (490, 10), (430, 10), (370, 10), (310, 10), (250, 10), (190, 10), (130, 10), (70, 10), (10, 10)]

player_1_pos = 0
player_2_pos = 0
pygame.init()
BLUE= (26, 167, 236)
GREEN = (27,121,20)
clock = pygame.time.Clock()
image = pygame.image.load("board.png")
dices=[]
for x in range(1, 7):
    img = pygame.image.load(f"dice_{x}.jpeg")
    img = pygame.transform.scale(img, (40, 40))
    dices.append(img)
image = pygame.transform.scale(image, (600,600))
img_surface = pygame.Surface((600, 560))
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake Ladder Ludo")

class circle():
    def __init__(self, x, y, height, line_width, color:tuple):
        self.x = x
        self.y = y
        self.height = height
        self.line_width = line_width
        self.color = color

    def draw(self, window, border=None):
        if border:
            pygame.draw.circle(window, border, (self.x+(self.height//2), self.y+(self.height//2)), self.height//2)
        pygame.draw.circle(window, self.color, (self.x+(self.height//2), self.y+(self.height//2)), (self.height//2)-(self.line_width))


def draw_game():
    img_surface.blit(image, (0, 0))
    window.blit(img_surface,(0, 0))
    pygame.draw.rect(window, (121, 126, 246), (0, 560, 600 , 40))
    if player_1_pos==0 and player_2_pos==0:
        player_1 = circle(70, 560, 40, 5, BLUE)
        player_2 = circle(10, 560, 40, 5, GREEN)
        player_1.draw(window, (30, 47, 121))
        player_2.draw(window, (20,91,15))
    pygame.display.update()

def change_dice(data_sd):
    window.blit(dices[data_sd], (260, 560))
    pygame.display.update()

def show_winner(winner):
    font = pygame.font.Font("./assests/fonts/Game_Of_Squids.ttf ", 32)
    window.fill((0,180,216))
    if winner=="1":
        text = font.render("Blue won", True, (0, 0, 0))
    elif winner=="2":
        text = font.render("Green won", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.topleft = (200, 250)
    window.blit(text, text_rect)
    pygame.display.update()

def check_win():
    if player_1_pos>=100:
        show_winner("1")
    elif player_2_pos>=100:
        show_winner("2")

def go_ladder(pos=0):
    LADDERS={1:38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 72:91, 80:99, 17:7, 54:34, 64:60, 87:36, 93:73, 94:75, 98:79}
    if pos in LADDERS.keys():
        return LADDERS[pos]
    else:
        return pos

def update_pos(play_a_pos, play_b_pos):
    img_surface.blit(image, (0, 0))
    window.blit(img_surface,(0, 0)) 
    if play_a_pos!=0 and play_b_pos!=0:
        player_1 = circle(pos_data[play_a_pos-1][0], pos_data[play_a_pos-1][1], 40, 5, BLUE)
        player_2 = circle(pos_data[play_b_pos-1][0], pos_data[play_b_pos-1][1], 40, 5, GREEN)
        player_1.draw(window, (30, 47, 121))
        player_2.draw(window, (20,91,15))
    elif play_a_pos==play_b_pos and play_a_pos!=0 and play_b_pos!=0:
        player_1 = circle(pos_data[play_a_pos-1][0], pos_data[play_a_pos-1][1]+10, 40, 5, BLUE)
        player_2 = circle(pos_data[play_b_pos-1][0], pos_data[play_b_pos-1][1]-10, 40, 5, GREEN)
        player_1.draw(window, (30, 47, 121))
        player_2.draw(window, (20,91,15))
    pygame.display.update()
   
def main_game():
    loop = True
    global player
    global player_1_pos
    global player_2_pos
    draw_game() 
    update_pos(player_1_pos, player_2_pos)
    player=1
    data_sd = random.randint(0, random.randint(0, 5))
    while loop:
        check_win()
        clock.tick(60)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                loop=False
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    player*=-1
                    data_sd=random.randint(0, random.randint(0, 5))
                    if player==1:
                        if 100-player_1_pos>6:
                            player_1_pos+=(data_sd+1)
                            player_1_pos = go_ladder(player_1_pos)
                            update_pos(player_1_pos, player_2_pos)
                        elif (100-player_1_pos)<=6 and (data_sd+1)<=(100-player_1_pos):
                            player_1_pos+=(data_sd+1)
                            player_1_pos = go_ladder(player_1_pos)
                            update_pos(player_1_pos, player_2_pos)
                    elif player==-1:
                        if 100-player_2_pos>6:
                            player_2_pos+=(data_sd+1)
                            player_2_pos = go_ladder(player_2_pos)
                            update_pos(player_1_pos, player_2_pos)
                        elif (100-player_2_pos)<=6 and (data_sd+1)<=(100-player_2_pos):
                            player_2_pos+=(data_sd+1)
                            player_1_pos = go_ladder(player_1_pos)
                            update_pos(player_1_pos, player_2_pos)
                    update_pos(player_1_pos, player_2_pos)
                if events.key == pygame.K_ESCAPE:
                    loop = False
        change_dice(data_sd)

main_game()