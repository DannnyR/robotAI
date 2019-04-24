"""Robot_AI – The machine spirits have awoken; to the detriment of mankind!"""

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class Robot(arcade.Sprite):
    # Robots sprite creation
    
    def update(self):
        self.center_y -= 1

class Window(arcade.Window):
    # Window creation class

    def __inti__(self):
        # StartS WINDOW
        # 1. arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,"WINDOW TEST")
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,"Robot_AI – \
The machine spirits have awoken; to the detriment of mankind!")

        # Var lists holders
        self.hero_list = None
        self.robot_list = None

        # Hero set up inf0
        self.hero_sprite = None
        self.robot_list = None

        # Mouse cursor remover
        self.set_mouse_visible(False)

        # Background color
        arcade.set_background_color(arcade.color.Black)

    def setup(self):
        """Starts game initializing vars"""

        # SPRITES LISTED
        self.hero_list = arcade.SpriteList()
        self.robot_list = SPriteList()

        # Score
        self.score = 0

        # setup HERO
        self.hero_sprite = aracde.Sprite("Gun_Knight.gif")
        self.hero_sprite.bottom_x = 50
        self.hero_sprite.center_y = 50
        self.hero_list.append(self.player_sprite)
        
        
        # 2. Clears screen and rends
        arcade.start_render()

        # 3. DISPLAY RESULTS
        arcade.finish_render()

        # 4. KEEPS WINDOW ALIVE UNTIL KILLED


arcade.run()


    
        
Robot(Window)
























