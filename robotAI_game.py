"""Robot_AI – The machine spirits have awoken; to the detriment of mankind!"""

import random
import arcade
import timeit
import os
#import pymunk 

# --- Constants ---
SPRITE_SCALING_HERO = 0.3
SPRITE_SCALING_ROBOT = 0.6
SPRITE_SCALING_BULLET = 0.8
ROBOT_COUNT = 70
NATIVE_SPRITE_SIZE = 128
#SPRITE_SIZE = NATIVE_SPRITE_SIZE * SPRITE_SCALING
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 700

Bullet_Speed = 5

VIEWPORT_MARGIN = 200

MOVEMENT_SPEED = 3

EXPLOSIONS_TEXTURE_COUNT = 60

MERGE_SPRITES = True

class Explosions(arcade.Sprite):
    # This is the robot explosion gif
    explosions_textures = []
    
    def __init__(self, texture_list):
        super().__init__("images/explosion0000.png")
        # STart frame
        self.current_texture = 0
        self.textures = texture_list

    def update(self):
        # THis code updates deletes boom_sprite
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.kill()

class hero:
    change_x = 0
    change_y = 0
    
    def __init__(self, position_x, position_y, change_x, change_y):
        super().__init__()
        # self.image = arcade.Surface([15,15])
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        
        
    # Number Robot collisions with hero   
    def update(self, delta_time):
        robot_hit_list = arcade.check_for_collision_with_list,
        (self.hero_sprite, self.hero_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for robot in robot_hit_list:
            robot.kill()
            self.score -= 1

    def draw(self):
        # HERO instance vars
        arcade.sprite_hero(self.position_x, self.position_y)      

class Robot(arcade.Sprite):
    # Robots sprite creation
    def __init__(self, filename, sprite_scaling):
        # Off screen - BRINGS ROBOTS BACK AROUND FOR ANOTHER PASS
        # if self.top < 0: MOVED TO UPDATE DEF BELOW IN SAME CLASS
        super().__init__(filename, sprite_scaling)
            # THIS RESETS ROBOT SO THEY NEVER STOP
        self.center_y = 0
        self.center_x = 0
            
    def update(self):
        self.center_x -=1
        # Off screen - Bounce ROBOTS BACK AROUND FOR ANOTHER PASS
        if self.left < 0:
            self.change_x *= -2
            
        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_WIDTH:
            self.change_y *= -1


    
class View(arcade.Window):
    def __init__(self):
        # 1. arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,"WINDOW TEST")
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Robot_AI – \
The machine spirits have awoken; to the detriment of mankind!")
        # Working directory- SET HERE
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        # Var lists holders
        self.wall_list = None
        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0
        self.hero_list = None
        self.robot_list = None
        self.bullet_list = None
        self.explosions_list = None
        # Hero set up inf0
        self.hero_sprite = None
        # Physics Engine- REALLY!
        self.physics_engine = None
        # USED TO SCROLL
        self.view_bottom = 0
        self.draw_time = 0
        # Score
        self.score = 0
        # Mouse cursor remover
        self.set_mouse_visible(False)
        # Background color
        arcade.set_background_color(arcade.color.ASH_GREY)
        # HERO DECLARED
        #self.hero = hero(50, 50, 0)
        # exploder loader ----------
        self.explosions_texture_list = []
        
        for i in range(EXPLOSIONS_TEXTURE_COUNT):
            # image loaded here
            texture_name = f"images/explosion{i:04d}.png"
            self.explosions_texture_list.append(arcade.load_texture(texture_name))

        self.explosions_texture_list = []
        
        
        
    def Key_Release(self, key, modifiers):
        # When key released
        if key == arcade.key.LEFT or key == arcade.KEY.RIGHT:
            self.hero.change_x = 0
        elif key == arcade.UP or key == arcade.KEY.DOWN:
            self.hero.change_y = 0


    def setup(self):
        """Starts game initializing vars"""
        
        # SPRITES LISTED
        self.hero_list = arcade.SpriteList()
        self.robot_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # setup HERO - hat tip Collin
        self.hero_sprite = arcade.Sprite("Gun_Knight.gif", SPRITE_SCALING_HERO)
        # The below positions the Hero
        self.hero_sprite.center_x = 64
        self.hero_sprite.center_y = 270
        # Adds Hero to list
        # self.hero_list.append(self.hero_sprite)

        #TEST - SHOULD START SCORE AT ZERO-------LN:261
        self.score = 0
       
            
        # create robot - hat tip Dan
        for i in range(ROBOT_COUNT):

            # Robots created
            robot = Robot("ROBOT-MARK1.gif", SPRITE_SCALING_ROBOT)
            # ROBOT PLACED ON MAP
            robot.center_x = random.randrange(SCREEN_WIDTH)
            robot.center_y = random.randrange(150, SCREEN_HEIGHT)
            # Twiked the negative numbers below to keep bots on screen
            robot.change_x = random.randrange(-1, 2)
            robot.change_y = random.randrange(-2, 1)
            # ADD ROBOTS TO LIST
            self.robot_list.append(robot)
            
        # Bullet
        self.bullet_sprite = arcade.Sprite("bullet.gif")
        #Add to List
        self.bullet_list.append(self.bullet_sprite)

        # Place the HERO. If we are in a wall, repeat until we aren't.
        placed = False
        while not placed:
            # Are we in a wall?
            walls_hit = arcade.check_for_collision_with_list,
            (self.hero_sprite, self.wall_list)
            #if len(walls_hit) == 0:
                # Not in a wall! Success!
            placed = True

        self.physics_engine = arcade.PhysicsEngineSimple(self.hero_sprite, self.wall_list)
        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0
        print(f"Total wall blocks: {len(self.wall_list)}")

        
    def on_draw(self):
        """DRAW ALL """        
        # 2. Clears screen and rends
        arcade.start_render()

        output = f"Sprite Count: {sprite_count}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 20 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 40 + self.view_bottom,
                         arcade.color.WHITE, 16)

        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output,
                         self.view_left + 20,
                         SCREEN_HEIGHT - 60 + self.view_bottom,
                         arcade.color.WHITE, 16)

        self.draw_time = timeit.default_timer() - draw_start_time

        # Draw Lists
        self.robot_list.draw()
        self.hero_list.draw()
        self.bullet_list.draw()
        self.explosions_list.draw()
        self.wall_list.draw()


        # Text Creation on Screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 20, 20, arcade.color.BLACK, 25)
        """
        self.wall_list.draw()
        This will be the code for the walls
        """
        x = 300; y = 300; radius = 20
        arcade.draw_circle_filled(x, y, radius, arcade.color.RED)

        x = 200; y = 250; radius = 10
        arcade.draw_circle_filled(x, y, radius, arcade.color.RED)

        x = 300; y = 280; width = 120; height = 100
        start_angle = 190; end_angle = 350
        arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK,
                                start_angle, end_angle, 5)
        

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
        # bullet.angle = 180  --NOT NEEDED-- DSR
        bullet.center_x = self.hero_sprite.center_x
        bullet.center_y = self.hero_sprite.center_y
        bullet.left = self.hero_sprite.right
        self.bullet_list.append(bullet)
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)
            print("Left mouse button pressed at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.laser_sound)
            print("Right mouse button pressed at", x, y)

    def on_key_motion(self, x, y, dx, dy):
        """up-down-left-right - CTRL COMMANDS"""
        # Hero Mouse Matched
        self.hero_sprite.center_x = x
        self.hero_sprite.center_y = y
        
    def update(self, delta_time):
        self.hero.draw()
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x
        
            
    def on_key_press(self, key, modifiers):
        # If the user hits the space bar, play the sound that we loaded
        if key == arcade.key.SPACE:
            print("Space-bar hit")
            bullet = arcade.Sprite("bullet.gif", SPRITE_SCALING_BULLET)
            bullet.change_x = Bullet_Speed
            bullet.angle = 30 # --NOT NEEDED-- Testing use only--SEE DIFFERENCE
            bullet.center_x = self.hero_sprite.center_x
            bullet.center_y = self.hero_sprite.center_y
            bullet.left = self.hero_sprite.right
            self.bullet_list.append(bullet)
            arcade.play_sound(self.laser_sound)
        # CALLED WHEN USER PRESSES KEYS
        # l.R,Up, DWN Keys for additional PLAYER-HERO-MOVEMENT
        # NOT WORKING AS EXPECTED!!!--------------------------
        if key == arcade.key.UP:
            self.hero_sprite.change_y = MOVEMENT_SPEED
            print("UP ARROW HIT")
        elif key == arcade.key.DOWN:
            self.hero_sprite.change_y = -MOVEMENT_SPEED
            print("DOWN ARROW HIT")
        elif key == arcade.key.LEFT:
            self.hero_sprite.change_x = -MOVEMENT_SPEED
            print("LEFT ARROW HIT")
        elif key == arcade.key.RIGHT:
            self.hero_sprite.change_x = MOVEMENT_SPEED
            print("RIGHT ARROW HIT")

    def Key_Release(self, key, modifiers):
        # When key released
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.hero_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.hero_sprite.change_x = 0
        
    
    def update(self, delta_time):
        """Moving Logic for Game"""
        start_time = timeit.default_timer()
        
        self.physics_engine.update()
        # Scroll TRACKER
        changed = False
        # SCROLLING LFT
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.hero_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.hero_sprite.left
            changed = True
        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.hero_sprite.right > right_bndry:
            self.view_left += self.hero_sprite.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.hero_sprite.top > top_bndry:
            self.view_bottom += self.hero_sprite.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.hero_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.hero_sprite.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # SAVE THE TIME TO COMPLETE
        self.processing_time = timeit.default_timer() - start_time
                
        # ****FOR NOW: Sprites called limited movement!!!!!!!
        self.robot_list.update()
        
        # Explode updater
        self.explosions_list.update()
        
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
             hit_list = arcade.check_for_collision_with_list,
             (bullet, self.robot_list, self.explosions)
             if len(hit_list) > 0:
                 explosions = Explosions(self.explosions_texture_list)
                 explosions.center_x = hit_list[0].center_y
                 explosions.center_y = hit_list[0].center_y
                 self.explosions_list.append(explosions)
                 bullet.kill()
             for robot in hit_list:
                 robot.kill()
                 self.score += 1

                 # Bullet killer when moves off-screen
             if bullet.left > SCREEN_WIDTH:
                bullet.kill()
                # TEST CODE IF ROBOT HIT HERO KILL------
             if robot in hit_list:
                 hero.kill()
                 self.score -= 1

        
        
def main():
    # Main Event
    window = View()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
