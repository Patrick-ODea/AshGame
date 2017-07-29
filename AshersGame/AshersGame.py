import pygame
import random
import time

# Initialize the game engine
pygame.init()
# -----------Color variables
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BLUE = [0, 50, 255]
YELLOW = [255, 255, 128]
RED = [255, 0, 0]
# --------------------DISPLAY SIZE
SIZE = [600, 600]
# creates a display called screen and sets to the size varible
screen = pygame.display.set_mode(SIZE)
# ----SETS TITLE
pygame.display.set_caption("Asher's Game")
# -----Set ICON
ICON = pygame.image.load("triangleFaceMan.PNG")
pygame.display.set_icon(ICON)
# -----MR. FRIENDLY CLOCK
clock = pygame.time.Clock()


# -------PRINTS A MESSAGE "TEXT" WITH "COLOR" to SOME SHITTY HARD CODED PART OF SCREEN
def Message(text, color):
    font = pygame.font.SysFont(None, 50)
    textMessage = font.render(text, True, color)
    screen.blit(textMessage, [(SIZE[0] * .28), (SIZE[1] / 2), 100, 50])


# --------DRAWS MR HAT TRIANGLE FACE
def draw_face(screen, x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), 50, )
    pygame.draw.circle(screen, BLACK, (x - 25, y - 25), 5)
    pygame.draw.circle(screen, BLACK, (x + 25, y - 25), 5)
    pygame.draw.polygon(screen, BLACK, ((x - 25, y + 5), (x, y + 30), (x + 25, y + 5)))
    pygame.draw.rect(screen, BLACK, [x - 50, y - 60, 104, 20], )
    pygame.draw.rect(screen, RED, [x - 50, y - 60, 100, 20], 2)
    pygame.draw.rect(screen, BLACK, [x - 25, y - 137, 52, 77], )
    pygame.draw.rect(screen, RED, [x - 25, y - 135, 52, 75], 2)


# -------MAKES IT RAIN WHEN YOU IMPORT A LIST/ARRAY
def rainDrops(raining):
    # Process each rain drop in the list
    for i in range(len(raining)):
        # Draw the drop
        pygame.draw.circle(screen, BLUE, raining[i], 2)
        # Move the drop down one pixel
        raining[i][1] += 1
        # If the drop has moved off the bottom of the screen
        if raining[i][1] > (SIZE[1]):
            # Reset it just above the top
            y = random.randrange(-50, -10)
            raining[i][1] = y
            # Give it a new x position
            x = random.randrange(0, (SIZE[0]))
            raining[i][0] = x


# --------------DISPLAYS THE RED BUTTON ON INTRO-----------
def startButton():
    pygame.draw.rect(screen, RED, [SIZE[0] * .33, SIZE[1] * .66, 200, 50])
    font = pygame.font.SysFont(None, 24)
    message = font.render("CLICK TO START", True, BLACK)
    screen.blit(message, (((SIZE[0] * .33 + 30), (SIZE[1] * .66 + 15))))
    pygame.display.update()


# -------Displays Peek on screen when middle of face goes off screen till it comes back
# -----USES THE MESSAGE FUNCTION TO PRINT ON TO THE SCREEN.
def peek():
    screen.fill(BLACK)
    Message("PEEK!", RED)
    pygame.display.update()
    time.sleep(.1)

# -------the click action for the start button.
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

        else:
            pygame.draw.rect(screen, ic, (x, y, w, h))
            font = pygame.font.SysFont(None, 24)
            message = font.render("CLICK TO START", True, BLACK)
            screen.blit(message, (((SIZE[0] * .33 + 30), (SIZE[1] * .66 + 15))))
            pygame.display.update()

# -------Draws and pauses game when user presses ''d''
def funStuff():
    while True:
        mouse = pygame.mouse.get_pos()
        mousex = mouse[0]
        mousey = mouse[1]
        for event in pygame.event.get():
            pygame.draw.rect(screen, YELLOW, [mousex, mousey, 20, 20])
            pygame.draw.circle(screen, WHITE, ((mousex + 50), (mousey + 50)),10)
            pygame.draw.circle(screen, BLUE, ((mousex + 50), (mousey)), 10)
            pygame.draw.circle(screen, RED, ((mousex + 50), (mousey-50)), 10)
            pygame.draw.circle(screen, RED, ((mousex -50), (mousey + 50)), 10)
            pygame.draw.circle(screen, WHITE, ((mousex - 50), (mousey)), 10)
            pygame.draw.circle(screen, BLUE, ((mousex - 50), (mousey - 50)), 10)
            pygame.draw.rect(screen, YELLOW, [mousex, mousey +50, 20, 20])
            pygame.draw.rect(screen, YELLOW, [mousex, mousey - 50, 20, 20])
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    Message("AMERICA!!!!!!!!!!",BLUE)
                    pygame.display.update()
                    time.sleep(.5)
                    return False




# ----------Intro screen----- Start game when screen is clicked
def intro():

    while intro:
        screen.fill(BLACK)
        Message("ASHER'S GAME", RED)
        startButton()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            button("Start Game!!!", (SIZE[0] * .33), (SIZE[1] * .66), 200, 50, RED, RED , gameloop)



# ----------------------MAIN FUCNTION FOR GAMEPLAY___MAIN LOOP--------
def gameloop():
    # ------SETTING START VALUES FOR USER AND DISPLAY
    x_coord = 300
    y_coord = 500
    face_changeX = 0
    face_changeY = 0
    raining = []
    for i in range(50):
        x = random.randrange(0, (SIZE[0]))
        y = random.randrange(0, (SIZE[1]))
        raining.append([x, y])

    # ---------------MAIN LOOP-------------
    done = False
    while not done:

        # --------EVENT LOGIC----------
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True # Flag that we are done so we exit this loop
            # This is the code for controlling the users char.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    face_changeX = -5
                if event.key == pygame.K_RIGHT:
                    face_changeX = 5
                if event.key == pygame.K_UP:
                    face_changeY = -5
                if event.key == pygame.K_DOWN:
                    face_changeY = 5
                if event.key == pygame.K_d:
                    funStuff()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    face_changeX = 0
                if event.key == pygame.K_RIGHT:
                    face_changeX = 0
                if event.key == pygame.K_UP:
                    face_changeY = 0
                if event.key == pygame.K_DOWN:
                    face_changeY = 0


        # --------Logic to display the peek function
        if x_coord-25 > SIZE[0] or x_coord+25 < 0:
            peek()
        if y_coord -25> SIZE[1] or y_coord+25 < 0:
            peek()

        # -------GAME LOGIC / Drawing Logic-----------
        x_coord += face_changeX
        y_coord += face_changeY
        # ----------Drawing---------
        screen.fill(BLACK)
        rainDrops(raining)
        draw_face(screen, x_coord, y_coord)
        # update----------
        pygame.display.update()
        clock.tick(60)


    # ------END OF MAIN LOOP

    # -----Quits on the exit of main gameloop
    pygame.quit()
    quit()


# ---------THE START OF THE GAME!!!!!!!!!!!!!!!!!!!!!!!

intro()


# ---------------NEED OF THE GAME Thanks for viewing ..by Odie......A.O.
