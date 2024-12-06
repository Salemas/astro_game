import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rotation_angle= random.uniform(20, 50)
            velocity_a = self.velocity.rotate(rotation_angle)
            velocity_b = self.velocity.rotate(-rotation_angle)
            radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_a = Asteroid(self.position.x, self.position.y, radius)
            asteroid_a.velocity = velocity_a *1.2

            asteroid_b = Asteroid(self.position.x, self.position.y, radius)
            asteroid_b.velocity = velocity_b *1.2



    # def draw(self, screen):
    #     pygame.draw.circle(screen, 'white', self.position , self.radius, width=2)

    # def update(self, dt):
    #     self.position += self.velocity * dt
