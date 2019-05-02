"""Robot_AI – The machine spirits have awoken; to the detriment of mankind!"""

import random
import arcade


# --- Constants ---
SPRITE_SCALING_HERO = 0.3
SPRITE_SCALING_ROBOT = 0.6
SPRITE_SCALING_BULLET = 0.8
ROBOT_COUNT = 70

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 700

Bullet_Speed = 5



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
            self.change_x *= -2
            
        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


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
        self.bullet_list = None

        # Hero set up inf0
        self.hero_sprite = None
        # Score
        self.score = 0

        # Mouse cursor remover
        self.set_mouse_visible(False)

        # Background color
        arcade.set_background_color(arcade.color.ASH_GREY)
        

    def setup(self):
        """Starts game initializing vars"""

        # SPRITES LISTED
        self.hero_list = arcade.SpriteList()
        self.robot_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

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
            # Twiked the negative numbers below to keep bots on screen
            robot.change_x = random.randrange(-1, 2)
            robot.change_y = random.randrange(-2, 1)
            # ADD ROBOTS TO LIST
            self.robot_list.append(robot)
            
        # Bullet
        self.bullet_sprite = arcade.Sprite("bullet.gif")
        #Add to List
        self.bullet_list.append(self.bullet_sprite)
     
        
    def on_draw(self):
        """DRAW ALL """        
        # 2. Clears screen and rends
        arcade.start_render()
        # Draw Lists
        self.robot_list.draw()
        self.hero_list.draw()
        self.bullet_list.draw()
        # Text Creation on Screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 20, 20, arcade.color.BLACK, 25)
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
    def on_mouse_press(self, x, y, button, modifiers):
        # Bullet Fire
        bullet = arcade.Sprite("bullet.gif", SPRITE_SCALING_BULLET)
        bullet.change_x = Bullet_Speed
        bullet.center_x = self.hero_sprite.center_x
        bullet.center_y = self.hero_sprite.center_y
        bullet.left = self.hero_sprite.right
        self.bullet_list.append(bullet)

    def Sound_ON_Mouse(self):
        # LOADS SOUND
        self.laser_sound = arcade.load_sound("laser.wav")
        # MOUSE LEFT OR RIGHT KEY PRESS TRIGGERS LASER-SOUND
        if key == arcade.key.LEFT or RIGHT:
            arcade.play_sound(self.laser_sound)
        
        
        
    
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

       #BULLET LOGIC
        self.bullet_list.update()
        for bullet in self.bullet_list:
             hit_list = arcade.check_for_collision_with_list(bullet, self.robot_list)
             if len(hit_list) > 0:
                 bullet.kill()
             for robot in hit_list:
                 robot.kill()
                 self.score += 1
             if bullet.left > SCREEN_WIDTH:
                bullet.kill()
       
    def Key_Pressed(self, key, modifiers):
        # CALLED WHEN USER PRESSES KEYS
        if key == arcade.key.LEFT:
            self.hero.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.hero.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.hero.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.hero.change_y = -MOVEMENT_SPEED
            # SPACE BAR PRESSED
        elif key == arcade.key.SPACE:
            self.bullet.change_y and change_x ####
        # SOUND LASER FIRES laser.wav FILE
        # SPACE BAR AND LEFT AND RIGHT MOUSE KEYS
        elif key == arcade.key.SPACE:
            arcade.play_sound(self.laser_sound)
        

    def Key_Release(self, key, modifiers):
        # When key released
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.hero.change_x = 0
        elif key == arcade.UP or key == arcade.key.DOWN:
            self.hero.change_y = 0
        # SPACE BAR RELEASED
        #elif key == arcade.SPACE
            #self.hero.change_y = 0
    
        
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
