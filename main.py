import pygame
import random
import os

PATH = os.getcwd()


# เริ่มต้น โปรเจค
pygame.init()
pygame.mixer.init()

######### Sound Effect ###########

# background music
pygame.mixer.music.load(os.path.join(PATH, 'bg2.mp3'))
pygame.mixer.music.play(-1) # -1 คือ loop

# collide sound
explosion = pygame.mixer.Sound(os.path.join(PATH, 'explosion.wav'))
laser = pygame.mixer.Sound(os.path.join(PATH, 'laser.wav'))
powerup = pygame.mixer.Sound(os.path.join(PATH, 'powerup.wav'))
bom = pygame.mixer.Sound(os.path.join(PATH, 'bom.wav'))
gameover = pygame.mixer.Sound(os.path.join(PATH, 'gameover.wav'))
sound_state = True


 # เฟรมเรท
fps = 30

# ความกว้าง สูงของเกมส์
WIDTH = 800
HEIGHT =700 

# สร้างสี RGB
BLACK = (0, 0, 0)
GREEN = (0, 255,0)
WHITE = (255,255,255)
RED = (247, 12, 24)
# คะแนนเมื่อยิงโดน

SCORE = 0
#ชีวิต

LIVES = 3
LIVES_TIME =pygame.time.get_ticks()
GAMEOVER = False
GAMEOVER_FONT = True
GAMEOVER_TIME = pygame.time.get_ticks()

# สร้าง สกรีน หรือกล่องใส่เกมส์  
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# สร้างชื่อ
pygame.display.set_caption('My First Game By Woravit')

# สร้างแบคกราวด์

bg = os.path.join(PATH,'bg1.png')

background = pygame.image.load(bg).convert_alpha() 
background_rect = background.get_rect()

# สร้างนาฬิกาของเกมส์ จัดการเวลา
clock = pygame.time.Clock()

# สร้าง ตัว enemy

class Enemy(pygame.sprite.Sprite):

	def __init__(self):
		#ฟังชั่นหลัก จะรันทุกครั้งที่มีการเรียกใช้
		pygame.sprite.Sprite.__init__(self)   
		
		img = os.path.join(PATH,'ufo1.png')

		# ถ้ามี โฟลเดอร์ image อีกชั้นต้องเขียนแบบนี้
		# img = os.path.join(PATH,'image').join(PATH,'aircraft.png')
		self.image = pygame.image.load(img).convert_alpha()

		# self.image = pygame.Surface((50,50))
		# self.image.fill(GREEN)

		# สร้างสี่เหลี่ยม
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image, (50, 50))
		# สุมตำแหน่ง แนวแกน x
		rand_x = random.randint(self.rect.width, WIDTH - self.rect.width)
		#rand_y = random.randint(self.rect.height, HEIGHT - self.rect.height)
		# ตำแหน่งจากจุดศูนย์กลางตัวละคร
		self.rect.center = (rand_x, 0)

		# เพิ่มความเร็วแนวแกน y 

		self.speed_y = random.randint(1, 5)

# 		# อัพเดท
	def update(self):
		self.rect.y += self.speed_y
		if self.rect.bottom > HEIGHT:
			self.rect.y = 0
			# สุมตำแหน่ง แนวแกน x อีกครั้ง
			rand_x = random.randint(self.rect.width, WIDTH - self.rect.width)
			self.rect.x = rand_x
			self.speed_y = random.randint(1, 5)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)  	
		img = os.path.join(PATH,'bomber.png')
		self.image = pygame.image.load(img).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT - self.rect.height)
		self.speed_x = 0
		self.speed_y = 0
	def update(self):
		#self.rect.y += 5
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if  GAMEOVER != True:
			if keystate[pygame.K_LEFT] and self.rect.x > 0:
				self.speed_x = -5
			if keystate[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
				self.speed_x = 5
			if keystate[pygame.K_UP] and self.rect.y > 0:
				self.speed_y = -5
			if keystate[pygame.K_DOWN] and self.rect.y < HEIGHT - self.rect.height:
				self.speed_y = 5
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		self.image = pygame.transform.scale(self.image, (40, 100))
		if self.rect.bottom > HEIGHT:
			self.rect.y = 0

	def shoot(self):
		if  GAMEOVER != True:
			pygame.mixer.Sound.play(laser)
			bullet = Bullet(self.rect.centerx, self.rect.top)
			all_sprites.add(bullet)
			group_bullet.add(bullet)

class Bullet(pygame.sprite.Sprite):

	def __init__(self,x ,y):
		# x = center ของเครื่องบิน
		# y = top ของเครื่องบิน

		#ฟังชั่นหลัก จะรันทุกครั้ง
		pygame.sprite.Sprite.__init__(self)   
		
		# img = '/Users/woravittosomrit/Desktop/python2D/firstgame/bomber.png'
		# self.image = pygame.image.load(img).convert_alpha()

		self.image = pygame.Surface((10,10))
		self.image.fill(RED)

		# สร้างสี่เหลี่ยม
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom = y

		#speed x แนวของกระสุนที่ยิงออกไป

		self.speed_y = -10

	def update(self):
		self.rect.y += self.speed_y
 
		# ลบกระสุนเมื่อแกน y < 0

		if self.rect.y < 0:
			self.kill()
# กระเป๋าพยาบาล

class Medicpack(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)   
		img = os.path.join(PATH,'medical.png')
		# main clock
		self.last = pygame.time.get_ticks()
		self.wait = 20000 # milisecon / 20 second
		self.run = False

		self.image = pygame.image.load(img).convert_alpha()
		self.rect = self.image.get_rect()	
		rand_x = random.randint(self.rect.width, WIDTH - self.rect.width)
		self.rect.center = (rand_x, -100)
		self.speed_y = random.randint(1, 10)


	def update(self):
		now = pygame.time.get_ticks()

		if self.run == True:
			self.rect.y += self.speed_y
		
		if self.rect.bottom > HEIGHT:
			# เมื่อกระเป๋าพยาบาลลงมาถึงขอบจอ
			self.run = False
			self.rect.y = -100
			
		if (now - self.last) >= self.wait:
			self.run = True
			self.last = now 
			rand_x = random.randint(self.rect.width, WIDTH - self.rect.width)
			self.rect.x = rand_x
			self.speed_y = random.randint(1, 10)



font_name = pygame.font.match_font('tahoma')

def draw_text(screen,text,size,x,y):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text,True,WHITE)
	text_rect = text_surface.get_rect()
	text_rect.topleft = (x,y)
	screen.blit(text_surface,text_rect)

