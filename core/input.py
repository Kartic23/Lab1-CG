import pygame


class Input(object):
    """Manages the users commands"""
    def __init__(self) -> None:
        """User terminated?"""
        self.quit = False

    def update(self):
        """Manage user input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
