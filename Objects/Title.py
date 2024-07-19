from GameFrame import RoomObject

class Title(RoomObject):
    """
    The object for displaying the title of the game
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        #set image
        image = self.load_image("title.png")
        self.set_image(image,800,350)