import pygame

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

class Player(pygame.sprite.Sprite):

	def __init__(self):
		#ฟังชั่นหลัก จะรันทุกครั้ง
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("/Users/woravittosomrit/Desktop/python2D/firstgame/aircraft.png").convert_alpha()


		# self.image = pygame.Surface((50,50))
		# self.image.fill(GREEN)

		# สร้างสี่เหลี่ยม
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT/2)


# อัพเดท
	def update(self):
		self.rect.y += 5
		if self.rect.bottom > HEIGHT:
			self.rect.y = 0


#สร้างกลุ่ม Sprite
all_sprites = pygame.sprite.Group() # กล่องเก็บตัวละคร
player = Player()# สร้างตัวละคร
all_sprites.add(player)  # เพิ่มตัวละครเข้าไปในกลุ่ม
		

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

	all_sprites.update()		

	# สีแบคกราวของเกมส์

	screen.fill(BLACK)

	# นำตัวละครมาวาดใส่เกมส์
	all_sprites.draw(screen)



	# ให้ pygame แสดงผล
	pygame.display.flip()

# ออกจากเกมส์
pygame.quit()
