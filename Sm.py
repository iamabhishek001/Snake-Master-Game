import pygame
import sys
import random
import webbrowser as wb

sc_wid = 1200
sc_hei = 600

# initializing pygame
pygame.init()

# rgb values colour

home_col = (255.99609375, 255.99609375, 70.2734375)
white = (255, 255, 255)
green = (157.61328125, 255.99609375, 60.234375)
red = (255.99609375, 43.16796875, 43.16796875)
black = (0, 0, 0)
orange = (255.99609375, 128.5, 64.25)
pink = (255.99609375, 151.58984375, 203.79296875)
purple = (153.59765625, 51.19921875, 255.99609375)
blue = (64.25, 64.25, 255.99609375)
silver = (188.734375, 188.734375, 188.734375)
yellow = (251.98046875, 251.98046875, 0.0)
grey = (160.625, 160.625, 160.625)
snk_eye = black

# creatig Screen
gameWindow = pygame.display.set_mode((sc_wid, sc_hei))
# set game name
pygame.display.set_caption("Snake Master By Abhishek")

# loading Images
apple_pic = pygame.image.load('G_S/Food/apple.png').convert_alpha()
game_icon = pygame.image.load("G_S\\Icons\\snake.png").convert_alpha()
home_snk = pygame.image.load("G_S\\Others\\snk.png").convert_alpha()
let_s = pygame.image.load("G_S\\Letters\\letter-s.png").convert_alpha()
let_n = pygame.image.load("G_S\\Letters\\letter-n.png").convert_alpha()
let_a = pygame.image.load("G_S\\Letters\\letter-a.png").convert_alpha()
let_k = pygame.image.load("G_S\\Letters\\letter-k.png").convert_alpha()
let_e = pygame.image.load("G_S\\Letters\\letter-e.png").convert_alpha()
back_ar = pygame.image.load("G_S\\Others\\backarrow.png").convert_alpha()

pl_black = pygame.image.load("G_S\\Players\\black_snk.png").convert_alpha()
pl_green = pygame.image.load("G_S\\Players\\green_snk.png").convert_alpha()
pl_blue = pygame.image.load("G_S\\Players\\blue_snk.png").convert_alpha()
pl_yellow = pygame.image.load("G_S\\Players\\yellow_snk.png").convert_alpha()
pl_pink = pygame.image.load("G_S\\Players\\pink_snk.png").convert_alpha()
pl_orange = pygame.image.load("G_S\\Players\\orange_snk.png").convert_alpha()
pl_red = pygame.image.load("G_S\\Players\\red_snk.png").convert_alpha()
pl_grey = pygame.image.load("G_S\\Players\\grey_snk.png").convert_alpha()

# sets icon of our game
pygame.display.set_icon(game_icon)

init_velocity = 5
home_run = True
about_run = True
settings_run = True
player_run = True

sp_file = open("G_S\\Player Properties\\Speed\\speed_file.txt", "r")
fill_length = sp_file.read()
sp_file.close()

pc_file = open("G_S\\Player Properties\\Settings\\player_colour.txt", "r")
player_color = pc_file.read()
pc_file.close()

hs_file = open("G_S\\Player Properties\\Settings\\hs.txt", "r")
highscore = hs_file.read()
hs_file.close()

highscore_happen = None

if player_color == "black":
    player_color = black
    snk_eye = white

if player_color == "red":
    player_color = red

if player_color == "green":
    player_color = green

if player_color == "yellow":
    player_color = yellow

if player_color == "blue":
    player_color = blue

if player_color == "pink":
    player_color = pink

if player_color == "grey":
    player_color = grey

if player_color == "orange":
    player_color = orange

if int(fill_length) == 1:
    init_velocity = 1

if int(fill_length) == 2:
    init_velocity = 2

if int(fill_length) == 3:
    init_velocity = 3

if int(fill_length) == 4:
    init_velocity = 4

if int(fill_length) == 5:
    init_velocity = 5

if int(fill_length) == 6:
    init_velocity = 6

if int(fill_length) == 7:
    init_velocity = 7

if int(fill_length) == 8:
    init_velocity = 8

if int(fill_length) == 9:
    init_velocity = 9

def text_screen(text, color, x, y, size=55, given_font="Forte"):
    font = pygame.font.SysFont(given_font, size)
    screen_text = font.render(text, True, color, size)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.circle(gameWindow, player_color, [x, y], snake_size)

fps = 60
clock = pygame.time.Clock()

