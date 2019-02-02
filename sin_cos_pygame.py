import pygame, math
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([250,250,250])

#coords
pygame.draw.rect(screen,[80,80,80],[0,240,640,1],1)
pygame.draw.rect(screen,[80,80,80],[320,0,1,480],1)

_pointssin = [] 
_pointscos = []
#sinus
for x in range(0, 640):
	y = int(240+30*math.sin((x/640.0*8*math.pi)))
	pygame.draw.rect(screen,[255,0,0],[x,y,1,1],2)
	_pointssin.append([x,y])
pygame.draw.lines(screen,[255,0,0], False, _pointssin, 2)	
#cosinus
for x in range(0, 640):
	y = int(240+30*math.cos((x/640.0*8*math.pi)))
	pygame.draw.rect(screen,[0,0,255],[x,y,1,1],2)
	_pointscos.append([x,y])
pygame.draw.lines(screen,[0,0,255], False, _pointscos, 2)
pygame.display.flip()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
pygame.quit()