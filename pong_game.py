import pygame, sys, random
import os

PATH = os.getcwd()

# setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

#  Game Variable
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
computer_speed = 7

# Scoer system

player_score = 0
computer_score = 0
game_font = pygame.font.Font('Aller_Bd.ttf', 32)

# Sound effect

pygame.mixer.music.load(os.path.join(PATH, 'background-music.mp3'))
pygame.mixer.music.play(-1) # -1 คือ loop

plop_sound = pygame.mixer.Sound("powerup.wav")

plang_sound = pygame.mixer.Sound('laser.wav')

def ball_anim():
	global ball_speed_x, ball_speed_y, player_score, computer_score

	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		

		ball_speed_y *= -1

	# Player score

	if ball.left <= 0:
		pygame.mixer.Sound.play(plop_sound)
		player_score += 1	
		ball_restart()

	if ball.right >= screen_width:
		computer_score += 1
		pygame.mixer.Sound.play(plop_sound)
		ball_restart()



	if ball.colliderect(player) or ball.colliderect(computer):
		pygame.mixer.Sound.play(plang_sound)
		ball_speed_x *= -1	


def player_anim():
	player.y += player_speed


	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def computer_logic():
	if computer.top < ball.y:
		computer.y += computer_speed
	if computer.bottom > ball.y:
		computer.y -= computer_speed
		
	if computer.top <= 0:
		computer.top = 0
	if computer.bottom >= screen_height:
		computer.bottom = screen_height

def ball_restart():
	global ball_speed_x, ball_speed_y
	ball.center = (screen_width /2, screen_height /2)
	ball_speed_y *= random.choice((1, -1))
	ball_speed_x *= random.choice((1, -1))




# Screen Surface 

screen_width = 1024
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("pong game by woravit")

white = 'white'
red = 'brown1'
bg_color = 'cadetblue2'
bg = os.path.join(PATH,'bg1.png')

background = pygame.image.load(bg).convert_alpha() 
background_rect = background.get_rect()
# Game Rectangles

player = pygame.Rect(screen_width - 30, screen_height /2 - 70 , 10,140)
computer = pygame.Rect(30, screen_height /2 -70, 10,140)
ball = pygame.Rect(screen_width /2- 12.5, screen_height /2- 12.5 , 25,25)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed -= 5
			if event.key == pygame.K_DOWN:  
				player_speed += 5

		if  event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed += 5
			if event.key == pygame.K_DOWN:
				player_speed -= 5

	# game loop
	ball_anim()
	player_anim()
	computer_logic()

	screen.fill(bg_color)
	pygame.draw.rect(screen, white, player)
	pygame.draw.rect(screen, red, computer)
	pygame.draw.ellipse(screen, red, ball)
	pygame.draw.aaline(screen , white, (screen_width/2, 0), (screen_width/2, screen_height))

	player_text = game_font.render(f'{player_score}',True, white)
	screen.blit(player_text, (480, 300))

	computer_text = game_font.render(f'{computer_score}',True, white)
	screen.blit(computer_text, ((525, 300)))


	pygame.display.update()
	clock.tick(60)
















	

	