# draw_text(screen, 'SCORE: 100', 30,WIDTH-100,10)


#สร้างกลุ่ม Sprite
all_sprites = pygame.sprite.Group() # กล่องเก็บตัวละคร
group_enemy = pygame.sprite.Group() # กล่องเก็บศัตรู
group_bullet = pygame.sprite.Group() # กล่องเก็บกระสุน
group_medicpack = pygame.sprite.Group()

#player
player = Player()# สร้างตัวละคร
all_sprites.add(player)  # เพิ่มตัวละครเข้าไปในกลุ่ม
		
#enemy
for i in range(5): # เพิ่มจำนวนตัวละคร
	enemy = Enemy()
	all_sprites.add(enemy)
	group_enemy.add(enemy)

# medicpack
medicpack = Medicpack()
all_sprites.add(medicpack)
group_medicpack.add(medicpack)


# สร้างสถานะของเกมส์ 
running = True 

# สร้างการวนลูป
while running:
	#สั่งเกมส์ ตามเฟรมเรท
	clock.tick(fps)

	# ตรวจสอบว่าปิดเกมส์หรือยัง
	#  หากกด กากบาท = สั่งให้ตัวแปร running = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()

	all_sprites.update()		

	# ตรวจการชนกันของ sprite ด้วยฟังชั่น collide

	collide = pygame.sprite.spritecollide(player, group_enemy, True)
	print (collide)
	# if collide:
	# 	LIVES -= 1


	if collide:
		pygame.mixer.Sound.play(explosion)
		enemy = Enemy()
		all_sprites.add(enemy)
		group_enemy.add(enemy)

		now_lives = pygame.time.get_ticks()
		if now_lives - LIVES_TIME >= 2000:
			LIVES -= 1
			LIVES_TIME = now_lives
		 
		if  LIVES == 0:
			GAMEOVER = True
			
		
		#running = False
	

   
	collidemedic = pygame.sprite.spritecollide(player, group_medicpack, True)
	if collidemedic:

		pygame.mixer.Sound.play(powerup)

		LIVES += 1
		medicpack = Medicpack()
		all_sprites.add(medicpack)
		group_medicpack.add(medicpack)

  	# bullet collission
	hits = pygame.sprite.groupcollide(group_bullet,group_enemy, True, True)
	# print('Bullet:', hits)
	for h in hits:
		pygame.mixer.Sound.play(bom)
		enemy = Enemy()
		all_sprites.add(enemy)
		group_enemy.add(enemy)    
		# add score
		SCORE += 10 # SCORE = SCORE + 1



	# สีแบคกราวของเกมส์

	screen.fill(BLACK)

	screen.blit(background,background_rect)

	draw_text(screen, 'SCORE: {}'.format(SCORE), 30, WIDTH-300,10)
	draw_text(screen, 'LIVES: {}'.format(LIVES), 20, 100,10)
	# เมื่อ Game over อยากใส่อะไรเข้าไป
	if GAMEOVER == True:
		pygame.mixer.Sound.play(gameover)
		now_gameover = pygame.time.get_ticks()
		if GAMEOVER_FONT == True:
			draw_text(screen, 'GAME OVER' , 100, 150, 300)
			if now_gameover - GAMEOVER_TIME >= 1000:
				GAMEOVER_FONT = False
				GAMEOVER_TIME = now_gameover
		else:
			draw_text(screen, 'GAME OVER', 50, 250, 300)
			if now_gameover - GAMEOVER_TIME >= 1000:
				GAMEOVER_FONT = True
				GAMEOVER_TIME = now_gameover
		# เครื่องบินหยุด
		for enemy in group_enemy:
			enemy.kill()
		for medicpack in group_medicpack:
			medicpack.kill()

	# นำตัวละครมาวาดใส่เกมส์
	all_sprites.draw(screen)

	# ให้ pygame แสดงผล
	pygame.display.flip()

# ออกจากเกมส์
pygame.quit()
