#Done slight changes to code and works for me:

import pygame
import asyncio
import math 

# Start the game
pygame.init()
game_width = 960
game_height = 540
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True
color = (255,255,255)
  
# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)
  
width = screen.get_width()
  
# stores the height of the
# screen into a variable
height = screen.get_height()
  
# defining a font
smallfont = pygame.font.Font('aachen.ttf',35)
  
# rendering a text written in
# this font
text = smallfont.render('PLAY' , True , color)
#motion1 = False

# Load the basketball image


# Set the starting position of the basketball


# Set the initial velocity of the basketball
basketball_velocity_x = 0
basketball_velocity_y = 0
score =0
# Set the gravity constant
GRAVITY = 0.5
shooted=False
hello = False
score = 0
score_add=  0
#rect = pygame.Rect(760, 285, 40, 50)
#pygame.draw.rect(screen, (255, 255, 255), rect)
class Basketball:
    def __init__(self, screen, running, basketball, player_x, player_y, player_facing_left, background, Y_VELOCITY, Y_GRAVITY, JUMP_HEIGHT, basketball_x, basketball_y, shooted):
        self.screen = screen
        self.running = running
        self.basketball = basketball
        self.player_x = player_x
        self.player_y = player_y
        self.player_facing_left = player_facing_left
        self.background = background
        self.Y_VELOCITY = Y_VELOCITY
        self.Y_GRAVITY = Y_GRAVITY
        self.JUMP_HEIGHT = JUMP_HEIGHT
        self.basketball_x = basketball_x
        self.basketball_y = basketball_y


        self.shooted = shooted
    def main(self):
        #print(type(self.basketball))
        if not shooted:
            if self.player_facing_left:

                self.basketball_x = self.player_x+26
                self.basketball_y = self.player_y+70
                #rect2 = pygame.Rect(self.basketball_x+26, self.basketball_y+70, 40, 47)

                #self.screen.blit(self.basketball, (self.basketball_x, self.basketball_y))


            else:

                self.basketball_x = self.player_x+115
                self.basketball_y = self.player_y+70
                #rect2 = pygame.Rect(self.basketball_x, self.basketball_y, 40, 47)
                global circle2_pos
                circle2_pos = (self.basketball_x+20, self.basketball_y+21)
                global circle2_rad
                circle2_rad= 19
                pygame.draw.circle(self.screen, (255, 255, 255), (circle2_pos), 19, width=0)

            self.screen.blit(self.basketball, (self.basketball_x, self.basketball_y))

            #pygame.draw.rect(self.screen, (255, 255, 255), rect2)

        else:
            global basketball_x2, basketball_y2
            global basketball_velocity_x, basketball_velocity_y

            if basketball_x2 > 5 and basketball_x2 < 915:
                if basketball_y2 > 0 and basketball_y2 < 500:
                    basketball_x2 += basketball_velocity_x
                    basketball_y2 += basketball_velocity_y
                    # Apply gravity to the basketball
                    #basketball_velocity_y += GRAVITY
            basketball_velocity_y += GRAVITY
            #rect2 = pygame.Rect(basketball_x2, basketball_y2, 40, 47)
            #pygame.draw.rect(self.screen, (255, 255, 255), rect2)
            circle2_pos = (basketball_x2+20, basketball_y2+21)
            pygame.draw.circle(self.screen, (255, 255, 255), (circle2_pos), circle2_rad, width=0)
            #screen.blit(b)

            # Draw the screen
            screen.blit(self.basketball, (basketball_x2, basketball_y2))  # Draw the basketball

            global hello
            global score, score_add
            if self.check_collision():
                score_add = 1



            





    def set_baspos(self):
        global basketball_x2, basketball_y2
        global basketball_velocity_x, basketball_velocity_y
        basketball_velocity_x = 10
        basketball_velocity_y = -10


        basketball_x2 = self.player_x+115
        basketball_y2 = self.player_y+70
    def check_collision(self):
        dx = circle2_pos[0] - circle1_pos[0]
        dy = circle2_pos[1] - circle1_pos[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Check for collision between the circles
        if distance <= circle1_rad + circle2_rad:
            return True





class Player:
    def __init__(self, screen, running, background, player, player_x, player_y, player_speed, player_size, player_facing_left, player_hitbox, player_alive, isjump, jumping,  Y_GRAVITY, JUMP_HEIGHT, Y_VELOCITY):
        self.screen = screen
        self.running = running
        self.background = background
        self.player = player
        self.player_x = player_x
        self.player_y = player_y
        self.player_speed = player_speed
        self.player_size = player_size
        self.player_facing_left = player_facing_left
        self.player_hitbox = player_hitbox
        self.player_alive = player_alive
        self.isjump = isjump
        self.jumping = jumping
        self.Y_GRAVITY = Y_GRAVITY
        self.JUMP_HEIGHT = JUMP_HEIGHT
        self.Y_VELOCITY = Y_VELOCITY

    async def main(self):
        # Everything under 'while running' will be repeated over and over again
        self.running = True
        pygame.event.set_allowed(None) # makes no events allowed
        pygame.event.set_allowed(pygame.QUIT) # Start setting what events we care about
        pygame.event.set_allowed(pygame.KEYDOWN)
        #pygame.event.set_allowed(pygame.KEYDOWN)

        while self.running:

            #basketball = Basketball(self.screen, self.running, pygame.image.load('basketball.png').convert_alpha(), self.player_x, self.player_y, self.player_facing_left,
                                    #motion1, pygame.image.load('background.png').convert_alpha(),1, 16, 16, self.player_x+80, self.player_y+75)
            global circle1_pos
            circle1_pos = (780, 305)
            global circle1_rad
            circle1_rad = 23
            pygame.draw.circle(screen, (255, 255, 255), (circle1_pos), 23, width=0)

            self.screen.blit(self.background, (0, 0))

            keys = pygame.key.get_pressed()

            # Makes the game stop if the player clicks the X or presses esc
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        self.jumping = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    global shooted
                    shooted = True
                    basketball.set_baspos()
            basketball = Basketball(self.screen, self.running, pygame.image.load('basketball.png').convert_alpha(), self.player_x, self.player_y, self.player_facing_left,
                                     pygame.image.load('background.png').convert_alpha(), 5, 3, 2,  self.player_x+80, self.player_y+75,  shooted)


            basketball.main()
            global score_add
            if score_add == 1:
                global score
                score += 1
                score_add = 0
            print(score)

            if keys[pygame.K_a]:
                #print(self.player_x, self.player_y)
                if self.player_x > 0:
                    self.player_x -= self.player_speed
                    self.player_facing_left = True

                #player_y += player_speed
            if keys[pygame.K_LSHIFT]:
                #print(self.player_x, self.player_y)

                    if keys[pygame.K_d]:
                        if self.player_x < 850:
                            self.player_x += 3.5
                        #player_facing_left = False
                    if keys[pygame.K_a]:
                        if self.player_x > 0:

                            self.player_x -= 3.5
                        #player_facing_left = True
            if keys[pygame.K_d]:
                #print(self.player_x, self.player_y)
                if self.player_x < 850:
                    self.player_x += self.player_speed
                    self.player_facing_left = False


            if self.jumping:
                self.player_y -= self.Y_VELOCITY
                self.Y_VELOCITY -= self.Y_GRAVITY
                if self.Y_VELOCITY < -self.JUMP_HEIGHT:
                    self.jumping = False
                    self.Y_VELOCITY = self.JUMP_HEIGHT

                
            # Spawn a new Enemy whenever enemy_timer hits 0


            # Draw Player
            global player_small
            player_small = pygame.transform.scale(self.player, (int(self.player_size*.7), int(self.player_size*.7)))

            screen.blit(player_small, (self.player_x, self.player_y))
            #rect.colliderect(player_small.rect)
            #print(type(player_small))


            #merged = self.player.copy()

            #screen.blit(score_text, (1600, 30))
            #print(score)
            # Update Screen
            pygame.display.update()
            clock.tick(50)
            await asyncio.sleep(0)
            pygame.display.set_caption("FPS: " + str(clock.get_fps()))


jordan = Player(pygame.display.set_mode((game_width, game_height)), True, pygame.image.load('background.png').convert(), pygame.image.load('curry3.png').convert_alpha(), 200, 300, 3, 260, False, pygame.Rect(0, 0, int(160*1.25), 160), True, False, False, 1, 16, 16)                
async def main_menu():
    running = True
    while running:
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                running = False
                
            #checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #if the mouse is clicked on the
                # button the game is terminated
                if width/2.5 <= mouse[0] <= width/2+45 and height/2.3 <= mouse[1] <= height/2+10:
                    await jordan.main()

        # fills the screen with a color
        screen.fill((190,0,50))
        
        # stores the (x,y) coordinates into
        # the variable as a tuple
        
        # if mouse is hovered on a button it
        # changes to lighter shade 
        if width/2.5 <= mouse[0] <= width/2+45 and height/2.3 <= mouse[1] <= height/2+10:
            pygame.draw.rect(screen,color_light,[width/2.5,height/2.3,140,40])
            
        else:
            pygame.draw.rect(screen,color_dark,[width/2.5,height/2.3,140,40])
        
        # superimposing the text onto our button
        screen.blit(text, (width/2.325,height/2.27))

        # updates the frames of the game
        pygame.display.update()
        await asyncio.sleep(0)  # Very important, and keep it 0
    #pygame.quit()
'''
def main():
    run = True
    while run:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                running = False
        main_menu()
'''
asyncio.run(main_menu())

#[Diff](https://diffy.org/diff/3626b7ae7b5fc)

#What did I change?
#Game loop also needs to be asynchronous, otherwise the window wouldn't be refreshed.