import arcade
import arcade.gui
from Players import PlayerCharacter

tileSize = 16
width = 30 * 16 * 2
height = 25 * 16 * 2
MovementSpeed = 3
title = "Hello"

# Margins for scrolling
VIEWPORT_MARGIN = 300

CAMERA_SPEED = 0.5

sound = arcade.load_sound("Assets/Kawaii White Lion.mp3")
play_bs = arcade.play_sound(sound, volume=0.2, looping=True)

class StartScreen(arcade.View):
    def __init__(self):
        super().__init__()

    def __init__(self):
        super().__init__()

    def setup(self):
        self.image = arcade.load_texture("Assets/Montgomery.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.CYAN)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(width/2, (height/2)+100, 150, 100, texture=self.image)
        arcade.draw_text("Welcome to the diamond mine.",width/2, (height/2)-70, arcade.color.WHITE,
                         font_size=25, font_name="Arial", anchor_x="center")
        arcade.draw_text("Press Here to Start Collecting Diamonds.", width / 2, (height / 2) - 120,
                         arcade.color.WHITE, font_size=14, font_name="Arial", anchor_x="center")

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        RuleScreen_view = RuleScreen()
        RuleScreen_view.setup()
        self.window.show_view(RuleScreen_view)

class RuleScreen(arcade.View):
    def __init__(self):
        super().__init__()

    def __init__(self):
        super().__init__()

    def setup(self):
        self.image = arcade.load_texture("Assets/Diamond.png.")

    def on_show(self):
        arcade.set_background_color(arcade.color.CYAN)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(width/2, (height/2)+100, 150, 100, texture=self.image)
        arcade.draw_text("The evil dark lord has died of cholera. His will has left a rain of diamonds.",
                         width/2, (height/2)- 25, arcade.color.WHITE, font_size=18, font_name="Arial", anchor_x="center")
        arcade.draw_text("Collect all the diamonds to become the richest man on the world.",
                         width / 2, (height /3) - 27, arcade.color.WHITE, font_size=18, font_name="Arial",
                         anchor_x="center")
        arcade.draw_text("Don't press the F button Please, just don't. Don't do it. Don't.",
                         width / 2, (height /4) - 28, arcade.color.WHITE, font_size=18, font_name="Arial",
                         anchor_x="center")
        arcade.draw_text("Get out there and have some fun. :)",
                         width / 2, (height /5) - 29, arcade.color.WHITE, font_size=18, font_name="Arial",
                         anchor_x="center")

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        game_screen_view = GameScreen()
        game_screen_view.setup()
        self.window.show_view(game_screen_view)

class GameScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.Ground = None
        self.Wall = None
        self.Bonus = None
        self.Secret = None
        self.gameMaps = None
        self.player = None
        self.players = None

        self.Left_pressed = None
        self.Right_pressed = None
        self.Up_pressed = None
        self.Down_pressed = None

        self.view_left = 0
        self.view_bottom = 0
        self.camera_sprites = arcade.Camera(width, height)
        self.camera_gui = arcade.Camera(width, height)


    def setup(self):
        self.gameMaps = arcade.load_tilemap("JustinBieberOneTime_1.json", scaling=0.6)
        self.Ground = self.gameMaps.sprite_lists["Ground"]
        self.Wall = self.gameMaps.sprite_lists["Wall"]
        self.Bonus = self.gameMaps.sprite_lists["Bonus"]
        self.Secret = self.gameMaps.sprite_lists["Secret"]

        self.players = arcade.SpriteList()
        self.player = PlayerCharacter()
        self.player.center_x = width // 2
        self.player.center_y = height // 2
        #self.player.scale = 0.2

        self.players.append(self.player)

    def on_update(self, delta_time: float):
        self.players.update()
        self.players.update_animation()
        self.player.change_x = 0
        self.player.change_y = 0

        collide_secret = arcade.check_for_collision_with_list(self.player, self.Secret)

        if collide_secret:
            next = GameScreen_Baby()
            next.setup()
            self.window.show_view(next)


        colide_bonus = arcade.check_for_collision_with_list(self.player, self.Bonus)
        if colide_bonus:
            for item in colide_bonus:
                item.remove_from_sprite_lists()



        if self.Left_pressed == True and not self.Right_pressed:
            self.player.change_x = -MovementSpeed

        elif self.Right_pressed == True and not self.Left_pressed:
            self.player.change_x = MovementSpeed

        elif self.Up_pressed == True and not self.Down_pressed:
            self.player.change_y = MovementSpeed

        elif self.Down_pressed == True and not self.Up_pressed:
            self.player.change_y = -MovementSpeed

        else:
            self.player.change_x = 0
            self.player.change_y = 0
        self.scroll_to_player()

    def scroll_to_player(self):

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
        self.camera_sprites.move_to((self.view_left, self.view_bottom), CAMERA_SPEED)


    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.Left_pressed = True

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.Right_pressed = True

        elif key == arcade.key.UP or key == arcade.key.W:
            self.Up_pressed = True

        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.Down_pressed = True

        if key == arcade.key.F:
            over = GameOver()
            over.setup()

            self.window.show_view(over)

        elif key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, key, modifiers: int):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.Left_pressed = False

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.Right_pressed = False

        elif key == arcade.key.UP or key == arcade.key.W:
            self.Up_pressed = False

        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.Down_pressed = False

    def on_draw(self):
        self.clear()
        self.camera_sprites.use()
        self.Ground.draw()
        self.Wall.draw()
        self.Bonus.draw()
        self.Secret.draw()
        self.player.draw()
        self.players.draw()

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



