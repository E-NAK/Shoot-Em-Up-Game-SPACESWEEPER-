from pygame import*
from random import* 
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

init()
#Size of window
size = width, height = 1000, 700
screen = display.set_mode(size)
display.set_caption("Space Sweeper")

#colours
BLACK = (0, 0, 0)
lightBLACK = (9, 10, 15)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)

#BLUE
BLUE = (0,0,255)
lightBLUE = (75,122,250)
deepBLUE = (24,52,129)

#Font
myFont = font.Font("KaneFont.ttf",35) # Source:https://www.1001fonts.com/terminator-real-nfi-font.html
storyFont = font.Font("KaneFont.ttf",25)
ruleFont = font.Font("KaneFont.ttf",20)

# load images
#backgrounds
menuBackground = image.load("MenuBackground.jpg")         
menuBackground = transform.scale(menuBackground, (width, height))# Source:https://spectrum.ieee.org/tech-talk/aerospace/satellites/european-space-agency-esa-mission-news-orbital-debris-solar-storms

gameBackground = image.load("GameBackground.jpg")
gameBackground = transform.scale(gameBackground, (width, height))# Source:

ruleBackground = image.load("RuleBackground.jpg")
ruleBackground = transform.scale(ruleBackground, (width, height))# Source:https://spaceships-spacestations.tumblr.com/

resultBackground = image.load("resultBackground.jpg")
resultBackground = transform.scale(resultBackground,(width,height))

#Spaceship
spaceship = image.load("Redspaceship.png")
spaceship = transform.scale(spaceship, (spaceship.get_width(), spaceship.get_height()))

yellowship = image.load("Yellowspaceship.png")
yellowship = transform.scale(yellowship, (spaceship.get_width(), spaceship.get_height()))

staminaS = image.load("stamina ship.png")
staminaS = transform.scale(staminaS, (25,25))

nuclearS = image.load("nuclear.png")
nuclearS = transform.scale(nuclearS, (25,25))

#Debris
debris1 = image.load("debris1.png")
debris1 = transform.scale(debris1, (spaceship.get_width(), spaceship.get_height()))

debris2 = image.load("debris2.png")
debris2 = transform.scale(debris2, (spaceship.get_width(), spaceship.get_height()))

debris3 = image.load("debris3.png")
debris3 = transform.scale(debris3, (spaceship.get_width(), spaceship.get_height()))

debris4 = image.load("debris4.png")
debris4 = transform.scale(debris4, (spaceship.get_width()*2, spaceship.get_height()))

debris5 = image.load("debris5.png")
debris5 = transform.scale(debris5, (spaceship.get_width(), spaceship.get_height()*2))

debris6 = image.load("debris6.png")
debris6 = transform.scale(debris6, (spaceship.get_width(), spaceship.get_height()*2))

debris7 = image.load("debris7.png")
debris7 = transform.scale(debris7, (spaceship.get_width(), spaceship.get_height()))

# meteorolite
mete1 = image.load("mete1.png")
mete1 = transform.scale(mete1, (spaceship.get_width(), spaceship.get_height()*2))

mete2 = image.load("mete2.png")
mete2 = transform.scale(mete2, (spaceship.get_width(), spaceship.get_height()))

mete3 = image.load("mete3.png")
mete3 = transform.scale(mete3, (spaceship.get_width(), spaceship.get_height())) 

mete4 = image.load("mete4.png")
mete4 = transform.scale(mete4, (spaceship.get_width(), spaceship.get_height())) 

# bullet
blueBullet = image.load("blueBullet.png")
blueBullet = transform.scale(blueBullet,(10,30))

yellowBullet = image.load("yellowBullet.png")
yellowBullet = transform.scale(yellowBullet,(10,30))

#crates
health = image.load("healcrate.png")
health = transform.scale(health,(50,50))

SD = image.load("spaceshipspeed.png")
SD = transform.scale(SD,(50,50))

moreBullet = image.load("moreBullet.png")
moreBullet = transform.scale(moreBullet,(50,50))

nuclearC = image.load("nuclearC.png")
nuclearC = transform.scale(nuclearC,(50,50))

#Rules
keyb = image.load("keyboard.png")
keyup = transform.scale(keyb,(50,50))

keyleft = transform.rotate(keyb,90)
keyleft = transform.scale(keyleft,(50,50))

keydown = transform.rotate(keyb,180)
keydown = transform.scale(keydown,(50,50))

keyright = transform.rotate(keyb,270)
keyright = transform.scale(keyright,(50,50))

space = image.load("space.png")
space = transform.scale(space,(400,70))

spaceship2 = transform.scale(spaceship,(100,100))

scorep = image.load("score.png")
scorep = transform.scale(scorep,(160,110))

page2 = image.load("page2.png")
page2 = transform.scale(page2,(875,510))

