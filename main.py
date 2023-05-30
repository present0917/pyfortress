import pygame
pygame.init()
backgroundColor=(255,255,255)
background=[800,600]
screen=pygame.display.set_mode(background)
done=False
clock=pygame.time.Clock()
tank1=pygame.image.load('images/tank/missile.png')
tank1=pygame.transform.scale(tank1,(80,60))



def running():
    global tank1, done
    x=50
    y=50
    while not done:
        clock.tick(30)
        screen.fill(backgroundColor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y-=10
                elif event.key == pygame.K_DOWN:
                    y+=10
                elif event.key == pygame.K_RIGHT:
                    x+=10
                elif event.key == pygame.K_LEFT:
                    x-=10



        screen.blit(tank1,(x,y))
        pygame.display.update()


running()
pygame.quit()