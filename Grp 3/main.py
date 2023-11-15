# Intialize
import pygame
import random
pygame.init()

#Settings
width = 600
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("SEA SHOOTER")
font = pygame.font.SysFont(None, 36)

global score
score = 0

assets = {
    "player":[pygame.image.load("assets/sprite_mermaid0.png")],
    "background":[pygame.image.load("assets/lava1.png"),pygame.image.load("assets/lava2.png"),pygame.image.load("assets/lava3.png"),pygame.image.load("assets/lava4.png")],
    "asteriod":[pygame.image.load("assets/submarine.png")],
    "bullet":[pygame.image.load("assets/New Piskel (1).png")],
    "bgm":pygame.mixer.Sound("assets/music1.mp3"),
    "pew":pygame.mixer.Sound("assets/fart.mp3")
}
cooldown = {"dash":0}

#Set an icon
pygame.display.set_icon(assets["player"][0])

frame_count = 0
shoot_delay = 30

#Setting the framerate
FPS = 60 #This is just a variable which we will call later with clock
clock = pygame.time.Clock()
run = True

def choice():
    r_num = random.random();
    if r_num > 0.8:
        return True;
    else:
        return False;

class Animation:
    def __init__(self,imgs,reverse,interval):
        self.index = 0
        self.imgs = imgs
        self.direction = 1
        self.reverse = reverse
        self.interval = interval
        self.interval_index = 0
    def display(self):
        self.interval_index += 1
        if self.interval_index == self.interval:
            self.interval_index = 0
            if self.index < len(self.imgs)-1 and self.index >= 0 :
                self.index += self.direction
            else:
                if self.reverse:
                    self.direction *= -1
                    self.index += self.direction
                else:
                    self.index = 0
        result = self.imgs[self.index]
        return result

class Object(pygame.sprite.Sprite):
    def __init__(self,name,imgs,reverse,pos,interval,hitbox=False):
        super().__init__()
        self.name = name
        self.pos = pos
        self.animations = Animation(imgs,reverse,interval)
        self.image = self.animations.display()
        if hitbox != False:
            self.rect = pygame.Rect(self.pos[0],self.pos[1],self.image.get_width(),self.image.get_height())
        else:
            self.rect = pygame.Rect(self.pos[0],self.pos[1],0,0)
    def update(self):
        self.image = self.animations.display()
    

class Player(Object):
    def __init__(self,pos):
        super().__init__("player",assets["player"],False,pos,30,True)
        self.velocity = [0,0]
        self.acc = [0,0]
        self.max = 3
    def update(self):
        super().update()
        #Change velcity
        self.velocity[0] += self.acc[0]
        self.velocity[1] += self.acc[1]
        #Apply maximum velocity
        if self.velocity[0] > self.max:
            self.velocity[0] = self.max
        if self.velocity[0] < -self.max:
            self.velocity[0] = -self.max
        if self.velocity[1] > self.max:
            self.velocity[1] = self.max
        if self.velocity[1] < -self.max:
            self.velocity[1] = -self.max
        #Add resistance
        if self.velocity[0] > 0:
            self.velocity[0] -= 0.1
        if self.velocity[1] > 0:
            self.velocity[1] -= 0.1
        if self.velocity[0] < 0:
            self.velocity[0] += 0.1
        if self.velocity[1] < 0:
            self.velocity[1] += 0.1
            
        #Change position: x-axis and y-axis
        #Checking on x-axis
        collided_x = False
        self.rect = pygame.Rect(self.pos[0]+self.velocity[0],self.pos[1],self.image.get_width(),self.image.get_height()) #A forecast
        for sprite in pygame.sprite.spritecollide(self,game,False): #Check if anything collided
            if sprite.name == "asteriod" and sprite.rigid == True:
                collided_x = True
                break
        if collided_x: #If collided, don't move, and don't change the position
            self.velocity[0] = 0
        else:
            self.pos[0] += self.velocity[0]
            
        #Checking on y-axis
        collided_y = False
        self.rect = pygame.Rect(self.pos[0],self.pos[1]+self.velocity[1],self.image.get_width(),self.image.get_height()) #A forecast
        for sprite in pygame.sprite.spritecollide(self,game,False): #Check if anything collided
            if sprite.name == "asteriod" and sprite.rigid == True:
                collided_y = True
                break
        if collided_y: #If collided, don't move, and don't change the position
            self.velocity[1] = 0
        else:
            self.pos[1] += self.velocity[1]
            
        #Update the rect based on the checked value of pos
        self.rect = self.rect = pygame.Rect(self.pos[0],self.pos[1],self.image.get_width(),self.image.get_height())
        #Limit the player in the screen
        if self.pos[0] > width-self.image.get_width():
            self.pos[0] = width-self.image.get_width()
        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[1]  > height-self.image.get_height():
            self.pos[1] = height-self.image.get_height()
        if self.pos[1]  < 0:
            self.pos[1] = 0

class Asteriod(Object): # create asteroids to shoot
    def __init__(self,image,location,rigid):
        super().__init__("asteroid",[image],False,location,60,True)
        self.rigid = rigid
        self.velocity = [0,2]
        self.very_fast = choice();
        self.very_slow = choice();
        self.move_left = choice();
    def update(self):
        global alive
        super().update()
        if self.very_fast:
            self.velocity[1] += 20;
        elif self.very_slow:
            self.velocity[1] -= 5;
        
        if self.move_left:
            self.velocity[0] += 10;

        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.image.get_width(),self.image.get_height())
        #Check for collision
        for sprite in pygame.sprite.spritecollide(self,game,False):
            if sprite.name == "bullet": #Kill both bulle and asteriod
                self.kill()
                sprite.kill()
                
                break
            if sprite.name == "player":
                alive  = False

