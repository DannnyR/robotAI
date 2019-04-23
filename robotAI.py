import arcade
import random

# ----CONSTANTS-----
#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 600
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ROBOT = 0.35
#ROBO_COUNT = 100

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Hero:
    def __init__(self, position_x, position_y, radius, color):

        #Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

"""def draw(self)# SPrite Hero called arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)  """

class MyGame(arcade.Window):# WINDOW CLASS CREATED---------

    def __init__(self):
        # INITIALIZER HERE --------------
        # Call the parent class's init function
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "KILLER CAN-BOTS")
        
        # Variables that will hold sprite lists
        self.hero_list = None
        self.robo_list = None

        # Set up the player info
        self.hero_list = arcade.SpriteList # Gun_knight.gif
        self.robo_list = arcade.SpriteList # ROBOT-MARK1.gif

        # score
        self.hero_sprite = None
        self.score = 0        

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create Hero Sprite
        #self.hero = Hero(50, 50, 15, arcade.color.AUBURN) ((commented out may remove?))
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.robo_Attacker_list.draw()
        self.hero_list.draw()
        self.robo_list.draw()
        
    def setup(self):
        # Game created - var initialization
        
        #self.hero_list = arcade.SpriteList()
        #self.robo_list = arcade.SpriteList()
        
        # Below will be where we put the Robot_AI list
        # self.robo_Attacker_list = arcade.SpriteList()  --- Moving Sprite list
        # Score --
        self.score = 0

        # HERO-SPRITE player setter
        # Sprite - robotAI.py - / admin/DCesktop?softwareDEV/Gun Knight.gif/robotAI.py(3.7.2)
        self.hero_sprite = hero("Gun_Knight.gif", SPRITE_SCALING_HERO)
        self.hero_sprite.center_x = 50
        self.hero_sprite.center_y = 50
        self.hero_list.append(self.hero_sprite)
        

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.hero.position_x = x
        self.hero.position_y = y


def main():
    # ISSUE line 68 --my game not defined
    #window = MyGame(800, 600, "Drawing Example")
    window = MyGame()
    window.setup()
    arcade.run()
        
if __name__ == "__main__":
    main()
