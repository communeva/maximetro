#!/usr/bin/python

import pygame
from pygame.locals import *

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

STATIONSIZE = 17
STATIONTHICKNESS = 5

screen = pygame.display.set_mode((500, 500))


class Track():
	"""A railtrack"""
	
	def __init__(self,pos):
		# pygame.sprite.Sprite.__init__(self)
		self.startpos = pos
		self.endpos = pos
		# self.status = 'new'
		
	def draw(self):
		pygame.draw.line(screen,RED,self.startpos,self.endpos,5)
		
class Station():
	"""a station"""

	def __init__(self,pos,shape='circle'):
		self.shape = shape
		self.pos = pos
		
	def draw(self):
		size = 20
		pos = self.pos
		#		print "draw circle at pos: " , pos
		if self.shape == 'circle':
			pygame.draw.circle(screen,BLACK,pos,STATIONSIZE)
			pygame.draw.circle(screen,WHITE,pos,STATIONSIZE-STATIONTHICKNESS)

stations = Station((100,100)),Station((200,200))
tracks = []

def is_in_range(pos1,pos2,dist=STATIONSIZE):
	"""retruns true if pos1 and pos2 are not more than dist pixels apart"""
	
	if pos1[0] < pos2[0] - dist:
		return False
	if pos1[0] > pos2[0] + dist:
		return False 		
	if pos1[1] < pos2[1] - dist:
		return False 
	if pos1[1] > pos2[1] + dist:
		return False 
		
	return True

def is_station_pos(pos):
	"""returns true if at pos is a station.
	this could maybe easier implemented with SpriteGroups?"""
	
	for s in stations:
		if is_in_range(pos,s.pos):
			return True 
	return False

def main():

	# initialize global status
	draw_status = False

	# Initialise screen
	pygame.init()
	clock = pygame.time.Clock()
	# screen = pygame.display.set_mode((500, 500))
	pygame.display.set_caption('Maxi Metro')

	# Fill background
	#background = pygame.Surface(screen.get_size())
	#background = background.convert()
	#background.fill(WHITE)

	# Display some text
	#font = pygame.font.Font(None, 36)
	#text = font.render("Hello There", 1, (10, 10, 10))
	#textpos = text.get_rect()
	#textpos.centerx = background.get_rect().centerx
	#background.blit(text, textpos)

	screen.fill(WHITE)
		
	# Blit everything to the screen
	#screen.blit(background, (0, 0))
	pygame.display.update()

	pos = (0,0);
	# Event loop
	while 1:

		screen.fill(WHITE)
			
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == MOUSEBUTTONDOWN:
				pos = event.pos
				if is_station_pos(pos):
					track = Track(pos)
					print "start drawing from " , track.startpos
					draw_status = True
			elif event.type == MOUSEMOTION:
				pos = event.pos
			elif event.type == MOUSEBUTTONUP:
				if draw_status:
					# pos = event.pos
					print "stop drawing at " , pos
					# screen.fill(WHITE)
					track.endpos = pos
					tracks.append(track)
					draw_status = False
		
		if draw_status:

			pygame.draw.line(screen,BLACK,track.startpos,pos,5)

		# display some stations and tracks
		for t in tracks:
			t.draw()		
		for s in stations:
			s.draw()

		pygame.display.update()
		msElapsed = clock.tick(10)
		
		
if __name__ == '__main__': main()
