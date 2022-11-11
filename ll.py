import pygame, sys

class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#000000'
		#text
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					print('click')
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'

pygame.init()
width = 700
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Connect4 Game')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,30)
font = pygame.font.SysFont('arial',75)


#define font color
fontColor=(255,255,255)

def draw_text(text,font, color,x,y):
    show = font.render(text,True,color)
    screen.blit(show,(x,y))

def draw_menu():
	draw_text("Connect4 Game", font, fontColor, 80, 100)
	#button1 = Button('PLAY WITHOUT PRUNING', 260, 130, (220, 480), 10)
	#button2 = Button('PLAY WITH PRUNING', 260, 130, (220, 280), 10)
	button1.draw()
	button2.draw()
	#if check_click(self) == True:
	#	menu = True
	#else:
	#	menu = False
	#return menu

pygame.display.update()
def draw_game():
	button3.draw()
pygame.display.update()

button1 = Button('PLAY WITHOUT PRUNING',260,130,(220,480),5)
button2 = Button('PLAY WITH PRUNING',260,130,(220,280),5)
button3 = Button('HEY!',260,130,(220,280),5)

main_menu=True
run= True
while run:
	screen.fill((52, 78, 91))
	#draw_text("Connect4 Game", font, fontColor, 80, 100)
	for event in pygame.event.get():
		#draw_text("Connect4 Game", font, fontColor, 160, 160)
		if main_menu:
			draw_menu()
			pygame.display.update()
		else:
			draw_game()
			pygame.display.update()
		#pygame.display.update()
		if event.type == pygame.QUIT:
			#pygame.quit()
			#sys.exit()
			run=False


	#button1.draw()
	#button2.draw()
	#pygame.display.update()
	clock.tick(60)
pygame.quit()
sys.exit()
