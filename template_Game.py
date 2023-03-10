import pygame

# เริ่มต้น โปรเจค
pygame.init()

 # เฟรมเรท
fps = 30

# ความกว้าง สูงของเกมส์
WIDTH = 800
HEIGHT =700

# สร้างสี
BLACK = (0, 0, 0)

# สร้าง สกรีน   
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# ชื่อ
pygame.display.set_caption('My First Game By Woravit')

# สร้างนาฬิกาของเกมส์ จัดการเวลา
clock = pygame.time.Clock()


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

	# background color
	screen.fill(BLACK)

	# ให้ pygame แสดงผล
	pygame.display.flip()

# ออกจากเกมส์
pygame.quit()
