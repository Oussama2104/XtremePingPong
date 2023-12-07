import pygame


class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.rect = pygame.Rect(x - radius, y - radius, 2 * radius, 2 * radius)
        self.speed = 5
        self.direction = [1, 1]

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self, width, height, p):
        # Kollision mit Wänden
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.direction[1] *= -1

        # Kollision mit Spielern
        if self.rect.colliderect(p.rect):
            self.direction[0] *= -1

        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

        if self.x - self.radius < -1 or self.x + self.radius > width + 1:
            # Setze die Position des Balls auf die Mitte des Bildschirms zurück
            self.x = width // 2
            self.y = height // 2
            self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
            # Ändere die Richtung des Balls
            self.direction[0] *= -1

    def respawn(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 5
        self.direction = [1, 1]
