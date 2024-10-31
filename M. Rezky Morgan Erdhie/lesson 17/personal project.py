import arcade
from players import PlayerCharacter
width = 16 * 30 * 2
height = 16 * 20 * 2
title = "game"

movement = 0.55


class StartScreen(arcade.View):

    def __init__(self):
        super().__init__()
        self.bg_sound = arcade.load_sound("asset/music.mp3")
        arcade.play_sound(self.bg_sound, volume=0.8, looping=True, speed=1.0)
        self.title = None

    def setup(self):
        self.title = arcade.load_texture("asset/chicken.jpg")

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_SKY_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(480,500,250,200, self.title)
        arcade.draw_text("Chicken Hunt", width / 2, height / 2, arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Click To Continue", width / 2, height / 2 - 55, arcade.color.WHITE, font_size=13,
                         anchor_x="center")


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == 1:
            window = GameScreen()
            window.setup()

            game.show_view(window)

class Gamescreeninterior(arcade.View):
    def __init__(self):
        super().__init__()
        self.mapinterior = None
        self.exit = None
        self.door2 = None
        self.wall2 = None
        self.decoration2 = None
        self.floor2 = None

    def setup(self):
        self.mapinterior = arcade.load_tilemap("asset/interior.json",scaling=2)
        print(self.mapinterior.sprite_lists.keys())  # This will list all available keys
        self.exit = self.mapinterior.sprite_lists["exit"]
        self.door2 = self.mapinterior.sprite_lists["door"]
        self.wall2 = self.mapinterior.sprite_lists["wall"]
        self.decoration2 = self.mapinterior.sprite_lists["decoration"]
        self.floor2 = self.mapinterior.sprite_lists["floor"]

        self.players = arcade.SpriteList()
        self.player = PlayerCharacter()

        self.player.center_x = 300
        self.player.center_y = 300

        self.players.append(self.player)

        self.tembok = arcade.PhysicsEngineSimple(self.player,self.wall2)

    def on_draw(self):
        self.clear()
        self.floor2.draw()
        self.door2.draw()
        self.wall2.draw()
        self.decoration2.draw()
        self.players.draw()

    def on_update(self, delta_time: float):
        self.players.update()
        self.players.update_animation()
        self.player.update()

        collide_door = arcade.check_for_collision_with_list(self.player, self.door2)
        if collide_door:

            Gameview = GameScreen()
            Gameview.setup()
            self.window.show_view(Gameview)







    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:

            window = GameOverScreen()

            game.show_view(window)

        elif symbol == arcade.key.W:
            self.player.change_y = +movement
        elif symbol == arcade.key.S:
            self.player.change_y = -movement
        elif symbol == arcade.key.D:
            self.player.change_x = +movement
        elif symbol == arcade.key.A:
            self.player.change_x = -movement
        elif symbol == arcade.key.F:
            self.trigger =  True
    def on_key_release(self, symbol: int, _modifiers: int):
        if symbol == arcade.key.W:
            self.player.change_y = 0
        elif symbol == arcade.key.S:
            self.player.change_y = 0
        elif symbol == arcade.key.D:
            self.player.change_x = 0
        elif symbol == arcade.key.A:
            self.player.change_x = 0
        elif symbol == arcade.key.F:
            self.trigger = False






class GameScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.map = None
        self.colletibles = None
        self.wall = None
        self.decoration = None
        self.house = None
        self.fences = None
        self.door = None

        self.floor = None

        self.score = 0

        self.trigger = False

        self.player = None
        self.players = None

    def setup(self):
        self.map = arcade.load_tilemap("asset/map_outdoor.json", scaling= 2)
        print(self.map.sprite_lists.keys())  # This will list all available keys

        self.colletibles = self.map.sprite_lists["colletibles"]
        self.wall = self.map.sprite_lists["wall"]
        self.decoration = self.map.sprite_lists["decoration"]
        self.house = self.map.sprite_lists["house"]
        self.fences = self.map.sprite_lists["fences"]
        self.border = self.map.sprite_lists["border"]
        self.door = self.map.sprite_lists["door"]

        self.floor = self.map.sprite_lists["floor"]

        self.players = arcade.SpriteList()
        self.player = PlayerCharacter()

        self.player.center_x = 300
        self.player.center_y = 300

        self.players.append(self.player)

        self.penghalang = arcade.PhysicsEngineSimple(self.player, self.fences)
        self.rumah = arcade.PhysicsEngineSimple(self.player, self.house)
        self.tembok = arcade.PhysicsEngineSimple(self.player,self.wall)
        self.bardor = arcade.PhysicsEngineSimple(self.player,self.border)


    def on_draw(self):
        self.clear()
        self.floor.draw()
        self.colletibles.draw()
        self.fences.draw()
        self.house.draw()
        self.decoration.draw()
        self.wall.draw()

        text_score = f"chicken collected = {self.score}"
        arcade.draw_text(text_score, 10, 570, color=arcade.color.WHITE)





        self.players.draw()

    def on_update(self, delta_time: float):
        self.players.update()
        self.players.update_animation()
        self.player.update()
        self.penghalang.update()
        self.rumah.update()
        self.tembok.update()
        self.floor.update()
        self.bardor.update()
        collect = arcade.check_for_collision_with_list(self.player, self.colletibles)
        if collect and self.trigger == True:
            for each_item in collect:
                each_item.remove_from_sprite_lists()
                self.score += 1

        collide_door = arcade.check_for_collision_with_list(self.player,self.door)

        if collide_door:
            print("door get touched")
            Gameview = Gamescreeninterior()
            Gameview.setup()
            self.window.show_view(Gameview)



    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:

            window = GameOverScreen()

            game.show_view(window)

        elif symbol == arcade.key.W:
            self.player.change_y = +movement
        elif symbol == arcade.key.S:
            self.player.change_y = -movement
        elif symbol == arcade.key.D:
            self.player.change_x = +movement
        elif symbol == arcade.key.A:
            self.player.change_x = -movement
        elif symbol == arcade.key.F:
            self.trigger =  True
    def on_key_release(self, symbol: int, _modifiers: int):
        if symbol == arcade.key.W:
            self.player.change_y = 0
        elif symbol == arcade.key.S:
            self.player.change_y = 0
        elif symbol == arcade.key.D:
            self.player.change_x = 0
        elif symbol == arcade.key.A:
            self.player.change_x = 0
        elif symbol == arcade.key.F:
            self.trigger = False



class GameOverScreen(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLUE_VIOLET)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game Over", width / 2, height / 2, arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Do you want to restart?", width / 2, height / 2 - 55, arcade.color.WHITE, font_size=13,
                         anchor_x="center")
        arcade.draw_text("Type R to restart or Q to quit", width / 2, height / 2 - 35, arcade.color.WHITE, font_size=13,
                         anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            window = GameScreen()
            game.show_view(window)
        elif symbol == arcade.key.Q:
            window = confirmationScreen()
            game.show_view(window)


class confirmationScreen(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def __init__(self):
        super().__init__()

        self.map = None

        self.wall = None
        self.decoration = None
        self.house = None
        self.fences = None
        self.floor = None

    def setup(self):

        self.map = arcade.load_tilemap("asset/mappp.json")

        self.wall = self.map.sprite_lists["wall"]
        self.decoration = self.map.sprite_lists["decoration"]
        self.house = self.map.sprite_lists["house"]
        self.fences = self.map.sprite_lists["fences"]
        self.floor = self.map.sprite_lists["floor"]

    def on_draw(self):
        self.clear()
        arcade.draw_text("Confirmation", width / 2, height / 2, arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("do you want to quint press Y to quit or N to back", width / 2, height / 2 - 55,
                         arcade.color.WHITE, font_size=13, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Y:
            arcade.close_window()
        elif symbol == arcade.key.N:
            window = GameOverScreen()
            game.show_view(window)


game = arcade.Window(width, height, title)
window = StartScreen()
window.setup()
game.show_view(window)

arcade.run()




