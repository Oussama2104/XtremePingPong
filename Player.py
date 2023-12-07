import pygame


class Player:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (x, y, width, height)
        self.image_path = image

    def draw(self, win):
        image = pygame.transform.scale(pygame.image.load(self.image_path), (self.width, self.height))
        win.blit(image, (self.x, self.y))

    def move(self, height):
        mouse_y = pygame.mouse.get_pos()[1]
        if mouse_y < 0:
            self.y = 0
        elif mouse_y > height - self.height:
            self.y = height - self.height
        else:
            self.y = mouse_y

        self.rect = (self.x, self.y, self.width, self.height)

    def leftClick(self):
        click = pygame.mouse.get_pressed()
        if click[0]:
            return True
