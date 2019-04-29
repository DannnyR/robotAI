"""Robot_AI – The machine spirits have awoken; to the detriment of mankind!"""

import random
import arcade


# --- Constants ---
SPRITE_SCALING_HERO = 0.3
SPRITE_SCALING_ROBOT = 0.6
ROBOT_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800



class Robot(arcade.Sprite):
    # Robots sprite creation
    def __init__(self, filename, sprite_scaling):
        # self.center_y -= 1 CODE MOVED TO NEW FUNCTION
        # Off screen - BRINGS ROBOTS BACK AROUND FOR ANOTHER PASS
        # if self.top < 0: MOVED TO UPDATE DEF BELOW IN SAME CLASS
        super().__init__(filename, sprite_scaling)
            # THIS RESETS ROBOT SO THEY NEVER STOP
        self.center_y = 0
        self.center_x = 0
            
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        # Off screen - Bounce ROBOTS BACK AROUND FOR ANOTHER PASS
        if self.left < 0:
            self.change_x *= -1
            
        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


"""
    def Smiles(self):
        # THE SMILE FACE
        x = 300; y= 300; radus = 200
        arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)
        # DRAW R-EYE
        x = 370; y = 350; radius = 20
        arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
        # DRAW L-EYE
        x = 230; y = 350; radius = 20
        arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
        # DRAW THE BULLET HOLE
        x = 115; y = 175; radius = 30
        arcade.draw_circle_filled(x, y, radius, arcade.color.RED)
        # SMILE - HERO
        x = 300; y = 280; width = 120; height = 100
        start_angle = 190; end_angle = 350; line_width = 10
        arcade.draw_arc_outline(x, y, width, height, arcade.color.black,
                                start_angle, end_angle, line_width)
    def switch(self, x, y):
        """
         # This function creates the switches that shut down the AI
"""
        # Draw lever on the wall
        arcade.draw_triangle_filled(x + 40, y,
                                    x, y - 100,
                                    arcade.color.Dark_RED)
        # Draw switch column
        arcade.draw_rectangle_filled(x + 30, x + 50,
                                          y - 100, y - 140,
                                          arcade.color.WHITE)
        
       """     

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
        # The below positions the Hero
        self.hero_sprite.center_x = 50
        self.hero_sprite.center_y = 50
        # Adds Hero to list
        self.hero_list.append(self.hero_sprite)
        # self.draw_switch.random.randrange(SCREEN_WIDTH)
        # self.draw_Smiles.left_y = 0

        # create robot - hat tip Dan
        for i in range(ROBOT_COUNT):

            # Robots created
            robot = Robot("ROBOT-MARK1.gif", SPRITE_SCALING_ROBOT)
            # ROBOT PLACED ON MAP
            robot.center_x = random.randrange(SCREEN_WIDTH)
            robot.center_y = random.randrange(SCREEN_WIDTH)
            robot.change_x = random.randrange(-1, 2)
            robot.change_y = random.randrange(-2, 1)
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
        """
        self.wall_list.draw()
        This will be the code for the walls
        """

    def on_mouse_motion(self, x, y, dx, dy):
        """MOUSE CTRL COMMANDS"""
        # Hero Mouse Matched
        self.hero_sprite.center_x = x
        self.hero_sprite.center_y = y
    
        # Mouse buttons enabled
    def on_mouse_press(self, x, y, button, key_modifiers):
        pass
    
    def update(self, delta_time):
        """Moving Logic for Game"""
        # ****FOR NOW: Sprites called limited movement!!!!!!!
        self.robot_list.update()
        # Robot Victories
        hit_list = arcade.check_for_collision_with_list(self.hero_sprite,
                                                         self.robot_list)
        # for loop for counting collisions and removing dead robots
        for robot in hit_list:
            # robot.kill() ---NO KILL COMMAND CONTIMUES ROBOT TOP OF SCREEN
            self.score += 1
            # RANDOM RESETS OF ROBOT
            robot.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                              SCREEN_HEIGHT + 100)
            robot.center_y = random.randrange(SCREEN_WIDTH)
       # Keyboard press button / CONTROLS
    def Key_Pressed(self, key, modifiers):
        # CALLED WHEN USER PRESSES KEYS
        if key == arcade.key.LEFT:
            self.hero.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.hero.change_y = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.hero.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.hero.change_y = -MOVEMENT_SPEED

    def Key_Release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.hero.change_x = 0
        elif key == arcade.UP or key == arcade.key.DOWN:
            self.hero.change_y = 0
    
        
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
    # draw_Smiles(25, 250)
    # draw_switch(100, 70)

if __name__ == "__main__":
    main()
