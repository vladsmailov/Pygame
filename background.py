from models import all_in_one


class Background:
    def __init__(self, screen):
        self.screen = screen

    def show(self, x_coordinate=0):
        """Method for creating background layer."""
        self.screen.blit(all_in_one, (x_coordinate, 0))
        return