# chose
spaceship3 = transform.scale(spaceship,(width//5,height//4))
yellowship2 = transform.scale(yellowship,(width//5,height//4))

# result
salute = image.load("salute.png")
salute = transform.scale(salute,(salute.get_width()//2, salute.get_height()//2))

# story
storyP = image.load("storyP.png")
storyP = transform.scale(storyP,(870,505))

#load music
"""menuSound = mixer.Sound("startMusic.wav")
mixer.Sound.play(menuSound,-1)
gameSound = mixer.Sound("gameMusic.wav")"""

# states in the game
MENU_STATE = 0
GAME_STATE = 1
#rules
RULE_STATE = 2
RULE2_STATE = 3
RULE3_STATE = 4
CHOSE_STATE = 5
STORY_STATE = 6
QUIT_STATE = 7
RESULT_STATE = 8

# movement key booleans
PRESS_RIGHT = False
PRESS_LEFT = False
PRESS_UP = False
PRESS_DOWN = False

#Global
def drawMenu(screen, button, mx, my, state):
    screen.blit(menuBackground, Rect(0, 0, width, height))
    blockwidth = width//8
    blockheight = width//8
    
    #Big Title
    draw.rect(screen, deepBLUE, (blockwidth//4, blockheight//2, blockwidth*4.5, blockheight//1.5))
    draw.rect(screen, BLACK, (blockwidth//4, blockheight//2, blockwidth*4.5, blockheight//1.5),3)
    text = myFont.render("SPACE SWEEPER", 1, WHITE)
    textwidth, textheight = myFont.size("SPACE SWEEPER") # get the font size
    useW = (blockwidth*4.5 - textwidth)//2  #use for centering
    useH = (blockheight//1.5 - textheight)//2 
    textRect = Rect(blockwidth//4 + useW, blockheight//2 + useH,textwidth,textheight)
    screen.blit(text,textRect)
    
    #Story Click
    draw.rect(screen,deepBLUE,(810,530,160,140))
    draw.rect(screen,BLACK,(807,527,166,146),3)
    rect = draw.rect(screen,deepBLUE,(810,530,160,140))
    text = storyFont.render("BACK",1,WHITE)
    textwidth, textheight = storyFont.size("BACK")
    textRect = Rect(837,575,textwidth,textheight)
    screen.blit(text,textRect)    
    text = storyFont.render("STORY",1,WHITE)
    textwidth, textheight = storyFont.size("STORY")
    textRect = Rect(817,600,textwidth,textheight)
    screen.blit(text,textRect)        
    
    if rect.collidepoint(mx,my):
        draw.rect(screen,BLACK,rect,5)
        if button == 1:
            state = STORY_STATE
            
    #Menu Options
    rectList = [Rect(blockwidth*1.25, 1.5*blockheight, blockwidth*2, blockheight//2),  #game choice
                Rect(blockwidth*1.25, 2.5*blockheight, blockwidth*2, blockheight//2), #rule choice
                Rect(blockwidth*1.25, 3.5*blockheight, blockwidth*2, blockheight//2)] #quit choice
    stateList = [CHOSE_STATE,RULE_STATE,QUIT_STATE]
    titleList = ["START", "RULES", "QUIT"]
    
    for i in range(len(rectList)):
        rect = rectList[i]
        draw.rect(screen,lightBLUE,rect)
        draw.rect(screen,BLACK,rect,3)
        text = myFont.render(titleList[i] , 1, BLACK)
        textwidth, textheight = myFont.size(titleList[i]) # get the font size
        useW = (blockwidth*2 - textwidth)//2  #use for centering
        useH = (blockheight//2 - textheight)//2 
        textRect = Rect(rect[0]+useW, rect[1]+useH, textwidth, textheight)
        screen.blit(text, textRect)	# draw to screen        
        if rect.collidepoint(mx,my):
            draw.rect(screen,BLACK,rect,5)
            if button == 1:
                state = stateList[i]
    return state


def chosePage(screen,button,mx,my,state):
    global bulletC,shipC
    screen.blit(ruleBackground,Rect(0,0,width,height))
    blockwidth = width//8
    blockheight = width//8 
    
    draw.rect(screen, deepBLUE, (blockwidth//4+30, blockheight//2+20, blockwidth*7, blockheight//1.5))
    draw.rect(screen, BLACK, (blockwidth//4+30, blockheight//2+20, blockwidth*7, blockheight//1.5),3)
    text = myFont.render("CHOOSE YOUR SPACESHIP", 1, WHITE)
    textwidth, textheight = myFont.size("CHOOSE YOUR SPACESHIP") # get the font size
    useW = (blockwidth*7 - textwidth)//2  #use for centering
    useH = (blockheight//1.5 - textheight)//2 
    textRect = Rect(blockwidth//4 + useW + 30, blockheight//2 + useH + 20,textwidth,textheight)
    screen.blit(text,textRect)
    
    #select
    draw.rect(screen,lightBLUE,(width//8+50,height//3,width//4,height//3))
    draw.rect(screen,lightBLUE,(width//8*5-50,height//3,width//4,height//3))
    
    draw.rect(screen,BLACK,(width//8+50,height//3,width//4,height//3),3)
    draw.rect(screen,BLACK,(width//8*5-50,height//3,width//4,height//3),3)  
    
    screen.blit(spaceship3,Rect(width//8+73,height//3+25,width//4,height//3))
    screen.blit(yellowship2,Rect(width//8*5-28,height//3+25,width//4,height//3))
    
    
    rectList = [Rect(width//8+50,height//3,width//4,height//3),
                Rect(width//8*5-50,height//3,width//4,height//3)]
    
    for i in range(len(rectList)):
        rect = rectList[i]
        if rect.collidepoint(mx,my):
            draw.rect(screen,BLACK,rect,5)
            if button == 1:     
                if rect == Rect(width//8+50,height//3,width//4,height//3):
                    state = GAME_STATE
                    bulletC = blueBullet
                    shipC = spaceship
                if rect == Rect(width//8*5-50,height//3,width//4,height//3):
                    state = GAME_STATE
                    bulletC = yellowBullet
                    shipC = yellowship 
                
    
    return state,bulletC,shipC

def drawGame(screen,button,mx,my,state,shipX,shipY,bulletC,shipC):
    global missiley, shotTimer, stamina, nuclear, BS, debrisP, moveRate, score
    global dt1,d1outTime, dt2, d2outTime, dt3, d3outTime, dt4, d4outTime, dt5, d5outTime, dt6, d6outTime, dt7, d7outTime
    global mt1, m1outTime, mt2, m2outTime, mt3, m3outTime, mt4, m4outTime
    global ct1,c1outTime, ct2, c2outTime, c2getTime, ct3, c3outTime, c3getTime, ct4,c4outTime
    global d1s, d2s, d3s, d4s, d5s, d6s, d7s
    
    # Music
    """mixer.Sound.stop(menuSound) 
    mixer.Sound.play(gameSound,-1)"""    
    
    #scorlling background 
    screen.blit(gameBackground, Rect(0,backx,width,height))   
    screen.blit(gameBackground, Rect(0, backx - height, width, height))
    
    #Back click
    draw.rect(screen,lightBLACK,(820,20,166,50),3)
    rect = draw.rect(screen,lightBLACK,(820,20,166,50))
    text = storyFont.render("MENU",1,WHITE)
    textwidth, textheight = storyFont.size("MENU")
    textRect = Rect(847,35,textwidth,textheight)
    screen.blit(text,textRect)    
    if rect.collidepoint(mx,my):
        draw.rect(screen,BLACK,rect,5)
        if button == 1:
            state = MENU_STATE   
    
    #score
    text = storyFont.render(str(score),1,WHITE)
    textwidth, textheight = storyFont.size(str(score))
    textRect = Rect(30,85,textwidth,textheight)
    screen.blit(text,textRect)      
     
    # starmina and nuclear ships:
    for i in range (stamina):
        staminaRect = Rect(int((i+1)*30),20,spaceship.get_width(), spaceship.get_height())
        screen.blit(staminaS,staminaRect)
    
    for n in range (nuclear):
        nuclearRect = Rect((int((n+1)*30),50,spaceship.get_width(), spaceship.get_height()))
        screen.blit(nuclearS,nuclearRect)
    
    #drawmete:
    mete1Rect = Rect(mt1[0],mt1[1],spaceship.get_width(), spaceship.get_height()*2)
    screen.blit(mete1,mete1Rect)
    
    mete2Rect = Rect(mt2[0],mt2[1],spaceship.get_width(), spaceship.get_height())
    screen.blit(mete2,mete2Rect)    
    
    mete3Rect = Rect(mt3[0],mt3[1],spaceship.get_width(), spaceship.get_height())
    screen.blit(mete3,mete3Rect)    
    
    mete4Rect = Rect(mt4[0],mt4[1],spaceship.get_width(), spaceship.get_height())
    screen.blit(mete4,mete4Rect)        
    
    meteList = [mete1Rect,mete2Rect,mete3Rect,mete4Rect]
    
    mt1[1]+= 5
    if mt1[1] >= 800:
        if time.get_ticks() - m1outTime >= 20000:
            mt1 = initMete1()
            m1outTime = time.get_ticks()
    
    mt2[0] -= 5
    mt2[1] += 5
    if mt2[1] >= 800 and mt2[0] <= 0:
        if time.get_ticks() - m2outTime >= 5000:
            mt2 = initMete2()
            m2outTime = time.get_ticks() 
    
    mt3[0] += 5
    mt3[1] += 5
    if mt3[1] >= 800 and mt3[0] >= 1000:
        if time.get_ticks() - m3outTime >= 5000:
            mt3 = initMete3()
            m3outTime = time.get_ticks()    
            mt1[1]+= 5
    
    mt4[1]+= 5
    if mt4[1] >= 800:
        if time.get_ticks() - m4outTime >= 10000:
            mt4 = initMete4()
            m4outTime = time.get_ticks()    
    
    #drawcrate:
    crate1Rect = Rect(ct1[0],ct1[1],50,50)
    screen.blit(health,crate1Rect)    
    
    crate2Rect = Rect(ct2[0],ct2[1], 50,50)
    screen.blit(SD,crate2Rect)        
    
    crate3Rect = Rect(ct3[0],ct3[1], 50,50)
    screen.blit(moreBullet,crate3Rect)           
    
    crate4Rect = Rect(ct4[0],ct4[1], 50,50)
    screen.blit(nuclearC,crate4Rect)    
    
    crateList = [crate1Rect,crate2Rect,crate3Rect,crate4Rect]    
    
    ct1[1] += 2
    if ct1[1] >= 700:
        if time.get_ticks()- c1outTime >= 1000: 
            ct1 = initTarget()
            ct1[1] = -1000
            c1outTime = time.get_ticks()   
    
    ct2[1] += 2
    if ct2[1] >= 700:
        if time.get_ticks()- c2outTime >= 1000:
            ct2 = initTarget2()
            ct2[1] = -1000
            c2outTime = time.get_ticks()
      
    ct3[1] += 2
    if ct3[1] >= 700:
        if time.get_ticks()- c3outTime >= 1000:
            ct3 = initTarget3()
            ct3[1] = -1000
            c3outTime = time.get_ticks()   
   
    ct4[1] += 2
    if ct4[1] >= 700:
        if time.get_ticks()- c4outTime >= 1000:
            ct4 = initTarget4()
            ct4[1] = -1000
            c4outTime = time.get_ticks()               
            
    #drawDebris
    debris1Rect = Rect(dt1[0],dt1[1],spaceship.get_width(), spaceship.get_height())
    screen.blit(debris1,debris1Rect)
    
    debris2Rect = Rect(dt2[0],dt2[1],spaceship.get_width(), spaceship.get_height())
    screen.blit(debris2,debris2Rect)    
    
    debris3Rect = Rect(dt3[0],dt3[1],spaceship.get_width(), spaceship.get_height())
    screen.blit(debris3,debris3Rect)    
    
    debris4Rect = Rect(dt4[0],dt4[1],spaceship.get_width()*2, spaceship.get_height())
    screen.blit(debris4,debris4Rect)        
    
    debris5Rect = Rect(dt5[0],dt5[1],spaceship.get_width(), spaceship.get_height()*2)
    screen.blit(debris5,debris5Rect)  
    
    debris6Rect = Rect(dt6[0],dt6[1],spaceship.get_width(), spaceship.get_height()*2)
    screen.blit(debris6,debris6Rect)      
    
    debris7Rect = Rect(dt7[0],dt7[1],spaceship.get_width(), spaceship.get_height())
    screen.blit(debris7,debris7Rect)     
    
    debrisList = [debris1Rect,debris2Rect,debris3Rect,debris4Rect,debris5Rect,debris6Rect,debris7Rect]
    
    dt1[1] += 2
    if dt1[1] >= 700:
        if time.get_ticks()- d1outTime >= 5000:
            dt1 = initTarget()
            d1outTime = time.get_ticks()
        
    dt2[1]+= 2
    if dt2[1] >= 700:
        if time.get_ticks()- d2outTime >= 5000:
            dt2 = initTarget()
            d2outTime = time.get_ticks()   
            
    dt3[1]+= 2
    if dt3[1] >= 700:
        if time.get_ticks()- d3outTime >= 5000:
            dt3 = initTarget()
            d3outTime = time.get_ticks()   
    
    dt4[1]+= 2
    if dt4[1] >= 700:
        if time.get_ticks()- d4outTime >= 5000:
            dt4 = initTarget()
            d4outTime = time.get_ticks()       
            
    dt5[1]+= 2
    if dt5[1] >= 700:
        if time.get_ticks()- d5outTime >= 5000:
            dt5 = initTarget()
            d5outTime = time.get_ticks()                   
            
    dt6[1]+= 2
    if dt6[1] >= 700:
        if time.get_ticks()- d6outTime >= 5000:
            dt6 = initTarget()
            d6outTime = time.get_ticks()        
            
    dt7[1]+= 2
    if dt7[1] >= 700:
        if time.get_ticks()- d7outTime >= 5000:
            dt7 = initTarget()
            d7outTime = time.get_ticks()    

    #drawship
    shipRect = Rect(shipX, shipY, spaceship.get_width(), spaceship.get_height())
    screen.blit(shipC,shipRect)
    rect1 = Rect(shipX + 32, shipY, 10, 35) 
    rect2 = Rect(shipX + 20, shipY + 26, 35, 18)
    rect3 = Rect(shipX + 4, shipY + 44, 67, 35)
    
    rect4 = Rect(shipX + 20, shipY, 35, 43)
    rect5 = Rect(shipX, shipY + 43, 74, 32)
    hitList = [rect1, rect2, rect3, rect4, rect5]
    
        
    # missile staff:
    for i in range (len(missileListY)-1,-1,-1): # get each missile
        missiley = missileListY[i] 
        missilex = missileListX[i]
        screen.blit(bulletC,(missilex - 4,missiley,10,30))
        screen.blit(bulletC,(missilex + 20,missiley,10,30))
        missileListY[i] -= 10 # move missile down
        
        if missileListY[i] < 0:# if off screen
            del missileListY[i]# delete current missile
            del missileListX[i]
            
        if missileListX[i] < 0:# if off screen
            del missileListY[i]# delete current missile
            del missileListX[i]   
        
        # ship collision 
    for i in range (len(missileListY)-1, -1, -1): # get each missile
        missiley = missileListY[i] 
        missilex = missileListX[i]
        missileRect1 = Rect(missilex,missiley,10,30) 
        missileRect2 = Rect(missilex + 24,missiley,10,30) 
        missileList = [missileRect1,missileRect2]
        
        # debris with missile
        for m in range (len(debrisList)): 
            if (debrisList[m].collidelist(missileList) != -1):
                if debrisList[m] == debris1Rect:
                    d1s -= 1
                    score += 2
                    if d1s == 0:
                        dt1 = initTarget()
                        dt1[1] = -400
                        d1s = 40
                            
                elif debrisList[m] == debris2Rect:
                    d2s -= 1
                    score += 2
                    if d2s == 0:
                        dt2 = initTarget2()
                        dt2[1] = -500
                        d2s = 40
                    
                elif debrisList[m] == debris3Rect:
                    d3s -= 1
                    score += 3
                    if d3s == 0:
                        dt3 = initTarget3()
                        dt3[1] = -600
                        d3s = 60                    
                    
                elif debrisList[m] == debris4Rect:
                    d4s -= 1
                    score += 4
                    if d4s == 0:
                        dt4 = initTarget4()  
                        dt4[1] = -600
                        d4s = 70
                    
                elif debrisList[m] == debris5Rect:
                    d5s -= 1
                    score += 4
                    if d5s == 0: 
                        dt5 = initTarget5()
                        dt5[1] = -500
                        d5s = 70 
                    
                elif debrisList[m] == debris6Rect:
                    d6s -= 1
                    score += 3
                    if d6s == 0:
                        dt6 = initTarget6()
                        dt6[1] = -500   
                        d6s = 60
                
                elif debrisList[m] == debris7Rect:
                    d7s -= 1
                    score += 2
                    if d7s == 0:
                        dt7 = initTarget7()
                        dt7[1] = -500     
                        d7s = 40            
   
    # debris with spaceship
    for r in range (len(debrisList)):
        if(debrisList[r].collidelist(hitList) != -1):
            if debrisList[r] == debris1Rect:
                dt1 = initTarget()
                stamina -=1

            elif debrisList[r] == debris2Rect:
                dt2 = initTarget2()
                stamina -=1
            
            elif debrisList[r] == debris3Rect:
                dt3 = initTarget3()
                stamina -=1
                
            elif debrisList[r] == debris4Rect:
                dt4 = initTarget4()
                stamina -=1
                
            elif debrisList[r] == debris5Rect:
                dt5 = initTarget5()
                stamina -=1    
                
            elif debrisList[r] == debris6Rect:
                dt6 = initTarget6()
                stamina -=1
            
            elif debrisList[r] == debris7Rect:
                dt7 = initTarget7()
                stamina -=1            
            
    
    for m in range(len(meteList)):
        if(meteList[m].collidelist(hitList) != -1):
            if meteList[m] == mete1Rect:
                mt1 = initMete1()
                stamina -= 2
                
            if meteList[m] == mete2Rect:
                mt2 = initMete2()
                stamina -= 2
            
            if meteList[m] == mete3Rect:
                mt3 = initMete3()
                stamina -= 2            
            
            if meteList[m] == mete4Rect:
                mt4 = initMete4()
                stamina -= 2             
                  
    # crate collision with spaceship
    for c in range(len(crateList)):
        if(crateList[c].collidelist(hitList) != -1):
            if crateList[c] == crate1Rect:
                stamina += 1
                ct1 = initcrate1()
                 
            if crateList[c] == crate2Rect:
                c2getTime = time.get_ticks()
                moveRate = 10 
                ct2 = initcrate2()
            
            if crateList[c] == crate3Rect:
                c3getTime = time.get_ticks()
                BS = 50                
                ct3 = initcrate3()
                             
            if crateList[c] == crate4Rect:
                nuclear += 1                
                ct4 = initcrate4()
                                   
    if time.get_ticks() - c2getTime >= 15000:  
        moveRate = 5
    
    if time.get_ticks() - c3getTime >= 10000:
        BS = 100

    if time.get_ticks() - shotTimer >= BS: # 1 second difference
        missileListX.append(shipX+24) # add new missile
        missileListY.append(shipY+12)
        shotTimer = time.get_ticks() # reset timer
    display.flip()
    
    if button == 3:
        state = MENU_STATE
        """mixer.Sound.stop(gameSound)
        mixer.Sound.play(menuSound,-1)"""
    
    if stamina <= 0:
        state = RESULT_STATE
        """mixer.Sound.stop(gameSound)"""
    return state

def drawRule(screen,button,mx,my,state):
    screen.blit(ruleBackground, Rect(0, 0, width, height))
    blockwidth = width//8
    blockheight = width//8     
    screen.blit(ruleBackground, Rect(0,0, width, height))
    rect = Rect(blockwidth//2,blockheight//2,blockwidth*4.9+blockwidth*2.1,height-blockheight*1.5)
    draw.rect(screen,lightBLUE,rect)    
    rect = Rect(blockwidth//2,blockheight//2,blockwidth*4.9+blockwidth*2.1,height-blockheight*1.5)
    draw.rect(screen,BLACK,rect,3)   
    rect = Rect(blockwidth//2, blockheight*4.8, blockwidth*2.2, blockheight//1.75)
    rect = Rect(width//2+blockwidth*1.3, blockheight*4.8, blockwidth*2.2, blockheight//1.75)
    rectList3 = [Rect(blockwidth//2, blockheight*4.8, blockwidth*2.2, blockheight//1.75),
                 Rect(width//2+blockwidth*1.3, blockheight*4.8, blockwidth*2.2, blockheight//1.75)]    
    stateList3 = [MENU_STATE,RULE2_STATE]
    titleList3 = ["MENU","NEXT"]
    
    for i in range (len(rectList3)):
        rect = rectList3[i]
        draw.rect(screen,lightBLUE,rect)
        draw.rect(screen,BLACK,rect,3)
        text = myFont.render(titleList3[i] , 1, BLACK)
        textwidth, textheight = myFont.size(titleList3[i])
        if rectList3[i] == Rect(blockwidth//2, blockheight*4.8, blockwidth*2.2, blockheight//1.75):
            useW = (blockwidth*2.2 - textwidth)//2  #use for centering
            useH = (blockheight//1.75 - textheight)//2 
            textRect = Rect(blockwidth//2 + useW, blockheight*4.8 + useH,textwidth//2,textheight)        
        elif rectList3[i] == (width//2+blockwidth*1.3, blockheight*4.8, blockwidth*2.2, blockheight//1.75):
            useW = (blockwidth*2.2 - textwidth)//2  #use for centering
            useH = (blockheight//1.75 - textheight)//2   
            textRect = Rect(width//2+blockwidth*1.3 + useW, blockheight*4.8 + useH,textwidth//2,textheight)
        screen.blit(text,textRect)             
        if rect.collidepoint(mx,my):
            draw.rect(screen,BLACK,rect,5)
            if button == 1:
                state = stateList3[i]  
    
    draw.line(screen,BLACK,(width//2,blockheight//2),(width//2,((height - blockheight)//2)+30),3)
    draw.line(screen,BLACK,(blockwidth//2,(height-blockheight*1.5)//2+blockheight//2),(width-blockwidth//2,(height-blockheight*1.5)//2+blockheight//2),3)
    
    #movement control
    screen.blit(spaceship2,Rect(105,150,spaceship.get_width(), spaceship.get_height()))        
    screen.blit(keyup,Rect(width//3,height//5,50,50))
    screen.blit(keydown,Rect(width//3,height//5+60,50,50))
    screen.blit(keyleft,Rect(width//3-60,height//5+60,50,50))
    screen.blit(keyright,Rect(width//3+60,height//5+60,50,50))
    
    #stamina,muclear,score
    screen.blit(scorep,Rect(width//4*2+20,150,300,70))
    titleList3 = ["STAMINA", "NUCLEAR", "SCORE"]
    rectList3 = [Rect(width//4*2+210,160,120,30),
                 Rect(width//4*2+210,190,120,30),
                 Rect(width//4*2+210,220,120,30)]    
    
    for i in range (len(rectList3)):
        rect = rectList3[i]
        text = ruleFont.render(titleList3[i] , 1, BLACK)
        textwidth, textheight = ruleFont.size(titleList3[i])
        if rectList3[i] == Rect(width//4*2+210,160,120,30):
            useW = (120 - textwidth)//2  #use for centering
            useH = (30 - textheight)//2 
            textRect = Rect(width//4*2+210 + useW, 160 + useH,textwidth//2,textheight)        
        elif rectList3[i] == Rect(width//4*2+210,190,120,30):
            useW = (120 - textwidth)//2  #use for centering
            useH = (30 - textheight)//2   
            textRect = Rect(width//4*2+210 + useW, 190 + useH,textwidth//2,textheight)
        elif rectList3[i] == Rect(width//4*2+210,220,120,30):
            useW = (120 - textwidth)//2  #use for centering
            useH = (30 - textheight)//2   
            textRect = Rect(width//4*2+210, 220 + useH,textwidth//2,textheight)        
        screen.blit(text,textRect)   
        
    # crates
    screen.blit(health,Rect(80,350,50,50))
    screen.blit(SD,Rect(80,410,50,50))
    screen.blit(moreBullet,Rect(500,350,50,50))
    screen.blit(nuclearC,Rect(500,410,50,50))
    
    titleList3 = ["EXTRA STAMINA", "SHIP MOVE FASTER"]
    rectList3 = [Rect(80,350,50,50),
                 Rect(80,410,50,50)]    
    
    for i in range (len(rectList3)):
        rect = rectList3[i]
        text = ruleFont.render(titleList3[i] , 1, BLACK)
        textwidth, textheight = ruleFont.size(titleList3[i])
        if rectList3[i] == Rect(80,350,50,50):
            useW = (50 - textwidth)//2  #use for centering
            useH = (50 - textheight)//2 
            textRect = Rect(280 + useW, 350 + useH,textwidth//2,textheight)        
        elif rectList3[i] == Rect(80,410,50,50):
            useW = (50 - textwidth)//2  #use for centering
            useH = (50 - textheight)//2   
            textRect = Rect(280 + useW, 410 + useH,textwidth//2,textheight) 
        screen.blit(text,textRect)       
    
    titleList3 = ["SHOT FASTER", "EXTRA NUCLEAR"]
    rectList3 = [Rect(500,350,50,50),
                 Rect(500,410,50,50)]    
        
    for i in range (len(rectList3)):
        rect = rectList3[i]
        text = ruleFont.render(titleList3[i] , 1, BLACK)
        textwidth, textheight = ruleFont.size(titleList3[i])
        if rectList3[i] == Rect(500,350,50,50):
            useW = (50 - textwidth)//2  #use for centering
            useH = (50 - textheight)//2 
            textRect = Rect(690 + useW, 350 + useH,textwidth//2,textheight)        
        elif rectList3[i] == Rect(500,410,50,50):
            useW = (50 - textwidth)//2  #use for centering
            useH = (50 - textheight)//2   
            textRect = Rect(690 + useW, 410 + useH,textwidth//2,textheight) 
        screen.blit(text,textRect)    
    
    
    screen.blit(space,Rect(80,480,0,0))
    draw.rect(screen,BLACK,(115,487,330,55),2)
    text = ruleFont.render("SPACE (NUCLEAR)", 1, BLACK)
    textwidth, textheight = ruleFont.size("SPACE (NUCLEAR)") # get the font size
    useW = (330 - textwidth)//2  #use for centering
    useH = (55 - textheight)//2 
    textRect = Rect(115 + useW, 487 + useH,textwidth,textheight)
    screen.blit(text,textRect)   
    
    text = ruleFont.render("SPACESHIP MOVEMENT", 1, BLACK)
    textwidth, textheight = ruleFont.size("SPACESHIP MOVEMENT") # get the font size
    useW = (330 - textwidth)//2  #use for centering
    useH = (55 - textheight)//2 
    textRect = Rect(120 + useW, 80 + useH,textwidth,textheight)
    screen.blit(text,textRect)    
    
    text = ruleFont.render("STAMINA NUCLEAR SCORE", 1, BLACK)
    textwidth, textheight = ruleFont.size("STAMINA NUCLEAR SCORE") # get the font size
    useW = (330 - textwidth)//2  #use for centering
    useH = (55 - textheight)//2 
    textRect = Rect(554 + useW, 80 + useH,textwidth,textheight)
    screen.blit(text,textRect)
    
    return state    

def drawRule2 (screen,button,mx,my,state):
    screen.blit(ruleBackground, Rect(0, 0, width, height))
    blockwidth = width//8
    blockheight = width//8     
    screen.blit(ruleBackground, Rect(0,0, width, height))
    rect = Rect(blockwidth//2,blockheight//2,blockwidth*4.9+blockwidth*2.1,height-blockheight*1.5)
    draw.rect(screen,lightBLUE,rect)    
    rect = Rect(blockwidth//2,blockheight//2,blockwidth*4.9+blockwidth*2.1,height-blockheight*1.5)
    draw.rect(screen,BLACK,rect,3)   
    rect = Rect(blockwidth//2, blockheight*4.8, blockwidth*2.2, blockheight//1.75)
    rect = Rect(width//2+blockwidth*1.3, blockheight*4.8, blockwidth*2.2, blockheight//1.75)
    rectList3 = [Rect(blockwidth//2, blockheight*4.8, blockwidth*2.2, blockheight//1.75),
                 Rect(width//2+blockwidth*1.3, blockheight*4.8, blockwidth*2.2, blockheight//1.75)]    
    stateList3 = [RULE_STATE,GAME_STATE]
    titleList3 = ["BACK","LET'S GO"]

    for i in range (len(rectList3)):
        rect = rectList3[i]
        draw.rect(screen,lightBLUE,rect)
        draw.rect(screen,BLACK,rect,3)
        text = myFont.render(titleList3[i] , 1, BLACK)
        textwidth, textheight = myFont.size(titleList3[i])
        if rectList3[i] == Rect(blockwidth//2, blockheight*4.8, blockwidth*2.2, blockheight//1.75):
            useW = (blockwidth*2.2 - textwidth)//2  #use for centering
            useH = (blockheight//1.75 - textheight)//2 
            textRect = Rect(blockwidth//2 + useW, blockheight*4.8 + useH,textwidth//2,textheight)        
        elif rectList3[i] == (width//2+blockwidth*1.3, blockheight*4.8, blockwidth*2.2, blockheight//1.75):
            useW = (blockwidth*2.2 - textwidth)//2  #use for centering
            useH = (blockheight//1.75 - textheight)//2   
            textRect = Rect(width//2+blockwidth*1.3 + useW, blockheight*4.8 + useH,textwidth//2,textheight)
        screen.blit(text,textRect)             
        if rect.collidepoint(mx,my):
            draw.rect(screen,BLACK,rect,5)
            if button == 1:
                state = stateList3[i]   
    screen.blit(page2,(125//2,125//2,0,0))

    
        
    return state
def drawStory(screen,button,mx,my,state):
    blockwidth = width//8
    blockheight = width//8     
    screen.blit(ruleBackground, Rect(0,0, width, height))
    rect = Rect(blockwidth//2,blockheight//2,blockwidth*4.9+blockwidth*2.1,height-blockheight*1.5)
    draw.rect(screen,lightBLUE,rect)    
    rect = Rect(blockwidth//2,blockheight//2,blockwidth*4.9+blockwidth*2.1,height-blockheight*1.5)
    draw.rect(screen,BLACK,rect,3)   
    rect = Rect(blockwidth//2, blockheight*4.8, blockwidth*2.2, blockheight//1.75)
    rect = Rect(width//2+blockwidth*1.3, blockheight*4.8, blockwidth*2.2, blockheight//1.75)
    rectList3 = [Rect(blockwidth//2, blockheight*4.8, blockwidth*2.2, blockheight//1.75),
                 Rect(width//2+blockwidth*1.3, blockheight*4.8, blockwidth*2.2, blockheight//1.75)]    
    stateList3 = [MENU_STATE,GAME_STATE]
    titleList3 = ["MENU","LET'S GO"]
    
    
    for i in range (len(rectList3)):
        rect = rectList3[i]
        draw.rect(screen,lightBLUE,rect)
        draw.rect(screen,BLACK,rect,3)
        text = myFont.render(titleList3[i] , 1, BLACK)
        textwidth, textheight = myFont.size(titleList3[i])
        if rectList3[i] == Rect(blockwidth//2, blockheight*4.8, blockwidth*2.2, blockheight//1.75):
            useW = (blockwidth*2.2 - textwidth)//2  #use for centering
            useH = (blockheight//1.75 - textheight)//2 
            textRect = Rect(blockwidth//2 + useW, blockheight*4.8 + useH,textwidth//2,textheight)        
        
        elif rectList3[i] == (width//2+blockwidth*1.3, blockheight*4.8, blockwidth*2.2, blockheight//1.75):
            useW = (blockwidth*2.2 - textwidth)//2  #use for centering
            useH = (blockheight//1.75 - textheight)//2   
            textRect = Rect(width//2+blockwidth*1.3 + useW, blockheight*4.8 + useH,textwidth//2,textheight)
        screen.blit(text,textRect)             
        if rect.collidepoint(mx,my):
            draw.rect(screen,BLACK,rect,5)
            if button == 1:
                state = stateList3[i]   
    screen.blit(storyP,(125//2+1,125//2+1,0,0))

    return state        

def drawResult(screen,button,mx,my,state,shipC):
    global stamina, score, dt1, dt2, dt3, dt4, dt5, dt6, dt7, mt1, mt2, mt3, mt4, shipX, shipY, missileListY, missileListX 
    """mixer.Sound.stop(gameSound)
    mixer.Sound.play(menuSound,-1)""" 
    
    screen.blit(resultBackground,Rect(0,0,width,height))
    blockwidth = width//8
    blockheight = width//8    
    
    rect = Rect(blockwidth//2,blockheight//2,blockwidth*4.9+blockwidth*2.1,height-blockheight*1.6)
    draw.rect(screen,lightBLUE,rect)
    
    rect = Rect(blockwidth//2,blockheight//2,blockwidth*4.9+blockwidth*2.1,height-blockheight*1.6)
    draw.rect(screen,BLACK,rect,3)
    
    rectList2 = [Rect(blockwidth//2, blockheight*4.6, blockwidth*2.2, blockheight//1.75),
                 Rect(width//2+blockwidth*1.3, blockheight*4.6, blockwidth*2.2, blockheight//1.75)]
    stateList2 = [MENU_STATE,QUIT_STATE]    
    titleList2 = ["MENU","QUIT"]
    
    for i in range(len(rectList2)):
        rect = rectList2[i]
        draw.rect(screen,lightBLUE,rect)
        draw.rect(screen,BLACK,rect,3)
        text = myFont.render(titleList2[i] , 1, BLACK)
        textwidth, textheight = myFont.size(titleList2[i])
        if rectList2[i] == Rect(blockwidth//2, blockheight*4.6, blockwidth*2.2, blockheight//1.75):
            useW = (blockwidth*2.2 - textwidth)//2  #use for centering
            useH = (blockheight//1.75 - textheight)//2 
            textRect = Rect(blockwidth//2 + useW, blockheight*4.6 + useH,textwidth//2,textheight)        
        
        elif rectList2[i] == Rect(width//2+blockwidth*1.3, blockheight*4.6, blockwidth*2.2, blockheight//1.75):
            useW = (blockwidth*2.2 - textwidth)//2  #use for centering
            useH = (blockheight//1.75 - textheight)//2   
            textRect = Rect(width//2+blockwidth*1.3 + useW, blockheight*4.6 + useH,textwidth//2,textheight)
        screen.blit(text,textRect)
        
        if shipC == spaceship:
            shipC = spaceship3
            screen.blit(shipC,Rect(blockwidth//2*11.5,blockheight//2*1.5,0,0))
        if shipC == yellowship:
            shipC = yellowship2
            screen.blit(shipC,Rect(blockwidth//2*11.5,blockheight//2*1.5,0,0))

            
        if rect.collidepoint(mx,my):
            draw.rect(screen,BLACK,rect,5)
            if button == 1:
                state = stateList2[i]        
                if state == MENU_STATE:
                    score = 0
                    GAME_STATE = 1
                    stamina = 3
                    dt1 = [randint(0,500),-300]
                    dt2 = [randint(500,width-74),-400]
                    dt3 = [randint(0,500),-500] # the first time
                    dt4 = [randint(500,width-74*2),-600] # the first time
                    dt5 = [randint(0,500),-700] # the first time
                    dt6 = [randint(500,width-74),-800] # the first time
                    dt7 = [randint(0,500),-900] # the first time 
                    mt1 = [randint(0,500),-1000]
                    mt2 = [1800,-800]
                    mt3 = [-400,-400]
                    mt4 = [randint(500, width-74),-2000]
                    shipX = 475
                    shipY = 600                    
                    missileListY = [624]
                    missileListX = [499]
    
    screen.blit(salute,Rect(65,383,0,0))
    
    text = myFont.render("CONGRATULATIONS!!", 1, WHITE)
    textwidth, textheight = myFont.size("CONGRATULATIONS!!") # get the font size
    useW = (blockwidth*4.5 - textwidth)//2  #use for centering
    useH = (blockheight//1.5 - textheight)//2 
    textRect = Rect(blockwidth//4 + useW+70, blockheight//2 + useH,textwidth,textheight)
    screen.blit(text,textRect)    
    
    text = ruleFont.render("This is the pieces of debris you", 1, WHITE)
    textwidth, textheight = ruleFont.size("This is the pieces of debris you") # get the font size
    useW = (blockwidth*4.5 - textwidth)//2  #use for centering
    useH = (blockheight//1.5 - textheight)//2 
    textRect = Rect(blockwidth//4 + useW+70, blockheight//2 + useH + 50,textwidth,textheight)
    screen.blit(text,textRect)
    
    text = ruleFont.render("cleared:", 1, WHITE)
    textwidth, textheight = ruleFont.size("cleared:") # get the font size
    useW = (blockwidth*4.5 - textwidth)//2  #use for centering
    useH = (blockheight//1.5 - textheight)//2 
    textRect = Rect(blockwidth//4 + useW+70, blockheight//2 + useH + 100,textwidth,textheight)
    screen.blit(text,textRect)  
    
    text = myFont.render(str(score)+"  "+"pieces", 1, BLACK)
    textwidth, textheight = myFont.size(str(score)+"  "+"pieces") # get the font size
    useW = (blockwidth*4.5 - textwidth)//2  #use for centering
    useH = (blockheight//1.5 - textheight)//2 
    textRect = Rect(blockwidth//4 + useW+70, blockheight//2 + useH + 150,textwidth,textheight)
    screen.blit(text,textRect)    
    
    text = storyFont.render("You have been cleared:", 1, WHITE)
    textwidth, textheight = storyFont.size("You have been cleared:") # get the font size
    useW = (blockwidth*4.5 - textwidth)//2  #use for centering
    useH = (blockheight//1.5 - textheight)//2 
    textRect = Rect(blockwidth//4 + useW+200, blockheight//2 + useH + 250,textwidth,textheight)
    screen.blit(text,textRect)
    
    percent = score/128000*100
    percent2 = ("%.2f" %percent)
    text = myFont.render(percent2+"%", 1, BLACK)
    textwidth, textheight = myFont.size(percent2 + "%") # get the font size
    useW = (blockwidth*4.5 - textwidth)//2  #use for centering
    useH = (blockheight//1.5 - textheight)//2 
    textRect = Rect(blockwidth//4 + useW+200, blockheight//2 + useH + 300,textwidth,textheight)
    screen.blit(text,textRect)    
    
    text = storyFont.render("of total debris.", 1, WHITE)
    textwidth, textheight = storyFont.size("of total debris.") # get the font size
    useW = (blockwidth*4.5 - textwidth)//2  #use for centering
    useH = (blockheight//1.5 - textheight)//2 
    textRect = Rect(blockwidth//4 + useW+200, blockheight//2 + useH + 350,textwidth,textheight)
    screen.blit(text,textRect)    
    return state, stamina, score, dt1, dt2, dt3, dt4, dt5, dt6, dt7, mt1, mt2, mt3, mt4, shipX, shipY, missileListY, missileListX  
    
# debris movement after shot
def initTarget():
    dt1 = []
    dt1.append(randint(0,width-74))
    dt1.append(-100)
    return dt1
 
def initTarget2():
    dt2 = []
    dt2.append(randint(0,width-74))
    dt2.append(-100)
    return dt2   

def initTarget3():
    dt3 = []
    dt3.append(randint(0,width-74))
    dt3.append(-100)
    return dt3

def initTarget4():
    dt4 = []
    dt4.append(randint(0,width-74))
    dt4.append(-1000)
    return dt4

def initTarget5():
    dt5 = []
    dt5.append(randint(0,width-74))
    dt5.append(-100)
    return dt5

def initTarget6():
    dt6 = []
    dt6.append(randint(0,width-74))
    dt6.append(-100)
    return dt6 

def initTarget7():
    dt7 = []
    dt7.append(randint(0,width-74))
    dt7.append(-1000)
    return dt7

# mete movement
def initMete1():
    mt1 = []
    mt1.append(randint(0,width-74))
    mt1.append(-10000)
    return mt1

def initMete2():
    mt2 = []
    mt2.append(2000)
    mt2.append(randint(-1000, -200))
    return mt2

def initMete3():
    mt3 = []
    mt3.append(-1000)
    mt3.append(randint(-1000, -200))
    return mt3

def initMete4():
    mt4 = []
    mt4.append(randint(0,width-74))
    mt4.append(-8000)
    return mt4    

# crate movement
def initcrate1():
    ct1 = []
    ct1.append(randint(0,width - 50))
    ct1.append(-5000)
    return ct1

def initcrate2():
    ct2 = []
    ct2.append(randint(0,width - 50))
    ct2.append(-6000)
    return ct2

def initcrate3():
    ct3 = []
    ct3.append(randint(0,width - 50))
    ct3.append(-7000)
    return ct3

def initcrate4():
    ct4 = []
    ct4.append(randint(0,width - 50))
    ct4.append(-8000)
    return ct4



running = True
myClock = time.Clock()

state = MENU_STATE
mx = my = 0
backx = 0 # scrolling background
score = 0 
bulletC = blueBullet
shipC = spaceship


shipX = 475
shipY = 600

shotTimer = time.get_ticks()

missileListY = [624]
missileListX = [499]

moveRate = 6 # speed of spaceship at first
stamina = 3 # number of stamina in the first 
nuclear = 2 # number of missiles
BS = 100 # speed of missiles

# debris first time
dt1 = initTarget() # Since the first collision
dt1 = [randint(0,500),-100] # the first time
d1outTime = time.get_ticks()
d1s = 40

dt2 = initTarget2() # Since the first collision
dt2 = [randint(500,width-74),-200] # the first time
d2outTime = time.get_ticks()
d2s = 40 

dt3 = initTarget3() # Since the first collision
dt3 = [randint(0,500),-300] # the first time
d3outTime = time.get_ticks()
d3s = 60 

dt4 = initTarget4() # Since the first collision
dt4 = [randint(500,width-74*2),-400] # the first time
d4outTime = time.get_ticks()
d4s = 70 

dt5 = initTarget5() # Since the first collision
dt5 = [randint(0,500),-500] # the first time
d5outTime = time.get_ticks()
d5s = 70

dt6 = initTarget6() # Since the first collision
dt6 = [randint(500,width-74),-600] # the first time
d6outTime = time.get_ticks()
d6s = 60

dt7 = initTarget7() # Since the first collision
dt7 = [randint(0,500),-700] # the first time
d7outTime = time.get_ticks()
d7s = 40

# mete
mt1 = initMete1()
mt1 = [randint(0,500),-1000]
m1outTime = time.get_ticks()

mt2 = initMete2()
mt2 = [2800,-1800]
m2outTime = time.get_ticks()

mt3 = initMete2()
mt3 = [-1000,-1000]
m3outTime = time.get_ticks()

mt4 = initMete1()
mt4 = [randint(500, width-74),-2000]
m4outTime = time.get_ticks()

# crates
ct1 = initcrate1()
ct1 = [randint(0,500),-1000]
c1outTime = time.get_ticks()

ct2 = initcrate2()
ct2 = [randint(500,width-50),-2000]
c2outTime = time.get_ticks()
c2getTime = time.get_ticks()

ct3 = initcrate3()
ct3 = [randint(0,500),-3000]
c3outTime = time.get_ticks()
c3getTime = time.get_ticks()

ct4 = initcrate4()
ct4 = [randint(500,width-50),-4000]
c4outTime = time.get_ticks()

# Game Loop
while running:
    button = 0
    for e in event.get():             # checks all events that happen
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos          
            button = e.button
        elif e.type == MOUSEMOTION:
            mx, my = e.pos
        elif e.type == KEYDOWN:
            
            if e.key == K_RIGHT:
                PRESS_RIGHT = True
            if e.key == K_LEFT:
                PRESS_LEFT = True 
            if e.key == K_UP:
                PRESS_UP = True
            if e.key == K_DOWN:
                PRESS_DOWN = True
            keys = key.get_pressed()
            if state == GAME_STATE:
                if nuclear > 0:
                    if keys[K_SPACE]:
                        """mixer.Sound.stop(gameSound)"""
                        dt1 = [randint(0,500),-300]
                        dt2 = [randint(500,width-74),-400]
                        dt3 = [randint(0,500),-500] # the first time
                        dt4 = [randint(500,width-74*2),-600] # the first time
                        dt5 = [randint(0,500),-700] # the first time
                        dt6 = [randint(500,width-74),-800] # the first time
                        dt7 = [randint(0,500),-900] # the first time 
                        mt1 = [randint(0,500),-1000]
                        mt2 = [1800,-800]
                        mt3 = [-400,-400]
                        mt4 = [randint(500, width-74),-2000]
                        nuclear -= 1
                  
        elif e.type == KEYUP:
            if e.key == K_RIGHT:
                PRESS_RIGHT = False
            if e.key == K_LEFT:
                PRESS_LEFT = False 
            if e.key == K_UP:
                PRESS_UP = False
            if e.key == K_DOWN:
                PRESS_DOWN = False 

                
    if state == MENU_STATE:
        state = drawMenu(screen, button, mx, my, state)
    elif state == CHOSE_STATE:
        state,bulletC,shipC = chosePage(screen,button,mx,my,state)
    elif state == GAME_STATE:
        state = drawGame(screen, button, mx, my, state,shipX,shipY,bulletC,shipC)
        #scrolling background
        backx += 1
        if backx > height:
            backx = 0 
    elif state == RULE_STATE:
        state = drawRule(screen, button, mx, my, state)
    elif state == RULE2_STATE:
        state = drawRule2(screen, button, mx, my, state)      
    elif state == STORY_STATE:
        state = drawStory(screen, button, mx, my, state)
    elif state == RESULT_STATE:
        state, stamina, score, dt1, dt2, dt3, dt4, dt5, dt6, dt7, mt1, mt2, mt3, mt4, shipX, shipY, missileListY, missileListX = drawResult(screen,button,mx,my,state,shipC)
    else:
        running = False
    display.flip()
    myClock.tick(60)                     # waits long enough to have 60 fps
    
    # for ship movement
    if PRESS_RIGHT == True:
        shipX += moveRate
        if shipX >= width-74:
            shipX = width-74
    if PRESS_LEFT == True:
        shipX -= moveRate
        if shipX <= 0:
            shipX = 0
    if PRESS_UP == True:
        shipY -= moveRate
        if shipY <= 65:
            shipY = 65
    if PRESS_DOWN == True:
        shipY += moveRate # waits long enough to have 60 fps
        if shipY >= height-78:
            shipY = height-78
quit()



