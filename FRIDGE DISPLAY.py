import Weathercode
import pygame
import News
import weathergraph
import random
from PIL import Image
pygame.init()
# Set up the drawing window
screen_size=(1100,800)
screen = pygame.display.set_mode(screen_size)
screen.fill((255,160,122))
# Pick a random ad
ads=['ad.png','ad1.jpg','ad2.jpg','ad3.jpg','ad4.jpg']
random_ad=random.choice(ads)
#Open the original image
original_image = Image.open(random_ad)
# Set the new size
new_size = (500, 400)
# Resize the image
resized_image = original_image.resize(new_size)
# Save the resized image
resized_image.save("newad.jpg")
#load image
image = pygame.image.load('newad.jpg')
# Set the position of the image on the screen
image_position = (700, 200)
# Blit the image onto the screen
screen.blit(image, image_position)
pygame.display.flip()
# Pick a random motivation
tweets=['mot1.jpg','mot2.jpg','mot3.png','mot4.jpg','mot5.jpg']
random_tweet=random.choice(tweets)
#load image
image = pygame.image.load(random_tweet)
# Set the position of the image on the screen
image_position = (0, 630)
# Blit the image onto the screen
screen.blit(image, image_position)
pygame.display.flip()
# set the font and font size
font = pygame.font.SysFont('Arial', 26, bold=True)
#News
i = News.news()
space=font.render(i, True, (0,0,255))
screen.blit(space, (0, 120))
pygame.display.flip()
#Weathergraph
img1 = pygame.image.load('weathergraph.png')
# Set the position of the image on the screen
img1_position = (0,150)
# Blit the image onto the screen
screen.blit(img1, img1_position)
# update the display
pygame.display.flip()
#Sentences describing weather
j=Weathercode.weather2()
font = pygame.font.SysFont('Arial', 26, bold=True)
lines = j.splitlines()
# Render each line on a separate surface
surfaces = []
for line in lines:
    surfaces.append(font.render(line, True, (0, 0, 0)))
# Blit the surfaces onto the screen
y=0
for surface in surfaces:
    screen.blit(surface, (0, y))
    y += surface.get_height()
pygame.display.flip()
image = pygame.image.load('slogo.png')
# Set the position of the image on the screen
image_position = (800, 650)
# Blit the image onto the screen
screen.blit(image, image_position)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
