import math
import pygame

def get_new_lines(lines):
    new_lines = []
    for ((x1, y1), (x2, y2)) in lines:
        a = ((2 * x1 + x2) / 3, (2 * y1 + y2) / 3)
        b = ((x1 + 2 * x2) / 3, (y1 + 2 * y2) / 3)
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        angle = math.atan2(dy, dx) - math.pi / 3
        length = math.sqrt(dx**2 + dy**2)
        tip = (a[0] + math.cos(angle) * length, a[1] + math.sin(angle) * length)
        new_lines.append(((x1, y1), a))
        new_lines.append((a, tip))
        new_lines.append((tip, b))
        new_lines.append((b, (x2, y2)))
    return new_lines

def draw(lines):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))
    for (start, end) in lines:
        pygame.draw.line(screen, (0, 0, 0), start, end, 2)
    updated = False
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    lines = get_new_lines(lines)
                    updated = True
        if updated:
            for (start, end) in lines:
                pygame.draw.line(screen, (0, 0, 0), start, end, 2)
            updated = False
            pygame.display.flip()
    pygame.quit()

a = (200, 300)
b = (600, 300)
lines = [(a, b)]

draw(lines)