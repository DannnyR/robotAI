"""Robot_AI – The machine spirits have awoken; to the detriment of mankind!"""

import random
import arcade

# --- Constants ---
SPRITE_SCALING_HERO = 0.5
SPRITE_SCALING_ROBOT = 0.2
ROBOT_COUNT = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class Robot(arcade.Sprite):
    # Robots sprite creation
    
    def update(self):
        self.center_y -= 1

class View(arcade.Window):
    # Window creation class

    def __init__(self):
        # StartS WINDOW
        # 1. arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,"WINDOW TEST")
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,"Robot_AI – \
The machine spirits have awoken; to the detriment of mankind!")

        # Var lists holders
        self.hero_list = None
        self.robot_list = None

        # Hero set up inf0
        self.hero_sprite = None
        # Score
        self.score = 0

        # Mouse cursor remover
        self.set_mouse_visible(False)

        # Background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """Starts game initializing vars"""

        # SPRITES LISTED
        self.hero_list = arcade.SpriteList()
        self.robot_list = arcade.SpriteList()

        # setup HERO - hat tip Collin
        self.hero_sprite = arcade.Sprite("Gun_Knight.gif", SPRITE_SCALING_HERO)
        self.hero_sprite.center_x = 80
        self.hero_sprite.center_y = 50
        self.hero_list.append(self.hero_sprite)

        # creat robot - hat tip Dan
        for i in range(ROBOT_COUNT):

            # Robots created
            robot = Robot("ROBOT-MARK1.gif", SPRITE_SCALING_ROBOT)
            # ROBOT PLACED ON MAP
            robot.center_x = random.randrange(SCREEN_WIDTH)
            robot.center_y = random.randrange(SCREEN_HEIGHT)
            # ADD ROBOTS TO LIST
            self.robot_list.append(robot)
     
        
    def on_draw(self):
        """DRAW ALL """        
        # 2. Clears screen and rends
        arcade.start_render()
        # Draw Lists
        self.robot_list.draw()
        self.hero_list.draw()
        # Text Creation on Screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """MOUSE CTRL COMMANDS"""
        # Hero Mouse Matched
        self.hero_sprite.center_x = x
        self.hero_sprite.center_y = x

    def update(self, delta_time):
        """Moving Logic for Game"""
        # ****FOR NOW: Sprites called limited movement!!!!!!!
        self.robot_list.update()
        # Robot Victories
        hit_list = arcade.check_for_collision_with_list(self.hero_sprite,
                                                         self.robot_list)
        # for loop for counting collisions and removing dead robots
        for robot in hit_list:
            robot.kill()
            self.score += 1

def main():
    # Main Event
    window = View()
    window.setup()
    arcade.run()
    # 3. DISPLAY RESULTS
    # arcade.finish_render()
    # 4. KEEPS WINDOW ALIVE UNTIL KILLED
    # arcade.run()
    # Robot(Window)

if __name__ == "__main__":
    main()
