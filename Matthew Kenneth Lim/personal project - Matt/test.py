import arcade
from players import playercharacter

height = 16 * 20 * 2
width =  16 * 30 * 2
speedofcharacter = 3.5
# Margins for scrolling
VIEWPORT_MARGIN = 200

CAMERA_SPEED = 0.5

class Startscreen(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.logo = arcade.load_texture("../Lesson 12/logo2.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE_SMOKE)





    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(width/2,350,250,100,self.logo)
        #arcade.draw_text("Farm",width/2,300,arcade.csscolor.DARK_GREEN,30,anchor_x= "center",font_name="Pixelate")
        arcade.draw_text("Click anywhere to start",width/2,200,arcade.csscolor.DIM_GRAY,15, anchor_x="center")

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        gamescreenn = gamescreen()
        gamescreenn.setup()
        self.window.show_view(gamescreenn)

class gamescreen(arcade.View):
    def __init__(self):
        super().__init__()

        self.physics = None

        self.hitcoins = None
        self.hittraps = None

        self.rghtclick = None
        self.leftclick = None
        self.upclick = None
        self.downclick = None
        self.score = 0

        self.players = None
        self.player = None

        self.tabrak_collition = None

        self.collect = None

        self.view_left = 0
        self.view_bottom = 0
        self.camera_sprites = arcade.Camera(width, height)
        self.camera_gui = arcade.Camera(width, height)

    def setup(self):

        self.tileMap = arcade.load_tilemap('personal_project_map.json',scaling= 3)
        self.barier = self.tileMap.sprite_lists['barier']
        self.floor = self.tileMap.sprite_lists["Floor"]
        self.floor2= self.tileMap.sprite_lists["floor2"]
        self.floor3= self.tileMap.sprite_lists["floor3"]
        self.decor= self.tileMap.sprite_lists["decor1"]
        self.wall= self.tileMap.sprite_lists["wall"]
        self.building= self.tileMap.sprite_lists["buildings"]
        self.building2= self.tileMap.sprite_lists["bulding2"]
        self.item= self.tileMap.sprite_lists["item"]
        self.door= self.tileMap.sprite_lists["door"]


        self.players = arcade.SpriteList()

        self.player = playercharacter()


        self.player.center_x = width // 2
        self.player.center_y = height // 2
        #self.scale = 0.2

        self.players.append(self.player)

        self.tabrak_collition = arcade.PhysicsEngineSimple(self.player,[self.barier,self.decor])

    def on_update(self, delta_time):

        self.tabrak_collition.update()
        self.players.update()
        self.players.update_animation()
        self.player.change_x = 0
        self.player.change_y = 0
        self.scroll_to_player()




        if self.leftclick:
            self.player.change_x = - speedofcharacter
        if self.rghtclick:
            self.player.change_x = + speedofcharacter
        if self.upclick:
            self.player.change_y = + speedofcharacter
        if self.downclick:
            self.player.change_y = - speedofcharacter
        if self.collect:
            hitcoin = arcade.check_for_collision_with_list(self.player, self.item)

            # if hitcoin:
            #     for coin in hitcoin:
            #         coin.remove_from_sprite_lists()
            #         self.score += 1
            #
            #         arcade.play_sound(self.ite)

    def scroll_to_player(self):
        """
        Scroll the window to the player.
        This method will attempt to keep the player at least VIEWPORT_MARGIN
        pixels away from the edge.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        # --- Manage Scrolling ---

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player.left < left_boundary:
            self.view_left -= left_boundary - self.player.left

        # Scroll right
        right_boundary = self.view_left + width - VIEWPORT_MARGIN
        if self.player.right > right_boundary:
            self.view_left += self.player.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + height - VIEWPORT_MARGIN
        if self.player.top > top_boundary:
            self.view_bottom += self.player.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player.bottom

        # Scroll to the proper location
        position = self.view_left, self.view_bottom
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width1, height1):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width1), int(height1))
        self.camera_gui.resize(int(width1), int(height1))







    def on_draw(self):
        self.clear()
        self.camera_sprites.use()
        self.barier.draw()
        self.floor.draw()
        self.floor2.draw()
        self.floor3.draw()
        self.decor.draw()
        self.wall.draw()
        self.building.draw()
        self.building2.draw()
        self.item.draw()
        self.door.draw()
        self.players.draw()
        text = f"Score = {self.score}"
        arcade.draw_text(text, 50, 28, arcade.csscolor.WHITE, 20)

        self.camera_gui.use()
        left_boundary = VIEWPORT_MARGIN
        right_boundary = width - VIEWPORT_MARGIN
        top_boundary = height - VIEWPORT_MARGIN
        bottom_boundary = VIEWPORT_MARGIN
        arcade.draw_lrtb_rectangle_outline(left_boundary, right_boundary, top_boundary, bottom_boundary,
                                           arcade.color.RED, 2)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))



    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.A:
            self.leftclick = True
        elif key == arcade.key.D:
            self.rghtclick = True
        elif key == arcade.key.W:
            self.upclick = True
        elif key == arcade.key.S:
            self.downclick = True
        elif key ==arcade.key.Q:
            self.collect = True

    def on_key_release(self, key, modifiers: int):
        if key == arcade.key.A:
            self.leftclick = False
        elif key == arcade.key.D:
            self.rghtclick = False
        elif key == arcade.key.W:
            self.upclick= False
        elif key == arcade.key.S:
            self.downclick = False
        elif key == arcade.key.Q:
            self.collect = False


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        gameover = gameoverscreen()
        self.window.show_view(gameover)





class pausescreen(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.logo = arcade.load_texture("../Lesson 12/logo2.png")

    def on_show(self):

        arcade.set_background_color(arcade.color.BANANA_YELLOW)

    def on_draw(self):
        self.clear()
        # arcade.draw_texture_rectangle(width/2,350,250,100,self.logo)
        arcade.draw_text("Game is being paused.", width / 2, 300, arcade.csscolor.BLACK, 30, anchor_x="center",font_name="Papyrus")
        arcade.draw_text("Click here to start", width / 2, 200, arcade.csscolor.DIM_GRAY, 15, anchor_x="center")
        #arcade.draw_text("Click here to quit game", width / 2, 100, arcade.csscolor.DIM_GRAY, 15, anchor_x="center")

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        gameover = gameoverscreen()
        self.window.show_view(gameover)

class gameoverscreen(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.logo = arcade.load_texture("../Lesson 12/logo2.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.RED_DEVIL)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.R:
            self.window.show_view(pausescreen())
        elif key == arcade.key.Q:
            arcade.close_window()



    def on_draw(self):
        self.clear()
        #arcade.draw_texture_rectangle(width/2,350,250,100,self.logo)
        arcade.draw_text("Game Over",width/2,300,arcade.csscolor.BLACK,30,anchor_x= "center",font_name="Lucida Handwriting")
        arcade.draw_text("Click 'R' to restart, Click 'Q' to quit game.",width/2,200,arcade.csscolor.DIM_GRAY,15, anchor_x="center")
        #arcade.draw_text("Click here to quit game",width/2,100,arcade.csscolor.DIM_GRAY,15, anchor_x="center")




def main():
    window = arcade.Window(width,height,"Welcome screen")
    gameon = Startscreen()
    gameon.setup()
    window.show_view(gameon)
    arcade.run()

main()