def play_page():
    global home_run, player_color, init_velocity, fill_length, snk_eye, player_color, highscore, highscore_happen
    colour_snk = False
    time_count = False

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Algerian", 55)

    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, 1000)
    food_y = random.randint(20, 500)
    score = 0
    snake_size = 10
    fps = 60
    num_greater = 50
    sec = 1
    color = green
    snake_dead_text = ["Saap Mar Gaya Re Baba", "Kya Yarr Saap Maar Diya", "Saap Swargiye Ho Gaya", "Saap Ne Khudko Kaat Liya", "Saap Ka Accident Ho gaya"]
    highscore_text = ["Gazab Yarr Score Hai Tumhara", "Kya Khela Hai Yaar Gazab", "Bemisaal Hai Yarr", "Tum Toh Pro Player Ho Yarr"]
    colour_lst = [red, orange, pink, purple, blue, silver, yellow]
    dead_snake = random.choice(snake_dead_text)
    highscore_text_sel = random.choice(highscore_text)
    color_choosen = random.choice(colour_lst)

    while not exit_game:
        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                        pygame.quit()
                        sys.exit()
                        
                    if event.key == pygame.K_RETURN:
                        play_page()

                    if event.key == pygame.K_BACKSPACE:
                        home_run = True
                        home_page()
                        exit_game = True


            gameWindow.fill(white)

            text_screen(dead_snake, pink, 100, 100)
            text_screen("Phir Khelna Hai To Enter Dabao", pink, 100, 200)
            text_screen("Your Score : " + str(score), orange, 250, 300)
            text_screen("Nahi Khelna Hai To Escape Dabao", pink, 100, 400)
            
            if highscore_happen:
                text_screen(highscore_text_sel, color_choosen, 100, 470)
                text_screen(f"Highscore - {score}", red, 800, 480)
            
            pygame.display.update()
            clock.tick(fps)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    
                    if event.key == pygame.K_q:
                        score += 5

                    if event.key == pygame.K_BACKSPACE:
                        home_run = True
                        home_page()
                        exit_game = True


            if snake_x > 1200:
                snake_x = 0
            if snake_x < 0:
                snake_x = 1200
            if snake_y > 600:
                snake_y = 0
            if snake_y < 0:
                snake_y = 600

            snake_x += velocity_x
            snake_y += velocity_y

            check_food_x = food_x - 10
            check_food_y = food_y - 10
            for x1 in range(check_food_x, food_x+33):
                for y1 in range(check_food_y, food_y+30):
                    if (snake_x, snake_y) == (x1, y1):
                        food_x = random.randint(0, 1000)
                        food_y = random.randint(0, 500)
                        score += 5
                        
                        if score > int(highscore):
                            highscore = score

                            hs_file = open("G_S\\Player Properties\\Settings\\hs.txt", "w")
                            hs_file.write(str(highscore))
                            hs_file.close()
                            highscore_happen = True
                            
                        if num_greater < score:
                            num_greater += 50
                            init_velocity += 1
                        snk_length += 3
                    
            gameWindow.fill(white)
            text_screen("Score: " + str(score), red, 5, 5)
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if colour_snk:
                color = random.choice(colour_lst)
                plot_snake(gameWindow, player_color, snk_list, snake_size)
                pygame.display.update()

            plot_snake(gameWindow, player_color, snk_list, snake_size)
            gameWindow.blit(apple_pic, [food_x, food_y])
            pygame.draw.circle(gameWindow, snk_eye, [snake_x+3, snake_y-4], 3)
            pygame.draw.circle(gameWindow, snk_eye, [snake_x+3, snake_y+4], 3)
            pygame.display.update()
            clock.tick(fps)

