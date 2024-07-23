from GameFrame import RoomObject, Globals
import random

class Zork(RoomObject):
    """
    A class for the game's antagonist
    """

    def __init__(self, room, x, y):
        """
        Initialize the Zork object
        """
        #include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)

        #set image
        image = self.load_image("Zork.png")
        self.set_image(image, 135, 165)

        #set initial movement
        self.y_speed = random.choice([-10, 10])
    def keep_in_room(self):
        """
        Keep the Zork object in the room
        """
        if self.rect.top < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
    
    def step(self):
        """
        1 per frame
        """
        self.keep_in_room()
