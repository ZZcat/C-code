import pygame,datetime,os,sys,select,string,socket
from datetime import date
from pygame.locals import *
pygame.init()


class Button:
   def __init__(self, text):
      self.text = text
      self.is_hover = False
      self.default_color = (100,100,100)
      self.hover_color = (255,255,255)
      self.font_color = (0,0,0)
      self.obj = None
      
   def label(self):
      '''button label font'''
      font = pygame.font.Font(None, 20)
      return font.render(self.text, 1, self.font_color)
      
   def color(self):
      '''change color when hovering'''
      if self.is_hover:
         return self.hover_color
      else:
         return self.default_color
         
   def draw(self, screen, mouse, rectcoord, labelcoord):
      '''create rect obj, draw, and change color based on input'''
      self.obj  = pygame.draw.rect(screen, self.color(), rectcoord)
      screen.blit(self.label(), labelcoord)
      
      #change color if mouse over button
      self.check_hover(mouse)
      
   def check_hover(self, mouse):
      '''adjust is_hover value based on mouse over button - to change hover color'''
      if self.obj.collidepoint(mouse):
         self.is_hover = True 
      else:
         self.is_hover = False
         
if __name__ == '__main__':
   # set up some colors
   BLACK = (0, 0, 0)
   WHITE = (255, 255, 255)
   RED = (255, 0, 0)
   GREEN = (0, 255, 0)
   BLUE = (0, 0, 255)

   # Set up screen and clock
   screen = pygame.display.set_mode((1000,700))
   clock = pygame.time.Clock()
   pygame.display.set_caption('Encrypted text sender')

   # Set up vars
   run = True
   DATE_clicked = 0
   TIME_clicked = 0
   OS_sys = "win"
   typing = False
   text = ""
   font = pygame.font.SysFont("comicsansms", 72)
   name = ""

   # Set up buttons
   DATE = Button('Date')
   TIME = Button('Time')
   OS = Button('WIN')
   TEXT = Button("Type here:")
   
   # connect to host
   host = "localhost"
   port = 5014
   
     
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.settimeout(2)
     
   # connect to remote host
   try :
      s.connect((host, port))
   except :
      print 'Unable to connect to remote host'
      sys.exit()
     
   print 'Connected to remote host. Start sending messages'

   while run:      
      mouse = pygame.mouse.get_pos()
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
            sys.quit()
            pygame.quit()
         elif typing == True and event.type == KEYDOWN:
            if event.unicode.isalpha():
                text += event.unicode
                TYPE_TEXT = font.render(text, True, (0, 128, 0))
            elif event.key == K_BACKSPACE:
                text = text[:-1]
                TYPE_TEXT = font.render(text, True, (0, 128, 0))
            elif event.key == K_RETURN:
                text = ""
                TYPE_TEXT = font.render(text, True, (0, 128, 0))
            elif event.key == pygame.K_1:
               text = text + str(1)
            elif event.key == pygame.K_2:
               text = text + str(2)
            elif event.key == pygame.K_3:
               text = text + str(3)
            elif event.key == pygame.K_4:
               text = text + str(4)
            elif event.key == pygame.K_5:
               text = text + str(5)
            elif event.key == pygame.K_6:
               text = text + str(6)
            elif event.key == pygame.K_7:
               text = text + str(7)
            elif event.key == pygame.K_8:
               text = text + str(8)
            elif event.key == pygame.K_9:
               text = text + str(9)
            elif event.key == (pygame.K_0):
               text = text + str(0)

              
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if not TEXT.obj.collidepoint(mouse):
               typing = False
            if DATE.obj.collidepoint(mouse):
################################################################################################
               if DATE_clicked == 0:
                  if OS_sys == "mac":
                     os.system("say Enabling date")
                     DATE_clicked = 1
                  else:
                     DATE_clicked = 1
               else:
                  if OS_sys == "mac":
                     os.system("say Disabling date")
                     DATE_clicked = 0
                  if OS_sys == "win":
                     DATE_clicked = 0
####################################################################################################
            elif TIME.obj.collidepoint(mouse):
                if TIME_clicked == 0:
                  if OS_sys == "mac":
                     os.system("say Enabling time")
                     TIME_clicked = 1
                  else:
                     TIME_clicked = 1
                else:
                   if OS_sys == "mac":
                     os.system("say Disabling time")
                     TIME_clicked = 0
                   if OS_sys == "win":
                      TIME_clicked = 0
####################################################################################################
            elif OS.obj.collidepoint(mouse):
                if OS_sys == "win":
                   OS_sys = "mac"
                   os.system("Turn on mac mode")
                   OS = Button('mac')
                elif OS_sys == "mac":
                   os.system("Turning off mac mode")
                   OS_sys = "win"
                   OS = Button('WIN')
####################################################################################################

####################################################################################################
            elif TEXT.obj.collidepoint(mouse):
               if typing == False:
                  typing = True
                  TYPE = Button("Typing")
               else:
                  typing = False
                  TYPE = Button("Type")


      for evt in pygame.event.get():
         if evt.type == KEYDOWN:
            if evt.unicode.isalpha():
               name += evt.unicode
            elif evt.key == K_BACKSPACE:
               name = text[:-1]
            elif evt.key == K_RETURN:
               conn.sendall(text)
               text = ""
      print text
      if DATE_clicked == 1:
          DATE = Button(str(date.today()))
      if TIME_clicked == 1:
         TIME = Button(str(datetime.datetime.now().time()))
      TEXT_text = ("Type here:"+str(text))
      
      TEXT = Button(TEXT_text)     
      
      TIME.draw(screen, mouse, (850,15,100,20), (875,18))
      DATE.draw(screen, mouse, (700,15,100,20), (724,18))
      OS.draw(screen, mouse, (100,160,100,20), (125,163))
      TEXT.draw(screen, mouse, (30, 650,660,20), (55,654))
      pygame.display.update()
      #clock.tick(100)
