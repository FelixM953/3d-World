import pygame
import pygame.display
from sys import exit
import math
from object import Cube

FOCAL_LENGTH = 150

pos = (0, 0, 15)
c = Cube(pos, 5)
objects = [c]

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def project(x, z, focal_length):
    return x*focal_length//z


def project_vertex(vertex, focal_length):
    x, y, z = vertex
    x_projected = project(x, z, focal_length)
    y_projected = project(y, z, focal_length)
    return (x_projected, y_projected)


def apply_offset(origin, vertex):
    return (vertex[0]+origin[0], vertex[1]+origin[1], vertex[2]+origin[2])


def draw_wireframes():
    for object in objects:
        for vertex in object.vertecies:
            shifted_vertex = apply_offset(object.origin, vertex)
            x, y = project_vertex(shifted_vertex, FOCAL_LENGTH)
            pygame.draw.circle(screen, (255,255,255), (x+WIDTH//2, y+HEIGHT//2), 5)
        for edge in object.edges:
            v1, v2 = [object.vertecies[i] for i in edge]
            shifted_v1 = apply_offset(object.origin, v1)
            shifted_v2 = apply_offset(object.origin, v2)
            x1, y1 = project_vertex(shifted_v1, FOCAL_LENGTH)
            x2, y2 = project_vertex(shifted_v2, FOCAL_LENGTH)

            pygame.draw.line(screen, (255, 255, 255), (x1+WIDTH//2, y1+HEIGHT//2), (x2+WIDTH//2, y2+HEIGHT//2), 1)
            

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        objects[0].origin = (objects[0].origin[0]+0.5, objects[0].origin[1], objects[0].origin[2])
    if keys[pygame.K_RIGHT]:
        objects[0].origin = (objects[0].origin[0]-0.5, objects[0].origin[1], objects[0].origin[2])
    if keys[pygame.K_UP] and FOCAL_LENGTH > 1:
        objects[0].origin = (objects[0].origin[0], objects[0].origin[1]+0.5, objects[0].origin[2])
    if keys[pygame.K_DOWN]:
        objects[0].origin = (objects[0].origin[0], objects[0].origin[1]-0.5, objects[0].origin[2])
    if keys[pygame.K_PAGEUP] and FOCAL_LENGTH > 1:
        objects[0].origin = (objects[0].origin[0], objects[0].origin[1], objects[0].origin[2]-0.5)
    if keys[pygame.K_PAGEDOWN]:
        objects[0].origin = (objects[0].origin[0], objects[0].origin[1], objects[0].origin[2]+0.5)

    if keys[pygame.K_LEFTBRACKET] and FOCAL_LENGTH > 1:
        FOCAL_LENGTH -= 5
    if keys[pygame.K_RIGHTBRACKET]:
        FOCAL_LENGTH += 5
    


    screen.fill((0, 0, 0))
    draw_wireframes()
    # draw_sides()
    pygame.display.update()