class Bullet(Object): # create bullets for the player
    def __init__(self,location):
        surface = pygame.Surface((2,12))  #Create a surface, which is basically a image filled with solid color
        surface.fill((255, 0, 220)) #Fill the surface with a color
        super().__init__("bullet",assets["bullet"],False,location,60,True) 
        self.velocity = [0,-8] #Travel upwards
        if self.velocity[1] < 0:
            self.velocity[1] -= 0.05
            
    def update(self): 
        super().update()
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.image.get_width(),self.image.get_height())
        if self.pos[1] < -20:
            self.kill() #This deletes the object, it is a method from the sprite class
        if self.velocity == 0:
             self.kill()
        
        
class Mouse(Object):
    def __init__(self):
        surface = pygame.Surface((10,10))
        mouse_pos = pygame.mouse.get_pos()
        super().__init__("mouse",[surface],True,mouse_pos,60,True)
    def update(self):
        super().update()
        mouse_pos = pygame.mouse.get_pos()
        self.pos = mouse_pos
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.image.get_width(),self.image.get_height())
class Button(Object):
    def __init__(self,location,text):
        surface = pygame.Surface((100,50))
        surface.fill((128, 128, 128))
        text_color = (255,255,255)
        button_font = pygame.font.SysFont(None, 20)
        button_word = button_font.render(text, True, text_color)
        # Calculate the center position of the text surface
        text_x = surface.get_width() // 2 - button_word.get_width() // 2
        text_y = surface.get_height() // 2 - button_word.get_height() // 2
        # Blit the text surface onto the button surface
        surface.blit(button_word, (text_x, text_y))
        super().__init__("button",[surface],False,location,60,True)
    def clicked(self):
        print("clicked")
    def update(self):
        super().update()
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]: #If left mouse button is pressed
            for sprite in pygame.sprite.spritecollide(self,game,False):
                if sprite.name == "mouse":
                    self.clicked()
                    
class AgainButton(Button):
    def __init__(self,location):
        super().__init__(location,"Play Again")
    def clicked(self):
        global again
        again = True

def get_sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0
        
def generate_bullet(player_obj):
    img = random.choice(assets["asteriod"])
    location = [player_obj.pos[0] + player_obj.image.get_width()/4 ,player_obj.pos[1]]
    game.add(Bullet(location))
    
def generate_asteriod():
    img = random.choice(assets["asteriod"])
    print(img)
    location = [random.choice(range(0,width-assets["asteriod"][0].get_width())),-1*assets["asteriod"][0].get_height()]
    game.add(Asteriod(img,location,False))

pygame.mixer.Channel(0).play(assets["bgm"],1,fade_ms=500)



while run:


    game = pygame.sprite.Group()
    player = Player([width/2-assets["player"][0].get_height()/2,height-assets["player"][0].get_height()])
    background = Object("background",assets["background"],False,[0,0],30)
    game.add()
    game.add(Object("background",assets["background"],False,[0,0],30))

    game.add(player)
    # game.add(Asteriod(assets["asteriod"][0],[width/2,height/2],True))
    # game.add(Asteriod(assets["asteriod"][0],[0,0],False))
    alive = True
    while alive:
        frame_count += 1
        if frame_count > shoot_delay:
            pygame.mixer.Channel(1).play(assets["pew"]) 
            generate_bullet(player) 
            generate_bullet(player)
            generate_bullet(player)
            score += 1

         
            frame_count = 0
        queue = pygame.event.get()
        if cooldown["dash"] > 0:
            cooldown["dash"] -= 1
        for event in queue:
            acc = 0.15
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.unicode == "s":
                    player.acc[1] += -acc
                if event.unicode == "d":
                    player.acc[0] += -acc
                if event.unicode == "w":
                    player.acc[1] += acc
                if event.unicode == "a":
                    player.acc[0] += acc
                if event.unicode == " ":
                    if cooldown["dash"] == 0:
                        cooldown["dash"] = 60
                        if abs(player.velocity[0]) > 0.1:
                            player.velocity[0] = get_sign(player.velocity[0]) * player.max
                        if abs(player.velocity[1]) > 0.1:
                            player.velocity[1] = get_sign(player.velocity[1]) * player.max

                    
            if event.type == pygame.KEYUP:
                if event.unicode == "s":
                    player.acc[1] -= -acc
                if event.unicode == "d":
                    player.acc[0] -= -acc
                if event.unicode == "w":
                    player.acc[1] -= acc
                if event.unicode == "a":
                    player.acc[0] -= acc
        if random.choice(range(100)) < 25:
            generate_asteriod(player)

        game.update()
        screen.fill((0,0,0))
        game.draw(screen)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))  # White color
        screen.blit(score_text, (10, 10))  # Draw the text at position (10, 10)

        clock.tick(FPS)
        pygame.display.flip()

    game = pygame.sprite.Group()
    game.add(Mouse())
    game.add(AgainButton((width/2-50,height/2-25)))
    score = 0
    
    
    
    again = False
    while again == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        game.update()
        screen.fill((0,0,0))
        game.draw(screen)

        clock.tick(FPS)
        pygame.display.flip()
