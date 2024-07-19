from GameFrame import RoomObject, Globals
import pygame
from colorama import Fore, Style

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
        
        if Globals.MOVEMENT_METHOD == "always":
            """
            Respond to keypress up and down
            """

            if key[pygame.K_w]:
                self.y_speed = -10
            if key[pygame.K_s]:
                self.y_speed = 10
        elif Globals.MOVEMENT_METHOD == "while":
            """
            Respond to keypress up and down
            """

            if key[pygame.K_w]:
                self.y_speed = -10
            elif key[pygame.K_s]:
                self.y_speed = 10
            else:
                self.y_speed = 0
        elif Globals.MOVEMENT_METHOD == "acceleration":
            """
            Respond to keypress up and down
            """

            if key[pygame.K_w]:
                self.y_speed -= 5
            elif key[pygame.K_s]:
                self.y_speed += 5
        
        else:
            print(Fore.RED + Style.BRIGHT + "Movement method not recognized" + Style.RESET_ALL)
    
    def keep_in_room(self):
        """
        Keeps the ship inside the room
        """

        if self.y <0:
            self.y = 0
        elif self.y + self.height > Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
    
    def step(self):
        """
        Determine what happens to the Ship on each click of the game clock
        """
        self.keep_in_room()
    