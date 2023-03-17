import pygame,sys
from pytmx.util_pygame import load_pygame

pygame.init()
screen_width, screen_height = (1024, 1024)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("topdown game level create by Tiled")

fps = 60
clock = pygame.time.Clock()

# Import Tiled layers whit pytmx  
tmx_data = load_pygame('/Users/woravittosomrit/Desktop/python2D/topdown.tmx')
#print(tmx_data)

# Created two spritegroup
tile_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()

# # Created Tile class
class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)


# Get tileset from Tile layer
for layer in tmx_data.visible_layers:
	if hasattr(layer, 'data'):
		# print(layer)
		for x,y,surf in layer.tiles():
			pos = (x * 32,y * 32)
			Tile(pos = pos, surf = surf, groups=tile_sprite)
			

# create Player class
class Player(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups):
		super().__init__(groups)
		self.image = surf  
		self.rect = self.image.get_rect(topleft = pos)	

		# # movement
		# self.direction = pygame.math_Vector2()
		# self.speed = 2


	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0
			
	def move(self,speed):

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.rect.x += self.direction.x * speed
		self.rect.y += self.direction.y * speed


	def update(self):
		self.input()
		self.move(self.speed)

# Import tiled layers with pytmx
tmx_data = load_pygame('/Users/woravittosomrit/Desktop/python2D/topdown.tmx')

# Sprite Group for Tileset

tile_sprite_group = pygame.sprite.Group()

#Sprite Group for Objects

player_sprite_group = pygame.sprite.Group()
object_sprite_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,surf,groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)

for layer in tmx_data.visible_layers:
	if  hasattr(layer,'data'):
		for x,y,surf in layer.tiles():
			pos = (x *32, y * 32) #Mult by tilesize
			Tile(pos = pos, surf = surf, groups = tile_sprite_group)

# Get objects layer

# Get objects and player obj
 
object_layer = tmx_data.get_layer_by_name('Object_Layer')

for obj in object_layer:

	if obj.name == 'Player':
		pos = (obj.x, obj.y)
		print(obj)
		print("Player here")
		player = Player(pos = pos, surf = obj.image, groups = player_sprite_group)
	
	else:
  		print(obj)
  		pos = (obj.x, obj.y)
  		Tile(pos = pos, surf = obj.image, groups = tile_sprite)
	

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
 
	screen.fill('black')
	tile_sprite_group.draw(screen)
	#objects_sprite_group.draw(screen)
	player_sprite_group.draw(screen)
	#player_sprite.group.update()


	pygame.display.update()
	clock.tick(fps)














