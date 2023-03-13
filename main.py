import pygame
import random

# เริ่มต้น โปรเจค
pygame.init()

 # เฟรมเรท
fps = 30

# ความกว้าง สูงของเกมส์
WIDTH = 800
HEIGHT =700 

# สร้างสี RGB
BLACK = (0, 0, 0)
GREEN = (0, 255,0)
# สร้าง สกรีน   
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# ชื่อ
pygame.display.set_caption('My First Game By Woravit')

# สร้างนาฬิกาของเกมส์ จัดการเวลา
clock = pygame.time.Clock()


# สร้าง ตัว enemy

class Enemy(pygame.sprite.Sprite):

	def __init__(self):
		#ฟังชั่นหลัก จะรันทุกครั้ง
		pygame.sprite.Sprite.__init__(self)   
		
		img = '/Users/woravittosomrit/Desktop/python2D/firstgame/aircraft.png'
		self.image = pygame.image.load(img).convert_alpha()

		
		# code ข้างล่างนี้ก็ทำงานได้
		#self.ship = pygame.image.load("/Users/woravittosomrit/Desktop/python2D/firstgame/aircraft.png").convert_alpha()


		# self.image = pygame.Surface((50,50))
		# self.image.fill(GREEN)

		# สร้างสี่เหลี่ยม
		self.rect = self.image.get_rect()

		# สุมตำแหน่ง แนวแกน x
		rand_x = random.randint(self.rect.width, WIDTH - self.rect.width)

		# ตำแหน่งจากจุดศูนย์กลางตัวละคร
		self.rect.center = (rand_x, 0)

		# เพิ่มความเร็วแนวแกน y 

		self.speed_y = random.randint(1, 5)

		# อัพเดท
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
		#ฟังชั่นหลัก จะรันทุกครั้ง
		pygame.sprite.Sprite.__init__(self)   
		
		img = '/Users/woravittosomrit/Desktop/python2D/firstgame/bomber.png'
		self.image = pygame.image.load(img).convert_alpha()

		
		# code ข้างล่างนี้ก็ทำงานได้
		#self.ship = pygame.image.load("/Users/woravittosomrit/Desktop/python2D/firstgame/aircraft.png").convert_alpha()


		# self.image = pygame.Surface((50,50))
		# self.image.fill(GREEN)

		# สร้างสี่เหลี่ยม
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT - self.rect.height)

		#speed x

		self.speed_x = 0


		# อัพเดท
	def update(self):
		#self.rect.y += 5
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5

		self.rect.x += self.speed_x


		if self.rect.bottom > HEIGHT:
			self.rect.y = 0

	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet)


class Bullet(pygame.sprite.Sprite):

	def __init__(self,x ,y):
		# x = center ของเครื่องบิน
		# y = top ของเครื่องบิน

		#ฟังชั่นหลัก จะรันทุกครั้ง
		pygame.sprite.Sprite.__init__(self)   
		
		# img = '/Users/woravittosomrit/Desktop/python2D/firstgame/bomber.png'
		# self.image = pygame.image.load(img).convert_alpha()

		self.image = pygame.Surface((10,10))
		self.image.fill(GREEN)

		# สร้างสี่เหลี่ยม
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom = y

		#speed แนวของกระสุนที่ยิงออกไป

		self.speed_y = -10

	def update(self):
		self.rect.y += self.speed_y
 
		# ลบกระสุนเมื่อแกน y < 0

		if self.rect.y < 0:
			self.kill()





#สร้างกลุ่ม Sprite
all_sprites = pygame.sprite.Group() # กล่องเก็บตัวละคร

#player
player = Player()# สร้างตัวละคร
all_sprites.add(player)  # เพิ่มตัวละครเข้าไปในกลุ่ม
		
#enemy
for i in range(5): # เพิ่มจำนวนตัวละคร
	enemy = Enemy()
	all_sprites.add(enemy)


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

	# สีแบคกราวของเกมส์

	screen.fill(BLACK)

	# นำตัวละครมาวาดใส่เกมส์
	all_sprites.draw(screen)



	# ให้ pygame แสดงผล
	pygame.display.flip()

# ออกจากเกมส์
pygame.quit()
