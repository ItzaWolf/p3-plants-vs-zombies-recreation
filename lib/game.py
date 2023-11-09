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

# Define the plant spawn points (you can adjust these coordinates)
plant_spawn_points = [
    pygame.Rect(185, 115, 50, 50), pygame.Rect(265, 115, 50, 50), pygame.Rect(345, 115, 50, 50), pygame.Rect(425, 115, 50, 50), pygame.Rect(505, 115, 50, 50),
    pygame.Rect(185, 200, 50, 50), pygame.Rect(265, 200, 50, 50), pygame.Rect(345, 200, 50, 50), pygame.Rect(425, 200, 50, 50), pygame.Rect(505, 200, 50, 50),
    pygame.Rect(185, 300, 50, 50), pygame.Rect(265, 300, 50, 50), pygame.Rect(345, 300, 50, 50), pygame.Rect(425, 300, 50, 50), pygame.Rect(505, 300, 50, 50),
    pygame.Rect(185, 400, 50, 50), pygame.Rect(265, 400, 50, 50), pygame.Rect(345, 400, 50, 50), pygame.Rect(425, 400, 50, 50), pygame.Rect(505, 400, 50, 50),
    pygame.Rect(185, 500, 50, 50), pygame.Rect(265, 500, 50, 50), pygame.Rect(345, 500, 50, 50), pygame.Rect(425, 500, 50, 50), pygame.Rect(505, 500, 50, 50),
    pygame.Rect(585, 115, 50, 50), pygame.Rect(665, 115, 50, 50), pygame.Rect(745, 115, 50, 50), pygame.Rect(825, 115, 50, 50),
    pygame.Rect(585, 200, 50, 50), pygame.Rect(665, 200, 50, 50), pygame.Rect(745, 200, 50, 50), pygame.Rect(825, 200, 50, 50),
    pygame.Rect(585, 300, 50, 50), pygame.Rect(665, 300, 50, 50), pygame.Rect(745, 300, 50, 50), pygame.Rect(825, 300, 50, 50),
    pygame.Rect(585, 400, 50, 50), pygame.Rect(665, 400, 50, 50), pygame.Rect(745, 400, 50, 50), pygame.Rect(825, 400, 50, 50),
    pygame.Rect(585, 500, 50, 50), pygame.Rect(665, 500, 50, 50), pygame.Rect(745, 500, 50, 50), pygame.Rect(825, 500, 50, 50),
]
class SelectedPlant:
    def __init__(self, plant):
        self.plant = plant
        self.image = plant.card_image
        self.rect = self.image.get_rect()
        self.cost = plant.cost
        self.dragging = False

    def update_position(self, x, y):
        self.rect.topleft = (x, y)

def select_plant(plant):
    global selected_plant
    selected_plant = SelectedPlant(plant)

class Plant:
    def __init__(self, name, cost, card_image):
        self.name = name
        self.cost = cost
        self.card_image = card_image
        self.rect = None

# Load plant card images
peashooter_card_image = pygame.image.load("lib/Game/Peashooter-Card.png")
sunflower_card_image = pygame.image.load("lib/Game/Sunflower-Card.png")

# Define a list of available plant types
available_plants = [
    Plant("Peashooter", 100, peashooter_card_image),
    Plant("Sunflower", 50, sunflower_card_image),
    # Add more plant types as needed
]

selected_plant = None

# Create a function to handle plant selection
def select_plant(plant):
    global selected_plant
    selected_plant = plant

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

    selected_plant = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if peashooter_card_rect.collidepoint(event.pos):
                    selected_plant = available_plants[0]
                    if selected_plant:
                        selected_plant.rect = selected_plant.card_image.get_rect()
                        if isinstance(selected_plant, SelectedPlant):
                            selected_plant.dragging = True
                            mouse_x, mouse_y = event.pos
                            selected_plant.rect.topleft = (mouse_x - selected_plant.rect.width // 2, mouse_y - selected_plant.rect.height // 2)
                elif sunflower_card_rect.collidepoint(event.pos):
                    selected_plant = available_plants[1]
                    if selected_plant:
                        selected_plant.rect = selected_plant.card_image.get_rect()
                        if isinstance(selected_plant, SelectedPlant):
                            selected_plant.dragging = True
                            mouse_x, mouse_y = event.pos
                            selected_plant.rect.topleft = (mouse_x - selected_plant.rect.width // 2, mouse_y - selected_plant.rect.height // 2)
            elif event.type == pygame.MOUSEMOTION:
                if selected_plant and isinstance(selected_plant, SelectedPlant) and selected_plant.dragging:
                    mouse_x, mouse_y = event.pos
                    selected_plant.update_position(mouse_x - selected_plant.rect.width // 2, mouse_y - selected_plant.rect.height // 2)

        # Now, outside the event loop (but still inside the game loop), check for plant placement:
        if selected_plant:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for spawn_rect in plant_spawn_points:
                if spawn_rect.collidepoint(mouse_x, mouse_y):
                    if selected_plant.cost <= sun_count:
                        sun_count -= selected_plant.cost
                        selected_plant.rect.topleft = spawn_rect.topleft
                        if hasattr(selected_plant, 'dragging'):
                            selected_plant.dragging = False
                        selected_plant = None

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