import pygame
import math

# the two imports above will help with the set up. The green lines underneath are ok, they are there to show that they are new modules that may or may not have used yet. After that we are going to initialise the game. init()
pygame.init()
# Then we are going to define the size of the game. make it varioable though.
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))

# The Width and height is capitised to show a constant value and do not change. Its good practice to keep constants in capitals.
pygame.display.set_caption("Hangman Game!")
# load images early, prefably after the title.
# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 12 - 2 * RADIUS) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + RADIUS + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('Helvetica', 20)
WORD_FONT = pygame.font.SysFont('Helvetica', 30)

images = []
for i in range(7):
    image = pygame.image.load("./images/hangman" + str(i) + ".png")
    images.append(image)
print(images)
# this uploads our pictures converting them to pixels know as surface. We will then display through variables. Hangman status goes through the roladex of hangman images.
hangman_status = 0
word = "LEWISHAM"
guessed = []

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# next we create a Loop checking for any errors and running the game loop
FPS = 60
# this frames per second to help stabalise the game. then make a Time. He said to put FPS in the clock but it crashes.Don't do it.
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += " _ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))
    for letter in letters:
        x, y, ltr, visable = letter
        if visable:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)
    # this helps the loop run at FPS. Then we check for events with a for loop. this looks for the mouse clicks etc
    # use the RBG system to make the screen white using the in variable uptop and will do this for every frame. Then we tell it to update the screen.
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visable = letter
                if visable:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("You Won!")
        break

    if hangman_status == 6:
        display_message("You Lost :(")
        break

        # This helps us to make sure that when we use the mouse click, something will happen, prefrably over the images(letters)that we have on the screen. once you have created your buttons, we have to manually check the accurancy of the mouse click.
pygame.quit