def about_page():
    global about_run, home_run
    
    while about_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                about_run = False
                if home_run == True:
                    home_run = False
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                mouse_pos = pygame.mouse.get_pos()
                for x in range(470, 724):
                    for y in range(300, 352):
                        if mouse_pos == (x, y):
                            wb.open("https://www.instagram.com/invites/contact/?i=3nqaa8tovdtu&utm_content=axyeg35")

                for x in range(10, 105):
                    for y in range(10, 95):
                        if mouse_pos == (x, y):
                            home_page()
                            home_run = True
                            about_run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    home_page()
                    home_run = True
                    about_run = False

        gameWindow.fill(orange)
        text_screen("ABOUT", black, 290, 20, 160)
        text_screen("ABOUT", green, 300, 20, 150)
        text_screen("This Game Is Made by Abhishek Kumar", black, 50, 200)
        text_screen("This Is A Simple Snake Master Game Coded With Python Programming Language.", black, 10, 260, 34)
        text_screen("Follow Me On", black, 100, 300)
        text_screen("Instagram", blue, 470, 300)
        text_screen("Check My", black, 10, 380, 35)
        text_screen("SnapChat @abhishek_ku9048", blue, 200, 380, 35)

        gameWindow.blit(back_ar, [10, 10])

        mouse_pos = pygame.mouse.get_pos()
        for x in range(470, 724):
            for y in range(300, 352):
                if mouse_pos == (x, y):
                    text_screen("|", blue, 450, 300)
                    text_screen("_________", blue, 470, 300)

        for x in range(490, 657):
            for y in range(450, 496):
                if mouse_pos == (x, y):
                    text_screen("|", blue, 470, 450)
                    text_screen("______", blue, 490, 450)

        pygame.display.update()
        clock.tick(fps)

def home_page():
    global home_run, player_run, about_run, settings_run
    let_vel = 3

    let_s_x = 20
    let_n_x = 220
    let_a_x = 350
    let_k_x = 540
    let_e_x = 750

    let_y = 100

    while home_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home_run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                mouse_pos = pygame.mouse.get_pos()
        
                for x in range(800, 1016):
                    for y in range(100, 198):
                        if mouse_pos == (x, y):
                            home_run = False
                            play_page()
        
                for x in range(780, 1088):
                    for y in range(200, 279):
                        if mouse_pos == (x, y):
                            home_run = False
                            about_page()

                for x in range(790, 1143):
                    for y in range(400, 486):
                        if mouse_pos == (x, y):
                            home_run = False
                            player_run = True
                            player_page()

                for x in range(740, 1193):
                    for y in range(300, 390):
                        if mouse_pos == (x, y):
                            home_run = False
                            settings_run = True
                            settings_page()

        # Fill the screen with colour
        gameWindow.fill(home_col)

        # Home Snk Plot
        gameWindow.blit(home_snk, [20, 100])

        let_s_x += let_vel
        let_n_x += let_vel
        let_a_x += let_vel
        let_k_x += let_vel
        let_e_x += let_vel

        # Letters Plotting
        gameWindow.blit(let_s, [let_s_x, let_y])
        gameWindow.blit(let_n, [let_n_x, let_y])
        gameWindow.blit(let_a, [let_a_x, let_y])
        gameWindow.blit(let_k, [let_k_x, let_y])
        gameWindow.blit(let_e, [let_e_x, let_y])

        if let_s_x > 1200:
            let_s_x  = -1
            let_y = random.randint(100, 400)

        if let_n_x > 1200:
            let_n_x  = -1

        if let_a_x > 1200:
            let_a_x  = -1

        if let_k_x > 1200:
            let_k_x  = -1

        if let_e_x > 1200:
            let_e_x  = -1

        # plotting Buttons

        text_screen("PLAY", black, 798, 100, 102)
        text_screen("ABOUT", black, 778, 200, 102)
        text_screen("SETTINGS", black, 738, 300, 102)
        text_screen("PLAYER", black, 788, 400, 102)

        text_screen("PLAY", grey, 800, 100, 100)
        text_screen("ABOUT", grey, 780, 200, 100)
        text_screen("SETTINGS", grey, 740, 300, 100)
        text_screen("PLAYER", grey, 790, 400, 100)

        mouse_pos = pygame.mouse.get_pos()

        for x in range(800, 1016):
            for y in range(100, 198):
                if mouse_pos == (x, y):
                    text_screen("PLAY", black, 800, 100, 100)
        
        for x in range(780, 1088):
            for y in range(200, 279):
                if mouse_pos == (x, y):
                    text_screen("ABOUT", black, 780, 200, 100)
        
        for x in range(740, 1193):
            for y in range(300, 390):
                if mouse_pos == (x, y):
                    text_screen("SETTINGS", black, 740, 300, 100)
        
        for x in range(790, 1143):
            for y in range(400, 486):
                if mouse_pos == (x, y):
                    text_screen("PLAYER", black, 790, 400, 100)

        pygame.display.update()
        clock.tick(fps)

