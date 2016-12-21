'''
Author: Brian Lam

Version: v1.10

Game Name: pyMaple

Python File: myMapleSprites

Description: Handles the sprite information (Player, Mob, Bullet), such as 
positioning and reading each image from the Sprites folder.

Project description: A game where the player plays to the end. In other words, 
they'll play for as long as they survive. The objective of the game is simply to
survive from the monsters attacking you. An attack is considered a collision 
between you and the monster.'''

import pygame, random
  
class Player(pygame.sprite.Sprite):
    def __init__(self,screen):
        ''' Initializer method for the player '''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self) 
        self.__width = screen.get_width()
        self.__height = screen.get_height()
        self.xcenter = 200
        self.ycenter = 367
        self.__dx = 0
        self.__dy  = 0
        self.__set_direction = 1
        self.__screen = screen
        self.__direction2 = 2
       
        # Set the image and rect attributes for the bricks
        self.image = pygame.image.load("stand_right0.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.xcenter, self.ycenter)
     
        # Right Sprites list, loading sprites, keeping count of frames, and count of right
        self.__goRightSprites = []
        for image_number in range (0,4):
            self.__right_image_pack  = pygame.image.load ("./Sprites/walk_right" + str(image_number)+ ".png")
            self.__goRightSprites.append(self.__right_image_pack)
        self.__rightCount = 0  
        
        # Left Sprites list, loading sprites, keeping count of frames, and count of left
        self.__goLeftSprites = []
        for image_number in range (0,4):
            self.__left_image_pack = pygame.image.load ("./Sprites/walk_left" + str(image_number)+ ".png")
            self.__goLeftSprites.append( self.__left_image_pack)
        self.__leftCount = 0
        
        #Shooting Images
        self.__shoot_left = pygame.image.load('./Sprites/shoot_left0.png')        
         
        self.__shoot_right = pygame.image.load('./Sprites/shoot_right0.png')
        
        # Sets isShooting to False
        self.__isShooting = False
        
        # Set Frame Count to 0 and Moving to False
        self.__frameCount = 0   
        self.__moving = False
        
        #Sets isShooting to false (not shooting)
        self.__isShooting = False 
        
        #Makes the player go into shooting position (left)    
        if (self.__isShooting== True) and (self.__direction2 == 1) :
            self.image = self.__leftShootImages 
            
        #Makes the player go into shooting position (right)       
        if (self.__isShooting== True) and (self.__direction2 == 2) : 
            self.image = self.__rightShootImages     
    
    def direction2 (self,direction):
        self.__direction2 = direction
        
    def dir_ret(self):
        return self.__direction2
    
    def change_direction(self,xy_change):
        ''' Changes the direction '''
        self.__dx = xy_change[0]*1.1
        
    def go_left(self,xy_change,direction):
        ''' Moves the left '''
        self.__moving = True
        self.__dx = xy_change[0]*1.1
        self.__direction = direction
    
    def go_right(self,xy_change,direction):
        ''' Moves the player right '''
        self.__moving = True 
        self.__dx = xy_change[0]*1.1
        self.__direction = direction
        
    def stop_moving_left (self):
        ''' Stops the player from moving left '''
        self.__moving = False
        self.__dx = 0
        self.image = pygame.image.load("stand_left0.png")
          
    def stop_moving_right (self):
        ''' Stops the player from moving right '''
        self.__moving = False
        self.__dx = 0
        self.image = pygame.image.load("stand_right0.png") 
        
    def update(self):
        ''' The update method for player used to update player sprites '''
        # Add 1 to the frame count, and makes the direction x to its negative value
        self.__frameCount += 1    
        if ((self.rect.left > 0) and (self.__dx > 0)) or\
             ((self.rect.right< self.__screen.get_width()) and (self.__dx < 0)):
            self.rect.left -= (self.__dx*5)
            
        # Updates the Right Side
        if self.__moving == True and self.__direction == 2:
            self.image = self.__goRightSprites[self.__rightCount]
            if (self.__frameCount % 4 == 0):
                self.__rightCount +=1
            if self.__rightCount >= 3:
                self.__rightCount = 1
        # Updates the Left Side
        if self.__moving == True and self.__direction == 1:
            self.image = self.__goLeftSprites[self.__leftCount]
            if (self.__frameCount % 4 == 0):
                self.__leftCount +=1
            if self.__leftCount >= 3:
                self.__leftCount = 1
                
        #Makes the player go into shooting position (left)    
        if (self.__isShooting== True) and (self.__direction2 ==1) :
            self.image = self.__shoot_left
        #Makes the player go into shooting position (right)       
        if (self.__isShooting== True) and (self.__direction2 ==2) : 
            self.image = self.__shoot_right     
               
                
    def direction_x (self,value2):
        ''' Assigns direction2 to value2'''
        self.__set_direction = value2            
     
    def return_direction_x (self):
        '''This function returns the value of self.__direction2'''          
        return self.__set_direction
    
    def shoot (self):
        '''This function sets the isShooting to true which allows the player to shoot
        and stops the player from moving'''
        self.__isShooting = True
        self.__dx = 0
        
    def stop_shooting (self):
        ''' Stops the player from shooting '''
        self.__isShooting = False
       
                
class Mob(pygame.sprite.Sprite):
    def __init__(self,screen):
        ''' Initializer method for Mob (aka Monster)'''
       # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self) 
        self.__width = screen.get_width()
        self.__height = screen.get_height()
        self.xcenter = random.randrange(2,400,30)
        self.ycenter = 347
        self.__dx = 1
        self.__dy  = 0
        self.__screen = screen
       
        # Set the image and rect attributes for the mobs
        self.image = pygame.image.load("./Sprites/slime_stand_left0.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.xcenter, self.ycenter)        
        
        # Right Sprites list, loading sprites, keeping count of ust s, and count of right
        self.__goRightSprites = []
        for image_number in range (0,5):
            self.__right_image_pack  = pygame.image.load ("./Sprites/slime_walk_right" + str(image_number)+ ".png")
            self.__goRightSprites.append(self.__right_image_pack)
        self.__rightCount = 0  
        
        # Left Sprites list, loading sprites, keeping count of frames, and count of left
        self.__goLeftSprites = []
        for image_number in range (0,5):
            self.__left_image_pack = pygame.image.load ("./Sprites/slime_walk_left" + str(image_number)+ ".png")
            self.__goLeftSprites.append( self.__left_image_pack)
        self.__leftCount = 0  
        
        # Set Frame Count to 0 and Moving to False
        self.__frameCount = 0 
    
    def update(self):
        ''' Update method for Mob used to update Mob sprites '''
        self.__frameCount += 1    
        if ((self.rect.left > 0.0) and (self.__dx > 0)) or\
             ((self.rect.right< self.__screen.get_width()) and (self.__dx < 0)):
            self.rect.left -= (self.__dx *5)
        else:
            self.__dx =-self.__dx        
        
        #  Right Side                   
        if (self.__frameCount % 4 == 0) and self.__dx == -1:
                self.__rightCount +=1
                if self.__rightCount >= 3:
                    self.__rightCount = 0
                self.image = self.__goRightSprites[self.__rightCount]
        # Left Side    
        if (self.__frameCount % 4 == 0) and self.__dx == 1:
                self.__leftCount +=1
                if self.__leftCount >= 3:
                    self.__leftCount = 0
                self.image = self.__goLeftSprites[self.__leftCount]
              
class Scorekeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Impact", and
        sets the starting score to 0 and life to 3'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Load our font, and initialize the starting score and life of ple player.
        self.__font = pygame.font.SysFont("Arial", 18)
        self.__monster_kills = 0
        self.__player_HP = 30000
        self.__progress = 0
        self.spawnMore = False
                
    def life_loss(self):
        '''This method minus 1 off of the player's life everytime its` called'''
        self.__player_HP -=100
        
    def progress(self):
        ''' Adds 1 to the progress '''
        self.__progress +=1
          
    def monster_kill(self):
        ''' Adds 1 to the monster kills and 1 to the progress '''
        self.__monster_kills += 1
        self.__progress +=1
    
    def player_dead(self):
        ''' Checks if the player is dead or not '''
        if self.__player_HP<= 0:
            return True
        else:
            return False
    
    def update(self):
        '''This method will be called automatically to display 
        the current score and number of lives at the top of the game window.'''
        message = "Monster Killed: %d" %(self.__monster_kills) + \
                "       HP : %d" % (self.__player_HP)
        self.image = self.__font.render(message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (380, 15)   
         
        # Spawn More
        if self.__progress >= 2:
            self.spawnMore = True
            self.__progress = 0
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x_y,direction):
        '''This initializer takes a screen surface,x and y positions and the direction as a parameter.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.__width = screen.get_width()
        self.__height = screen.get_height() 
        self.xcenter = x_y[0]+32
        self.ycenter = x_y[1]
        self.__dx = 10
        self.__dy  = -6
        self.image = pygame.image.load("./Sprites/bullet_hit_left0.png")   
        self.image.convert()        
        self.rect = self.image.get_rect()          
        self.rect.center = (self.xcenter, self.ycenter)
        self.__screen = screen 
        self.__direction = direction         
        # Loads the left images
        self.__goLeftImages = []
        for image_num in range(0,4): 
            self.__goLeftImages.append(pygame.image.load('./Sprites/bullet_hit_left'+str(image_num)+".png"))
            self.__left_image_count = 0          
        # Loads right images
        self.__goRightImages = []
        for image_num in range(0,4): 
            self.__goRight_image_pack = pygame.image.load('./Sprites/bullet_hit_right'+str(image_num)+".png")
            self.__goRightImages.append(self.__goRight_image_pack) 
        self.__right_image_count= 0
     
        # Frame counter
        self.__framecount = 0
          
    def update (self):
        self.__framecount +=1
        self.rect.left -= (self.__dx*5)
        if self.rect.right < -10 or self.rect.left > self.__screen.get_width():
            self.kill()               
       
        # Sets the speed and Direction of the Bullet Sprites
        if self.__direction ==1:
            self.__dx = 5
        if self.__direction ==2:
            self.__dx = -5   
                       
        # Animating going left pictures       
        if (self.__direction ==2) :
            self.image = self.__goLeftImages[self.__left_image_count]            
            self.__left_image_count += 1  
            if self.__left_image_count>= 1:
                self.__left_image_count =0 
               
        # Animating going right pictures
        if (self.__direction ==1) :
            self.image = self.__goRightImages[self.__right_image_count]                         
            self.__right_image_count+=1
                    
            if self.__right_image_count >= 1:
                self.__right_image_count =0 


          
              
 

