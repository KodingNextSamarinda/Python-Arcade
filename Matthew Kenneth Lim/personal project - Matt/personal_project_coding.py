import arcade
import arcade.gui
from players import PlayerCharacter

height = 16 * 25 * 2
width =  16 * 35 * 2
speedofcharacter = 3.5
# Margins for scrolling
VIEWPORT_MARGIN = 400

CAMERA_SPEED = 0.5
score = 0
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
        self.inside = None
        self.score = score


        self.rghtclick = None
        self.leftclick = None
        self.upclick = None
        self.downclick = None

        self.players = None
        self.player = None

        self.tabrak_collition = None

        self.collect = None

        self.masuk = None

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

        self.player = PlayerCharacter()


        self.player.center_x = width // 2
        self.player.center_y = height // 2
        self.scale = 0.5

        self.players.append(self.player)

        self.tabrak_collition = arcade.PhysicsEngineSimple(self.player,[self.barier, self.decor,self.building,self.building2,self.wall])





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

        hitcoin = arcade.check_for_collision_with_list(self.player, self.item)

        if hitcoin:
            for coin in hitcoin:
                coin.remove_from_sprite_lists()
                self.score += 1

        if self.score == 10:
            gameover = gameoverscreen()
            gameover.setup()
            self.window.show_view(gameover)


        inside = arcade.check_for_collision_with_list(self.player,self.door)

        if inside:
            indoor = indoorscreen()
            indoor.setup()
            self.window.show_view(indoor)

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

        self.camera_gui.use()


        text = f"Flowers collected = {self.score}"
        arcade.draw_text(text, 100, 100, arcade.color.BLACK_BEAN, 20)

        self.camera_gui.use()
        left_boundary = VIEWPORT_MARGIN
        right_boundary = width - VIEWPORT_MARGIN
        top_boundary = height - VIEWPORT_MARGIN
        bottom_boundary = VIEWPORT_MARGIN


    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))



    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.LEFT:
            self.leftclick = True
        elif key == arcade.key.RIGHT:
            self.rghtclick = True
        elif key == arcade.key.UP:
            self.upclick = True
        elif key == arcade.key.DOWN:
            self.downclick = True
        elif key ==arcade.key.Q:
            self.collect = True

    def on_key_release(self, key, modifiers: int):
        if key == arcade.key.LEFT:
            self.leftclick = False
        elif key == arcade.key.RIGHT:
            self.rghtclick = False
        elif key == arcade.key.UP:
            self.upclick= False
        elif key == arcade.key.DOWN:
            self.downclick = False
        elif key == arcade.key.Q:
            self.collect = False






class indoorscreen(arcade.View):
    def __init__(self):
        super().__init__()

        def __init__(self):
            super().__init__()

            self.physics = None
            self.score = score
            self.hitcoins = None
            self.hittraps = None

            self.rghtclick = None
            self.leftclick = None
            self.upclick = None
            self.downclick = None

            self.players = None
            self.player = None

            self.tabrak_collition = None

            self.collect = None



    def setup(self):

        self.tileMap = arcade.load_tilemap('interiormap.json', scaling=3)
        self.decor = self.tileMap.sprite_lists['decor']
        self.out = self.tileMap.sprite_lists['out']
        self.decor1 = self.tileMap.sprite_lists['decor1']
        self.wall = self.tileMap.sprite_lists['wall']
        self.floor = self.tileMap.sprite_lists['floor']


        self.players = arcade.SpriteList()

        self.player = PlayerCharacter()

        self.player.center_x = width // 2
        self.player.center_y = height // 2
        self.scale = 0.5

        self.players.append(self.player)

        self.tabrak_collition = arcade.PhysicsEngineSimple(self.player, [self.wall])

    def on_update(self, delta_time):

        self.tabrak_collition.update()
        self.players.update()
        self.players.update_animation()
        self.player.change_x = 0
        self.player.change_y = 0


        if self.leftclick:
            self.player.change_x = - speedofcharacter
        if self.rghtclick:
            self.player.change_x = + speedofcharacter
        if self.upclick:
            self.player.change_y = + speedofcharacter
        if self.downclick:
            self.player.change_y = - speedofcharacter

        hitcoin = arcade.check_for_collision_with_list(self.player, self.item)

        if hitcoin:
            for coin in hitcoin:
                coin.remove_from_sprite_lists()
                self.score += 1

        arcade.play_sound(self.item)
        if self.score == 10:
            gameover = gameoverscreen()
            gameover.setup()
            self.window.show_view(gameover)



    def on_draw(self):
        self.clear()
        self.decor.draw()
        self.out.draw()
        self.decor1.draw()
        self.wall.draw()
        self.floor.draw()

        self.players.draw()
        text = f"Score = {self.score}/10"
        arcade.draw_text(text, 50, 28, arcade.csscolor.WHITE, 20)





    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.LEFT:
            self.leftclick = True
        elif key == arcade.key.RIGHT:
            self.rghtclick = True
        elif key == arcade.key.UP:
            self.upclick = True
        elif key == arcade.key.DOWN:
            self.downclick = True
        elif key == arcade.key.Q:
            self.collect = True

    def on_key_release(self, key, modifiers: int):
        if key == arcade.key.LEFT:
            self.leftclick = False
        elif key == arcade.key.RIGHT:
            self.rghtclick = False
        elif key == arcade.key.UP:
            self.upclick = False
        elif key == arcade.key.DOWN:
            self.downclick = False
        elif key == arcade.key.Q:
            self.collect = False



class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class gameoverscreen(arcade.View):
    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box))

    def setup(self):
        self.logo = arcade.load_texture("../Lesson 12/logo2.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.YELLOW)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.Q:
            arcade.close_window()



    def on_draw(self):
        self.clear()
        #arcade.draw_texture_rectangle(width/2,350,250,100,self.logo)
        arcade.draw_text("Quest Complete",width/2,300,arcade.csscolor.BLACK,30,anchor_x= "center",font_name="Lucida Handwriting")
        arcade.draw_text("Press 'Q' to quit game.",width/2,200,arcade.csscolor.DIM_GRAY,15, anchor_x="center")
        #arcade.draw_text("Click here to quit game",width/2,100,arcade.csscolor.DIM_GRAY,15, anchor_x="center")
        self.manager.draw()







def main():
    window = arcade.Window(width,height,"Welcome screen")
    gameon = Startscreen()
    gameon.setup()
    window.show_view(gameon)
    arcade.run()

main()