def settings_page():
    global settings_run, home_run, init_velocity, fill_length

    fill_rect_x = 100
    initial_state = 300
    lst_of_fill = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]

    while settings_run:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                settings_run = False
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if int(fill_length) < 10:
                        fill_length = int(fill_length)
                        fill_length += 1
                        sp_file = open("G_S\\Player Properties\\Speed\\speed_file.txt", "w")
                        sp_file.write(str(fill_length))
                        sp_file.close()

                if event.key == pygame.K_LEFT:   
                    if int(fill_length) > 1:
                        fill_length = int(fill_length)
                        fill_length -= 1
                        sp_file = open("G_S\\Player Properties\\Speed\\speed_file.txt", "w")
                        sp_file.write(str(fill_length))
                        sp_file.close()

                if event.key == pygame.K_BACKSPACE:
                    home_page()
                    home_run = True
                    settings_run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos(), "setting")
                for x in range(10, 105):
                    for y in range(10, 95):
                        if mouse_pos == (x, y):
                            home_run = True
                            settings_run = False
                            home_page()
                
        gameWindow.fill(white)

        text_screen("SETTINGS", grey, 200, 10, 150)

        if fill_rect_x > 1100:
            fill_rect_x = 1100

        if fill_rect_x < 300:
            fill_rect_x = 300

        if int(fill_length) == 1:
            init_velocity = 6

        if int(fill_length) == 2:
            init_velocity = 7

        if int(fill_length) == 3:
            init_velocity = 8

        if int(fill_length) == 4:
            init_velocity = 9

        if int(fill_length) == 5:
            init_velocity = 10

        if int(fill_length) == 6:
            init_velocity = 11

        if int(fill_length) == 7:
            init_velocity = 12

        if int(fill_length) == 8:
            init_velocity = 13

        if int(fill_length) == 9:
            init_velocity = 14

        pygame.draw.rect(gameWindow, black, [300, 200, 60, 110])
        pygame.draw.rect(gameWindow, black, [400, 200, 60, 110])
        pygame.draw.rect(gameWindow, black, [500, 200, 60, 110])
        pygame.draw.rect(gameWindow, black, [600, 200, 60, 110])
        pygame.draw.rect(gameWindow, black, [700, 200, 60, 110])
        pygame.draw.rect(gameWindow, black, [800, 200, 60, 110])
        pygame.draw.rect(gameWindow, black, [900, 200, 60, 110])
        pygame.draw.rect(gameWindow, black, [1000, 200, 60, 110])
        pygame.draw.rect(gameWindow, black, [1100, 200, 60, 110])
        
        pygame.draw.rect(gameWindow, blue, [300, 200, 60, 110])
        for sp in range(int(fill_length)):
            pygame.draw.rect(gameWindow, blue, [lst_of_fill[sp], 200, 60, 110])

        pygame.draw.rect(gameWindow, white, [0, 200, 300, 110])

        text_screen("SPEED", black, 10, 220, 80)
        text_screen("SET SPEED AND PRESS ENTER KEY", black, 200, 420, 50)
        gameWindow.blit(back_ar, [10, 10])

        pygame.display.update()

