import pygame
import random
import imageio
import time

class Sun:
    def __init__(self, images, rect, frame_delay):
        self.images = images
        self.rect = rect
        self.current_frame = 0
        self.frame_delay = frame_delay
        self.last_frame_time = 0

    def update_frame(self, current_time):
        if current_time - self.last_frame_time > self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.last_frame_time = current_time

def load_sun_images():
    sun_images = [pygame.image.load(f"lib/Game/Sun Animation/sun-{i}.gif") for i in range(3, 23)]
    return sun_images

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

    peashooter_card_image = pygame.image.load("lib/Game/Peashooter-Card.png")
    peashooter_card_rect = peashooter_card_image.get_rect()
    peashooter_card_rect.topleft = (90, 7)

    sunflower_card_image = pygame.image.load("lib/Game/Sunflower-Card.png")
    sunflower_card_rect = sunflower_card_image.get_rect()
    sunflower_card_rect.topleft = (160, 7)

    desired_sunflower_card_width = 63
    desired_sunflower_card_height = 88
    sunflower_card_image = pygame.transform.scale(sunflower_card_image, (desired_sunflower_card_width, desired_sunflower_card_height))

    desired_card_width = 63
    desired_card_height = 88
    peashooter_card_image = pygame.transform.scale(peashooter_card_image, (desired_card_width, desired_card_height))

    print(f"Sunflower card image size: {sunflower_card_image.get_size()}")

    sun_images = load_sun_images()
    sun_instances = []
    current_frame = 0

    font = pygame.font.Font(None, 36)
    sun_count = 100

    return game_window, background_image, taskbar_image, taskbar_rect, font, sun_count, sun_images, sun_instances, current_frame, peashooter_card_image, peashooter_card_rect, sunflower_card_image, sunflower_card_rect

def run_game():
    game_window, background_image, taskbar_image, taskbar_rect, font, sun_count, sun_images, sun_instances, current_frame, peashooter_card_image, peashooter_card_rect, sunflower_card_image, sunflower_card_rect = init_game()

    running = True
    x = 0
    y = 0
    frame_delay = 55

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()

        if random.randint(0, 10000) < 3:
            x = random.randint(150, 825)
            y = random.randint(100, 500)
            sun = Sun(sun_images, pygame.Rect(x, y, sun_images[0].get_width(), sun_images[0].get_height()), frame_delay)
            sun_instances.append(sun)
        
        for sun in sun_instances[:]:
            if sun.rect.collidepoint(pygame.mouse.get_pos()):
                sun_instances.remove(sun)
                sun_count += 25

        game_window.blit(background_image, (0, 0))

        game_window.blit(taskbar_image, taskbar_rect)

        game_window.blit(peashooter_card_image, peashooter_card_rect)

        game_window.blit(sunflower_card_image, sunflower_card_rect)

        for sun in sun_instances:
            sun.update_frame(current_time)
            sun_frame = sun.images[sun.current_frame]
            game_window.blit(sun_frame, (sun.rect.x, sun.rect.y))

        sun_text = font.render(f"{sun_count}", True, (0, 0, 0))
        game_window.blit(sun_text, (26, 75))

        pygame.display.update()

def quit_game():
    pygame.quit()

if __name__ == "__main__":
    run_game()
    quit_game()