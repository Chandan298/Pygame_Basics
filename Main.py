# GUI : Graphical User Interface
from pdb import Restart
import pygame,sys
import random,time
playing = True
#Initialization...
pygame.init()

width = 500
height = 500

window = pygame.display.set_mode(size = (width,height))

fps = 10
game_clock = pygame.time.Clock()
background = pygame.image.load('snakeground.jpg')
background = pygame.transform.scale(background,(width,height))
red = pygame.Color(255,0,0)
black = pygame.Color(0,0,0)
food_position = [random.randrange(0,width, 10),random.randrange(0,height, 10)]
snake_fullBody = [[100,50],[90,50],[80,50]]
snake_head = [100,50]

current_direction = 'RIGHT'
change_direction = current_direction
score = 0
def gameEnd():
    # Photo Frame :-> Photo + Frame
    font = pygame.font.SysFont('minecraft-evenings-font',90)
    scorefont = pygame.font.SysFont('minecraft-evenings-font', 50)
    text = font.render("YOU DIED", True, red)
    scoretext = scorefont.render(f"Final Score : {score}", True,pygame.Color(0, 0, 100))
    scoreframe = scoretext.get_rect()
    scoreframe.midtop = (width/2, height/2.5)
    
    Restartbutton = pygame.image.load('restartbutton.png')
    Restartbutton = pygame.transform.scale(Restartbutton,(225,100))
    
    frame = text.get_rect()
    frame.midtop = (width/2,height/4)
    window.fill(black)
    window.blit(text,frame)
    window.blit(scoretext, scoreframe)
    window.blit(Restartbutton,(width/3.5, height/2))
    
        
            
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def showScore():
    font = pygame.font.SysFont('minecraft-font',20)
    text = font.render(f"Score : {score}", True, pygame.Color(0, 0, 200))
    frame = text.get_rect()
    frame.midtop = (50,10)
    # window.fill(black)
    window.blit(text,frame)
    pygame.display.update()
  



while playing:
    window.blit(background,(0,0))

    # Food
    pygame.draw.rect(window, red, [food_position[0], food_position[1], 10, 10])
    
    for block in snake_fullBody:
        pygame.draw.rect(window, red, [block[0], block[1],10,10])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                
                change_direction = 'UP'
            elif event.key == ord('a'):
                change_direction = 'LEFT'
            elif event.key == ord('s'):
                change_direction = 'DOWN'
            elif event.key == ord('d'):
                change_direction = 'RIGHT'

    if change_direction == "UP" and current_direction != 'DOWN':
        current_direction = 'UP'
    elif change_direction == 'LEFT' and current_direction != 'RIGHT':
        current_direction = 'LEFT'

    elif change_direction == 'DOWN' and current_direction != 'UP':
        current_direction = 'DOWN'

    elif change_direction == 'RIGHT' and current_direction != 'LEFT':
        current_direction = 'RIGHT'
    
    if change_direction == "UP" and current_direction == 'DOWN':
        gameEnd()
    elif change_direction == 'LEFT' and current_direction == 'RIGHT':
        gameEnd()
    elif change_direction == 'DOWN' and current_direction == 'UP':
        gameEnd()
    elif change_direction == 'RIGHT' and current_direction == 'LEFT':
        gameEnd()
   
    if current_direction == 'UP':
        snake_head[1] -= 10
    if current_direction == 'DOWN':
        snake_head[1] += 10
    if current_direction == 'LEFT':
        snake_head[0] -= 10
    if current_direction == 'RIGHT':
        snake_head[0] += 10
  

    # .append(), .insert()
    snake_fullBody.insert(0, list(snake_head))

    if snake_head[0] == food_position[0] and snake_head[1] == food_position[1]:
        food_position = [random.randrange(0,width, 10),random.randrange(0,height, 10)]
        score += 1
    else:
       snake_fullBody.pop()

    if snake_head[0] < 0 or snake_head[0] > width:
        gameEnd()
        
    if snake_head[1] < 0 or snake_head[1] > height:
        gameEnd()

    for block in snake_fullBody[1:]:
        if snake_head[0] == block[0] and snake_head[1] == block[1]:
            gameEnd()
    game_clock.tick(fps)
    pygame.display.update()
    showScore()


# Snake Collision with the walls and no reverse motion.
# On a collision, "YOU DIED" text should be displayed.
# Score.