def player_page():
    global player_run, home_run, player_color, col_choose

    player_col_data = player_color
    player_red_x = 200
    player_black_x = 350
    player_green_x = 450
    player_yellow_x = 550
    player_blue_x = 650
    player_pink_x = 750
    player_grey_x = 850
    player_orange_x = 950
    
    player_vel = 0

    col_choose = None

    while player_run:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                player_run = False
                sys.exit()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse_pos)

                for x in range(10, 101):
                    for y in range(200, 322):
                        if mouse_pos == (x, y):
                            player_vel = 10
                
                for x in range(1100, 1186):
                    for y in range(200, 322):
                        if mouse_pos == (x, y):
                            player_vel = -10

                for x in range(10, 105):
                    for y in range(10, 95):
                        if mouse_pos == (x, y):
                            home_page()
                            home_run = True
                            player_run = False

                for x in range(450, 754):
                    for y in range(507, 542):
                        if mouse_pos == (x, y):
                            player_color = col_choose
                            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    player_vel = 10
                
                if event.key == pygame.K_LEFT:
                    player_vel = -10

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT:
                    player_vel = 0
                
                if event.key == pygame.K_LEFT:
                    player_vel = 0

                if event.key == pygame.K_RETURN:
                    player_color = col_choose

                if event.key == pygame.K_BACKSPACE:
                    home_run = True
                    home_page()
                    player_run = False

            if event.type == pygame.MOUSEBUTTONUP:

                for x in range(10, 101):
                    for y in range(200, 322):
                        if mouse_pos == (x, y):
                            player_vel = 0
            
                for x in range(1100, 1186):
                    for y in range(200, 322):
                        if mouse_pos == (x, y):
                            player_vel = 0

        gameWindow.fill(white)

        text_screen("PLAYER", grey, 200, 10, 150)
        
        if player_red_x > 1180:
            player_red_x = 120
        
        if player_black_x > 1180:
            player_black_x = 120
        
        if player_green_x > 1180:
            player_green_x = 120
        
        if player_yellow_x > 1180:
            player_yellow_x = 120
        
        if player_blue_x > 1180:
            player_blue_x = 120
        
        if player_pink_x > 1180:
            player_pink_x = 120
        
        if player_grey_x > 1180:
            player_grey_x = 120
        
        if player_orange_x > 1180:
            player_orange_x = 120

        if player_red_x < 120:
            player_red_x = 1180
        
        if player_black_x < 120:
            player_black_x = 1180
        
        if player_green_x < 120:
            player_green_x = 1180
        
        if player_yellow_x < 120:
            player_yellow_x = 1180
        
        if player_blue_x < 120:
            player_blue_x = 1180
        
        if player_pink_x < 120:
            player_pink_x = 1180
        
        if player_grey_x < 120:
            player_grey_x = 1180
        
        if player_orange_x < 120:
            player_orange_x = 1180
        
        player_red_x += player_vel
        player_black_x += player_vel
        player_green_x += player_vel
        player_yellow_x += player_vel
        player_blue_x += player_vel
        player_pink_x += player_vel
        player_grey_x += player_vel
        player_orange_x += player_vel

        gameWindow.blit(pl_red, [player_red_x, 200])
        gameWindow.blit(pl_black, [player_black_x, 200])
        gameWindow.blit(pl_green, [player_green_x, 200])
        gameWindow.blit(pl_yellow, [player_yellow_x, 200])
        gameWindow.blit(pl_blue, [player_blue_x, 200])
        gameWindow.blit(pl_pink, [player_pink_x, 200])
        gameWindow.blit(pl_grey, [player_grey_x, 200])
        gameWindow.blit(pl_orange, [player_orange_x, 200])

        pygame.draw.rect(gameWindow, white, [0, 200, 100, 310])
        pygame.draw.rect(gameWindow, white, [1100, 200, 100, 310])

        text_screen("<", purple, 10, 200, 150)
        text_screen(">", purple, 1100, 200, 150)
        
        text_screen("Choose Player", black, 450, 500, 50)
        
        for x in range(576, 635):
            if str(player_red_x) in str(x):
                text_screen("RED", red, 550, 550, 50)
                col_choose = red
        
        for x in range(576, 635):
            if str(player_black_x) in str(x):
                text_screen("BLACK", black, 550, 550, 50)
                col_choose = black
        
        for x in range(576, 635):
            if str(player_green_x) in str(x):
                text_screen("GREEN", green, 550, 550, 50)
                col_choose = green
        
        for x in range(576, 635):
            if str(player_yellow_x) in str(x):
                text_screen("YELLOW", yellow, 550, 550, 50)
                col_choose = yellow
        
        for x in range(576, 635):
            if str(player_blue_x) in str(x):
                text_screen("BLUE", blue, 550, 550, 50)
                col_choose = blue
        
        for x in range(576, 635):
            if str(player_pink_x) in str(x):
                text_screen("PINK", pink, 550, 550, 50)
                col_choose = pink
        
        for x in range(576, 635):
            if str(player_grey_x) in str(x):
                text_screen("GREY", grey, 550, 550, 50)
                col_choose = grey
        
        for x in range(576, 635):
            if str(player_orange_x) in str(x):
                text_screen("ORANGE", orange, 550, 550, 50)
                col_choose = orange

        for x in range(450, 754):
            for y in range(507, 542):
                if mouse_pos == (x, y):
                    text_screen("Choose Player", purple, 450, 500, 50)

        if col_choose == red:
            player_col_data = "red"

        if col_choose == black:
            player_col_data = "black"

        if col_choose == green:
            player_col_data = "green"

        if col_choose == yellow:
            player_col_data = "yellow"

        if col_choose == blue:
            player_col_data = "blue"

        if col_choose == pink:
            player_col_data = "pink"

        if col_choose == grey:
            player_col_data = "grey"

        if col_choose == orange:
            player_col_data = "orange"

        pc_file = open("G_S\\Player Properties\\Settings\\player_colour.txt", "w")
        pc_file.write(str(player_col_data))
        pc_file.close()

        gameWindow.blit(back_ar, [10, 10])
        pygame.display.update()

home_page()