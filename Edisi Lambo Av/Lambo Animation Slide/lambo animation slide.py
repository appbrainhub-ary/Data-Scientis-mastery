import pygame

# menjalankan pygame
pygame.init()

# mengatur skala aplikasi terbuka Pygame
screen_width, screen_height = 900, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lamborghini Aventador Animation")

# mengambil gambar
car_frames = [
    pygame.image.load("frame1.png"),
    
    # bisa tambahkan lagi sesuai yang di inginkan
]

# mengatur posisi dan frame
car_x = screen_width // 2 - car_frames[0].get_width() // 2
car_y = screen_height - car_frames[0].get_height()
current_frame = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Update the car's position and animation frame
    car_x += 1  # Example: Move the car to the right
    current_frame = (current_frame + 1) % len(car_frames)  # Cycle through frames

    # Draw the car on the screen
    screen.blit(car_frames[current_frame], (car_x, car_y))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
