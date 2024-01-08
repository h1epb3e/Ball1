import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Các tham số màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Balls")

# Định nghĩa màu sắc
white = (255, 255, 255)

# Class đại diện cho mỗi quả bóng
class Ball:
    def __init__(self):
        self.radius = random.randint(10, 30)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.speed_x = random.randint(2, 5)
        self.speed_y = random.randint(2, 5)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Nảy lên khi chạm vào các cạnh
        if self.x <= self.radius or self.x >= width - self.radius:
            self.speed_x = -self.speed_x
        if self.y <= self.radius or self.y >= height - self.radius:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Tạo danh sách các quả bóng
num_balls = 2
balls = [Ball() for _ in range(num_balls)]

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Xóa màn hình
    screen.fill(white)

    # Di chuyển và vẽ mỗi quả bóng
    for ball in balls:
        ball.move()
        ball.draw()

    # Cập nhật màn hình
    pygame.display.flip()

    # Đặt tốc độ khung hình (FPS)
    pygame.time.Clock().tick(60)
