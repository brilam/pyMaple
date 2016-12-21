'''
Author: Brian Lam

Version: v1.10

Game Name: pyMaple

Description: This contains the mainline logic, and the main menu function which
explains how the game is played.

Project description: A game where the player plays to the end. In other words, 
they'll play for as long as they survive. The objective of the game is simply to
survive from the monsters attacking you. An attack is considered a collision 
between you and the monster.
'''

import pygame, myMapleSprites
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640, 480))

# Define a main_menu function for the game
def main_menu():
   ''' This functions accepts the high score as a parameter. It also shows
   game instructions, and allows the user to start the game'''
   
   # D - Display
   
   # A - Assign
   clock = pygame.time.Clock()
   quit_game = False
   keepGoing = True
   mobCount = 0

   # Hide the mouse pointer
   pygame.mouse.set_visible(False)
   
   # L - Loop
   while keepGoing:
      
      #T- Time
      clock.tick(30)
   
      # E - Event Handling
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            keepGoing = False
            quit_game = True
         elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               keepGoing = False
               quit_game = True
            else:
               keepGoing = False
               quit_Game = False
               
      pygame.display.flip()
   
   return quit_game

# Defines the main function, which is the game
def main():
   '''This function defines the 'mainline logic' for our game.'''
   
   # D - Display
   pygame.display.set_caption("pyMaple ICS3U Summative")
   
   # E - Entities
   background = pygame.Surface(screen.get_size())       
   background = pygame.image.load ("background2.png")
   background.convert()
   bgm = pygame.mixer.music
   bgm.load ("AltarOfAkayrum.mp3")
   bgm.set_volume(0.1)
   bgm.play(-1)
   slimeDeath = pygame.mixer.Sound("./Sounds/SlimeDie.wav")
   gunShot = pygame.mixer.Sound("./Sounds/GunSound.wav")
   # Creating Sprites, and sprite group
   player = myMapleSprites.Player(screen)
   slime = myMapleSprites.Mob(screen)
   scorekeeper = myMapleSprites.Scorekeeper()
   bullet_group = pygame.sprite.Group()
   slime_group = pygame.sprite.Group(slime)
   allSprites = pygame.sprite.Group(slime_group,bullet_group,player,scorekeeper)
   
   # A - Assign
   clock = pygame.time.Clock()
   keepGoing = True
   quit_game = False
   
   # Hide the mouse pointer
   pygame.mouse.set_visible(False)

   # L - LOOP
   while not quit_game:
      quit_game = main_menu()
      if not quit_game:
         while keepGoing:
         
            # T- Time
            clock.tick(30)
      
      # EVENT HANDLING: Player uses the keyboard to move the player
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  keepGoing = False
               elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_RIGHT:
                     player.go_right((-1,0),2)
                     player.direction2(2)
                  if event.key == pygame.K_LEFT:
                     player.go_left((1,0),1)
                     player.direction2(1)
                  if event.key == pygame.K_LCTRL:
                     player.shoot()
                     gunShot.play()
                     bullet = myMapleSprites.Bullet(screen, player.rect.center,player.dir_ret())
                     bullet_group.add(bullet)
                     allSprites = pygame.sprite.OrderedUpdates(slime_group,bullet_group,player,scorekeeper)
               
               elif event.type == pygame.KEYUP:
                  if event.key == pygame.K_LEFT:
                     player.stop_moving_left()
                  if event.key == pygame.K_RIGHT:
                     player.stop_moving_right()
                  if event.key == pygame.K_LCTRL:
                     player.stop_shooting()
               
               # Checks if a bullet was fired at a slime and adds to kill and progress
               for fire in bullet_group:
                  hit = pygame.sprite.spritecollide(fire,slime_group, False)     
                  if hit:
                     slimeDeath.play()
                     fire.kill()
                     hit[0].kill()
                     scorekeeper.monster_kill() 
                     scorekeeper.progress()
                     
               # Adds slime upon kills     
               if scorekeeper.spawnMore == True:
                  slime = myMapleSprites.Mob(screen)
                  slime_group.add(slime)
                  allSprites = pygame.sprite.Group(slime_group,bullet_group,player,scorekeeper)
                  scorekeeper.spawnMore = False
                     
            #Checks for monster collision and deducts health      
            monsterCollision = pygame.sprite.spritecollide(player, slime_group, False)
            for monster in monsterCollision:                   
               scorekeeper.life_loss()
               
            # If the player is dead the game ends
            if scorekeeper.player_dead(): 
               keepGoing = False
            
           # If the game is stopped, the background music fades out          
            if keepGoing == False:
               bgm.fadeout(2000)
      
            # R - Refresh Screen   
            screen.blit(background, (0, 0)) 
            allSprites.clear(screen, background)
            allSprites.update()
            allSprites.draw(screen)
            pygame.display.flip()
   
         # Quits the Game   
         keepGoing = False
         quit_game = True
         
      pygame.quit()

# Calls the main function
main()