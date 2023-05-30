import pygame
from tank import tank
import map
pygame.init()
backgroundColor=(255,255,255)#배경색지정
background=[800,600] #배경 해상도
screen=pygame.display.set_mode(background) #screen을 지정한 해상도로
done=False #게임이 끝났는가?
clock=pygame.time.Clock()
tank1=tank('images/tank/missile.png',(100,60))#tank 객체를 사용해 모듈화해서 사용.


def running():
    global tank1, done #케릭터와 완료여부 전역변수로
    tank1x=50 #tank 초기위치
    tank1y=50
    while not done:
        clock.tick(30)
        screen.fill(backgroundColor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tank1y-=10
                elif event.key == pygame.K_DOWN:
                    tank1y+=10
                elif event.key == pygame.K_RIGHT:
                    tank1x+=10
                elif event.key == pygame.K_LEFT:
                    tank1x-=10

       
        map.drawRec(screen, (0,0,0), (50,500,300,50))

        screen.blit(tank1.img,(tank1x,tank1y))
        pygame.display.update()


running()
pygame.quit()