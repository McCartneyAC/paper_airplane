
 
import pygame
import random
 
# --- Global constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,154,23)
RED = (255, 0, 0)
SAGE = (156,175,136)
GRAPE = (128,49,167)
BABY = (155,211,221)
YELLOW = (255,239,0)
BROWN = (101,56,24)
MILLENNIAL = (165,169,160)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
 
# --- Classes ---
 
 
class Cloud(pygame.sprite.Sprite):
 
    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        width = random.randint(140, 300)  # Random width between 30 and 100
        height = random.randint(40, 150)  # Random height between 15 and 60
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.fill((0,0,0,0))
        pygame.draw.ellipse(self.image, WHITE, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.reset_pos()

    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-10, SCREEN_HEIGHT) 
        self.rect.x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH + 20) 
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.x += -1
 
        if self.rect.x + self.rect.width < 0:
            self.reset_pos()
 
class Player(pygame.sprite.Sprite):
    """ This class represents the player. """
    def __init__(self):
        super().__init__()
        #self.image = pygame.Surface([20, 20])
        self.image = pygame.Surface([95,80],pygame.SRCALPHA)
        self.image.fill(BLACK)
        self.image.fill((0,0,0,0))
        tipx = 95
        tipy = 0
        pygame.draw.polygon(self.image, WHITE, 
                        [[tipx,tipy], #1
                        [tipx-50, tipy+80], #2
                        [tipx-66, tipy+50], #3
                        [tipx-75, tipy+66], #4
                        [tipx-63, tipy+63], #5 
                        [tipx-66, tipy+50],   #6  
                        [tipx, tipy], #1
                        [tipx-95, tipy+30],#8
                        [tipx-78, tipy+40],#9
                        [tipx-75, tipy+66], #4 
                        [tipx-66, tipy+50],   #6 
                        [tipx, tipy],#1
                        [tipx-78, tipy+40]#9
                        ]
                       ) 
        pygame.draw.polygon(self.image, BLACK, 
                        [[tipx,tipy], #1
                        [tipx-50, tipy+80], #2
                        [tipx-66, tipy+50], #3
                        [tipx-75, tipy+66], #4
                        [tipx-63, tipy+63], #5 
                        [tipx-66, tipy+50],   #6  
                        [tipx, tipy], #1
                        [tipx-95, tipy+30],#8
                        [tipx-78, tipy+40],#9
                        [tipx-75, tipy+66], #4 
                        [tipx-66, tipy+50],   #6 
                        [tipx, tipy],#1
                        [tipx-78, tipy+40]#9
                         
                        ], 
                        width = 3
                       ) 
        self.rect = self.image.get_rect()

 
    def update(self):
        """ Update the player location. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Cash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        rangex = random.randint(-10, SCREEN_HEIGHT)
        rangey = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 20)
        self.image = pygame.Surface([10,15])
        self.image.fill(GREEN)
        pygame.draw.rect(self.image,GREEN,[rangex, rangey,10,15])
        # money blit goes here. 
        self.rect = self.image.get_rect()
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-10, SCREEN_HEIGHT) 
        self.rect.x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH + 20) 
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.x += -1
        if self.rect.x + self.rect.width < 0:
            self.reset_pos()

            
class RedX(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        rangex = random.randint(-10, SCREEN_HEIGHT)
        rangey = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 20)
        self.image = pygame.Surface([10,15])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-10, SCREEN_HEIGHT) 
        self.rect.x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH + 20) 
        
    def update(self):
        self.rect.x += -1
        if self.rect.x + self.rect.width < 0:
            self.reset_pos()
 
class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """
 
    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """
 
        self.score = 0
        self.game_over = False
 
        # Create sprite lists
        self.cloud_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.cash_list = pygame.sprite.Group()
        self.redx_list = pygame.sprite.Group() 

 
        # Create the block sprites
        for i in range(50):
            cloud = Cloud()
 
            cloud.rect.x = random.randrange(-10, SCREEN_HEIGHT) 
            cloud.rect.y = random.randrange(-300, SCREEN_HEIGHT)
 
            self.cloud_list.add(cloud)
            self.all_sprites_list.add(cloud)

        for i in range(15):
            cash = Cash()

            cash.rect.x = random.randrange(SCREEN_WIDTH)
            cash.rect.y = random.randrange(-300, SCREEN_HEIGHT)
            self.cash_list.add(cash)
            self.all_sprites_list.add(cash)
        for i in range(15):
            redx = RedX()

            redx.rect.x = random.randrange(SCREEN_WIDTH +100)
            redx.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            self.redx_list.add(redx)
            self.all_sprites_list.add(redx)


        # Create the player
        self.player = Player()
        self.all_sprites_list.add(self.player)
 
    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
 
        return False
 
    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()
 
            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.cash_list, True)
            exes_hit_list = pygame.sprite.spritecollide(self.player, self.redx_list, True)
 
            # Check the list of collisions.
            for block in blocks_hit_list:
                self.score += 1
                print(self.score)
                # You can do something with "block" here.
            
            for ex in exes_hit_list: 
                self.score += -5
                print(self.score)

            if len(self.cash_list) == 0:
                self.game_over = True
 
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(BABY)
 
        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            score = self.score
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over! Your Score was: " + str(score) + ". Click to Restart",True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
 
        if not self.game_over:
            self.all_sprites_list.draw(screen)
 
        pygame.display.flip()
 
 
def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)
 
    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = Game()
 
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Update object positions, check for collisions
        game.run_logic()
 
        # Draw the current frame
        game.display_frame(screen)
 
        # Pause for the next frame
        clock.tick(60)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()