import pygame


class Boid:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        arrow_length = 1  # Set this to the desired arrow length

        # Normalize the velocity vector
        speed = (self.dx**2 + self.dy**2) ** 0.5
        dx = self.dx / speed
        dy = self.dy / speed

        # Scale the normalized vector by the arrow length
        dx *= arrow_length
        dy *= arrow_length

        # Calculate the end point of the arrow
        endx = self.x + dx
        endy = self.y + dy

        # Draw the main line of the arrow
        pygame.draw.line(screen, (0, 0, 255), (self.x, self.y), (endx, endy), 2)

        # Calculate the points for the arrowhead
        arrowhead = [
            (endx, endy),
            (endx - 5 * dy, endy + 5 * dx),
            (endx + 5 * dy, endy - 5 * dx),
        ]

        # Draw the arrowhead
        pygame.draw.polygon(screen, (0, 0, 255), arrowhead)
