import pygame
import math
import random
import numpy

pygame.init()

WIDTH = 950
HEIGHT = 950





WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Motion of Particles")




# PARTICLEs as a class
class Particle:

    NUMBER = 250
    M = 25

    def __init__(self, initial_x_pos, initial_y_pos, initial_v_x,initial_v_y, acceleration_x,acceleration_y,initial_time , radius, colour, mass):
        self.initial_x_pos = initial_x_pos
        self.initial_y_pos = initial_y_pos
        self.initial_v_x= initial_v_x
        self.initial_v_y = initial_v_y
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.initial_time  = 0
        self.radius = radius
        self.colour = colour
        self.mass = mass

    def pos_update(self, TIME_STEP): 
        pass

    def Linear_draw(self, WIN):
        x = self.initial_x_pos
        y = self.initial_y_pos
        pygame.draw.circle(WIN, self.colour, (int(x), int(y)), self.radius)



    def border_crash(self):
        if (self.initial_x_pos -self.radius < 0 )or (self.initial_x_pos + self.radius > WIDTH):
            self.initial_v_x *= -1
        if (self.initial_y_pos - self.radius < 0) or (self.initial_y_pos +self.radius > HEIGHT):
            self.initial_v_y *= -1

    def particle_collision(self, other_dot):
        distance = math.sqrt(((self.initial_x_pos - other_dot.initial_x_pos)**2)+ (self.initial_y_pos-other_dot.initial_y_pos)**2)
        if distance < self.radius + other_dot.radius:
            self.initial_v_x, other_dot.initial_v_x = other_dot.initial_v_x, self.initial_v_x
            self.initial_v_y, other_dot.initial_v_y = other_dot.initial_v_y, self.initial_v_y


class LinearMotion(Particle):
    TIME_STEP = 3600 * 24

    def __init__(self, initial_x_pos, initial_y_pos, initial_v_x, initial_v_y, acceleration_x, acceleration_y, initial_time, radius, colour, mass, orbital_radius, angle, Pressure, viscosity, buoyancy):
        super().__init__(initial_x_pos, initial_y_pos, initial_v_x, initial_v_y, acceleration_x, acceleration_y, initial_time, radius, colour, mass)
        self.initial_x_pos = initial_x_pos
        self.initial_y_pos = initial_y_pos
        self.initial_v_x = initial_v_x
        self.initial_v_y = initial_v_y
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.initial_time = initial_time
        self.radius = radius
        self.colour = colour
        self.mass = mass
        self.orbital_radius = orbital_radius
        self.angle = angle
        self.Pressure = Pressure
        self.viscosity = viscosity  
        self.buoyancy = buoyancy

    def border_control(self):
        if self.initial_x_pos < 0:
            self.initial_x_pos = 0
        elif self.initial_x_pos > WIDTH:
            self.initial_x_pos = WIDTH

        if self.initial_y_pos < 0:
            self.initial_y_pos = 0
        elif self.initial_y_pos > HEIGHT:
            self.initial_y_pos = HEIGHT

    def pos_update(self, TIME_STEP):
        super().pos_update(TIME_STEP)
        self.initial_x_pos += self.initial_v_x * TIME_STEP * self.M  
        self.initial_y_pos += self.initial_v_y * TIME_STEP * self.M
        self.border_control()
        self.initial_time += TIME_STEP







def main():
    run = True
    clockspeed = pygame.time.Clock()

    particles = [] 



    linear_x_coors = []
    linear_y_coors = []


    for b in range(Particle.NUMBER):
        x_coor = random.randint(0,WIDTH)
        linear_x_coors.append(x_coor)

    for a in range(Particle.NUMBER):
        y_coor = random.randint(0,HEIGHT)
        linear_y_coors.append(y_coor)




    for i in range(Particle.NUMBER):
            particle = LinearMotion(
                initial_x_pos = linear_x_coors[i],  
                initial_y_pos = linear_y_coors[i],
                initial_v_x = random.uniform(-1, 1),  
                initial_v_y = random.uniform(-1, 1),
                acceleration_x = 0,
                acceleration_y = 0,
                initial_time = 0,
                radius= 2,
                colour= (0, 0, 255),
                mass=1,
                orbital_radius=0,
                angle = 0,
                Pressure = 0,
                viscosity = 0,
                buoyancy = 0,
            )
            particles.append(particle)




    while run:
        clockspeed.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for particle in particles:
            particle.pos_update(1)
            particle.border_crash()


            for other_dot in particles:
                if particle != other_dot:
                    particle.particle_collision(other_dot)
        
            particle.Linear_draw(WIN)

        pygame.display.update()

main()


