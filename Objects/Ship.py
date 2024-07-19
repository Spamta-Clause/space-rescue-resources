from GameFrame import RoomObject
import pygame

class Ship(RoomObject):
    """
    A class for the player's avatar (the Ship)
    """

    def __init__(self, room, x, y):
        """
        Initialize the Ship object
        """
        RoomObject.__init__(self, room, x, y)


        #set image
        image = self.load_image("Ship.png")
        self.set_image(image, 100, 100)

        #register events
        self.handle_key_events = True
    
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """

        if key[pygame.K_W]:
            self.y_speed = -10
        if key[pygame.K_S]:
            self.y_speed = 10