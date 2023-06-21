
import pygame as p
import sys


global x_speed
global y_speed

x_speed = 4
y_speed = 5

other_speed = 2

def move_rect():

    global x_speed 
    global y_speed
    global other_speed

    test_rect.x += x_speed
    test_rect.y += y_speed
    
    p.draw.rect(screen, (255,255,255), test_rect)
    p.draw.rect(screen, (255,255,0), test_rect2)

    # Border collisions
    if test_rect.right >= screen_width or test_rect.left <= 0:
        x_speed *= -1

    if test_rect.bottom >= screen_height or test_rect.top <= 0:
        y_speed *= -1
    
    # Move second rectangle
    test_rect2.y += other_speed

    if test_rect2.top <= 0 or test_rect2.bottom >= screen_height:
        other_speed *= -1



    # Collisions with Rect 
    collision_tolerance = 10

    if test_rect.colliderect(test_rect2):
        if abs(test_rect2.top - test_rect.bottom) < collision_tolerance and y_speed > 0: # What the fuck
            y_speed *= -1
        
        if abs(test_rect2.bottom - test_rect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1

        if abs(test_rect2.right - test_rect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1

        if abs(test_rect2.left - test_rect.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1



def main():

    global test_rect
    global test_rect2
    global screen
    global screen_width
    global screen_height
    
    # initialization
    p.init()
    clock = p.time.Clock()
    screen_width, screen_height = 800,800
    screen = p.display.set_mode((screen_width, screen_height))
 

    test_rect = p.Rect(350,350,100,100)
    test_rect2 = p.Rect(300,600,200,100)

    # MAIN GAME LOOP
    while True:

        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()

       
        screen.fill((30,30,30))
        move_rect()
        p.display.flip()
        clock.tick(60)
   



if __name__ == "__main__":
    main()
    