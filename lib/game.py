import pygame
import random
import imageio

class Sun:
    def __init__(self, image, rect, x, y):
        self.image = image
        self.rect = rect
        self.rect.topleft = (x, y)

def init_game():
    pygame.init()
    
    window_width = 1050
    window_height = 600
    FPS = 60
    game_window = pygame.display.set_mode((window_width, window_height))

    pygame.display.set_caption("Plants VS Zombies")

    background_image = pygame.image.load("lib/Game/Frontyard.jpg")

    taskbar_image = pygame.image.load("lib/Game/Level_1-6.jpg")
    taskbar_rect = taskbar_image.get_rect()
    taskbar_rect.topleft = (0, 0)

    sun_image = pygame.image.load("lib/Game/sun.gif")  # Load your sun image
    sun_instances = []
    current_frame = 0

    font = pygame.font.Font(None, 36)
    sun_count = 100

    return game_window, background_image, taskbar_image, taskbar_rect, font, sun_count, sun_image, sun_instances

def run_game():
    game_window, background_image, taskbar_image, taskbar_rect, font, sun_count, sun_image, sun_instances = init_game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if random.randint(0, 10000) < 3:
            x = random.randint(150, 825)
            y = random.randint(100, 500)
            sun_instances.append(Sun(sun_image, sun_image.get_rect(), x, y))
        
        for sun in sun_instances[:]:
            if sun.rect.collidepoint(pygame.mouse.get_pos()):
                sun_instances.remove(sun)
                sun_count += 25

        game_window.blit(background_image, (0, 0))

        game_window.blit(taskbar_image, taskbar_rect)

        for sun in sun_instances:
            game_window.blit(sun.image, sun.rect)

        sun_text = font.render(f"{sun_count}", True, (0, 0, 0))
        game_window.blit(sun_text, (26, 75))

        pygame.display.update()

def quit_game():
    pygame.quit()

if __name__ == "__main__":
    run_game()
    quit_game()