import pygame
import random
from threading import Semaphore

# Khởi tạo màn hình
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Balls")

# Định nghĩa màu sắc
WHITE = (255, 255, 255)

# Định nghĩa lớp Ball
class Ball:
    def __init__(self, x, y, radius, color, semaphore):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = random.choice([-1, 1]) * random.randint(1, 3)
        self.dy = random.choice([-1, 1]) * random.randint(1, 3)
        self.semaphore = semaphore

    def update(self):
        # Acquire  semaphore trước khi cập nhật vị trí
        self.semaphore.acquire()

        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.dx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.dy *= -1

        # Release semaphore sau khi cập nhật vị trí
        self.semaphore.release()

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Tạo danh sách các trái banh
balls = []
num_balls = 6
semaphore = Semaphore(value=2)  # Semaphore có giá trị ban đầu là 2

for _ in range(num_balls):
    x = random.randint(50, width - 50)
    y = random.randint(50, height - 50)
    radius = random.randint(10, 30)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ball = Ball(x, y, radius, color, semaphore)
    balls.append(ball)

# Vòng lặp chính
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for ball in balls:
        ball.update()
        ball.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