class GameScreen_Baby(arcade.View):
    def __init__(self):
        super().__init__()
        self.Ground = None
        self.Wall = None
        self.Bonus = None
        self.Secret = None
        self.Special = None
        self.Galaxy = None
        self.gameMaps = None
        self.player = None
        self.players = None
        self.score = 0
        self.specc = 0
        self.galaxx = 0

        self.Left_pressed = None
        self.Right_pressed = None
        self.Up_pressed = None
        self.Down_pressed = None

        self.view_left = 0
        self.view_bottom = 0
        self.camera_sprites = arcade.Camera(width, height)
        self.camera_gui = arcade.Camera(width, height)


    def setup(self):
        self.gameMaps = arcade.load_tilemap("JustinBieberBaby_1.json", scaling=0.6)
        self.Ground = self.gameMaps.sprite_lists["Ground"]
        self.Wall = self.gameMaps.sprite_lists["Wall"]
        self.Bonus = self.gameMaps.sprite_lists["Bonus"]
        self.Secret = self.gameMaps.sprite_lists["Secret"]
        self.Special = self.gameMaps.sprite_lists["Special"]
        self.Galaxy = self.gameMaps.sprite_lists["Galaxy"]

        self.players = arcade.SpriteList()
        self.player = PlayerCharacter()
        self.player.center_x = width // 2
        self.player.center_y = height // 2
        #self.player.scale = 0.2

        self.players.append(self.player)


    def on_update(self, delta_time: float):
        self.players.update()
        self.players.update_animation()
        self.player.change_x = 0
        self.player.change_y = 0


        colide_bonus = arcade.check_for_collision_with_list(self.player, self.Bonus)
        if colide_bonus:
            for item in colide_bonus:
                item.remove_from_sprite_lists()
                self.score += 1

        collide_spec = arcade.check_for_collision_with_list(self.player, self.Special)

        if collide_spec:
            for item in collide_spec:
                item.remove_from_sprite_lists()
                self.specc += 1

        collide_gall = arcade.check_for_collision_with_list(self.player, self.Galaxy)

        if collide_gall:
            for item in collide_gall:
                item.remove_from_sprite_lists()
                self.galaxx += 1



        if self.Left_pressed == True and not self.Right_pressed:
            self.player.change_x = -MovementSpeed

        elif self.Right_pressed == True and not self.Left_pressed:
            self.player.change_x = MovementSpeed

        elif self.Up_pressed == True and not self.Down_pressed:
            self.player.change_y = MovementSpeed

        elif self.Down_pressed == True and not self.Up_pressed:
            self.player.change_y = -MovementSpeed

        else:
            self.player.change_x = 0
            self.player.change_y = 0
        self.scroll_to_player()

        if self.score == 361 and self.specc == 12 and self.galaxx == 10:
            over = YouWin()
            over.setup()
            self.window.show_view(over)


    def scroll_to_player(self):

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
        self.camera_sprites.move_to((self.view_left, self.view_bottom), CAMERA_SPEED)


    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.Left_pressed = True

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.Right_pressed = True

        elif key == arcade.key.UP or key == arcade.key.W:
            self.Up_pressed = True

        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.Down_pressed = True

        if key == arcade.key.F:
            over = GameOver()
            over.setup()

            self.window.show_view(over)

        elif key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, key, modifiers: int):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.Left_pressed = False

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.Right_pressed = False

        elif key == arcade.key.UP or key == arcade.key.W:
            self.Up_pressed = False

        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.Down_pressed = False

    def on_draw(self):
        self.clear()
        self.camera_sprites.use()

        self.Wall.draw()
        self.Ground.draw()
        self.Secret.draw()
        self.Bonus.draw()
        self.Special.draw()
        self.Galaxy.draw()
        self.player.draw()
        self.players.draw()

        self.camera_gui.use()

        #361 #12
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



class YouWin(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.stop_sound(play_bs)

    def setup(self):
        self.image = arcade.load_texture("Assets/Why Are We Here.png")

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(width / 2, (height / 2) + 100, 150, 100, texture=self.image)
        arcade.draw_text("My brother, you have redeemed yourself by discovering countless diamonds and ores"
                         "used by the Great Dark Lord.",
                         width / 2, (height / 2) - 70, arcade.color.SKY_BLUE,
                         font_size=18, font_name="Arial", anchor_x="center")
        arcade.draw_text("Pack up your equipment. We are gonna go to crusade.", width / 2, (height / 2) - 120, arcade.color.LIGHT_BLUE,
                         font_size=14, font_name="Arial",
                         anchor_x="center")

    def __init__(self):
        super().__init__()
        self.sound = arcade.load_sound("Assets/Never Gonna Give You up in Old English.mp3")
        arcade.play_sound(self.sound, volume=0.2, looping=True)

class GameOver(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.stop_sound(play_bs)

    def setup(self):
        self.image = arcade.load_texture("Assets/Vader.png")

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(width / 2, (height / 2) + 100, 150, 100, texture=self.image)
        arcade.draw_text("Congratulations. NOW GET OUT!", width / 2, (height / 2) - 70, arcade.color.WHITE,
                         font_size=18, font_name="Arial", anchor_x="center")
        arcade.draw_text("GET OUT THERE AND TOUCH GRASS.", width / 2, (height / 2) - 120, arcade.color.WHITE,
                         font_size=14, font_name="Arial",
                         anchor_x="center")

    def __init__(self):
        super().__init__()
        self.sound = arcade.load_sound("Assets/Run.mp3")
        arcade.play_sound(self.sound, volume=0.2, looping=True)


def main():
     window = arcade.Window(width, height, title)
     start_game = StartScreen()
     start_game.setup()
     window.show_view(start_game)
     arcade.run()

main()