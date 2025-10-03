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

def draw():
    #a = (200, 500)
    #b = (800, 500)
    #lines = [(a, b)]
    lines = []
    num_points = 0
    prev_point = ()
    point = ()
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill((255, 255, 255))
    #for (start, end) in lines:
        #pygame.draw.line(screen, (0, 0, 0), start, end, 2)
    updated = False
    pygame.display.flip()
    running = True
    triangle_mode = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    # Switch to triangle mode
                    triangle_mode = not triangle_mode
                    triangle_points = []
            if locals().get('triangle_mode', False) and event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                triangle_points = locals().get('triangle_points', [])
                triangle_points.append(pos)
                if len(triangle_points) == 2:
                    # Calculate triangle vertices
                    center = triangle_points[0]
                    vertex = triangle_points[1]
                    dx = vertex[0] - center[0]
                    dy = vertex[1] - center[1]
                    r = math.sqrt(dx**2 + dy**2)
                    angle0 = math.atan2(dy, dx)
                    vertices = []
                    for i in range(3):
                        angle = angle0 + i * 2 * math.pi / 3
                        x = center[0] + r * math.cos(angle)
                        y = center[1] + r * math.sin(angle)
                        vertices.append((x, y))
                    # Add triangle edges to lines
                    lines.append((vertices[0], vertices[1]))
                    lines.append((vertices[1], vertices[2]))
                    lines.append((vertices[2], vertices[0]))
                    updated = True
                    triangle_points = []
                    triangle_mode = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not triangle_mode:
                    pos = pygame.mouse.get_pos()
                    prev_point = point
                    point = pos
                    num_points += 1
                    print(num_points)
                    print(num_points % 2)
                    if num_points != 0 and num_points % 2 == 0:
                        lines.append((prev_point, point))
                        updated = True
                        print(f"added line from {prev_point} to {point}")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    lines = get_new_lines(lines)
                    updated = True
        if updated:
            screen.fill((255, 255, 255))
            for (start, end) in lines:
                pygame.draw.line(screen, (0, 0, 0), start, end, 2)
            updated = False
            pygame.display.flip()
    pygame.quit()

draw()