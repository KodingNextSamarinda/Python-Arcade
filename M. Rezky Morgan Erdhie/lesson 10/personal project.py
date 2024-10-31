import arcade
import time

gridSize = 70
widthMap = 18 * gridSize
heightMap = 10 * gridSize
title = "Map level 2"
Speed= 2
jump = 7


class level1(arcade.Window):
    def __init__(self):
        super().__init__(widthMap,heightMap,title)

        self.ground = None
        self.foreground = None
        self.decoration = None
        self.bg_image = None
        self.border = None


        self.level1 = None

        self.player = None

        self.physics_engine = None
        self.bardor = None

        self.right_pressed = None
        self.left_pressed = None

        self.score = 0

        self.killl =arcade.load_sound('asset/kills.mp3')
        self.coinss = arcade.load_sound('asset/coinns.mp3')

    def setup(self):

        self.level1 = arcade.load_tilemap("asset/map2.json",scaling=0.55)

        self.ground = self.level1.sprite_lists["ground"]
        self.foreground = self.level1.sprite_lists["foreground"]
        self.decoration = self.level1.sprite_lists["decoration"]
        self.bg_image = self.level1.sprite_lists["bg_image"]
        self.border = self.level1.sprite_lists["border"]
        self.obstacle = self.level1.sprite_lists["obstacle"]
        self.coins = self.level1.sprite_lists["coins"]

        self.player = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png",scale=0.6)
        self.player.center_x = 40
        self.player.center_y = heightMap / 2

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.ground)

        self.bardor = arcade.PhysicsEngineSimple(self.player, self.border)






    def on_draw(self):
        arcade.start_render()
        self.bg_image.draw()
        self.foreground.draw()
        self.ground.draw()
        self.decoration.draw()
        self.obstacle.draw()
        self.player.draw()
        self.coins.draw()
        text_score = f"coins colleted = {self.score}"
        arcade.draw_text(text_score, 10, 570, color=arcade.color.AMETHYST)
        arcade.draw_rectangle_filled(10, 570, 20, 15, color=arcade.color.DARK_SKY_BLUE)




    def on_update(self, delta_time: float):
        self.player.update()
        self.physics_engine.update()
        self.bardor.update()
        if arcade.check_for_collision_with_list(self.player, self.obstacle):
            arcade.play_sound(self.killl)
            time.sleep(1)
            self.close()         



    def update(self, delta_time: float):

        self.coins.update()
        coin_touched = arcade.check_for_collision_with_list(self.player, self.coins)
        for coins in coin_touched:
            coins.remove_from_sprite_lists()
            arcade.play_sound(self.coinss)
            self.score += 10

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x = Speed
        elif symbol == arcade.key.LEFT:
            self.player.change_x = -Speed
        elif symbol == arcade.key.UP or symbol == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player.change_y = jump

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 0
        elif symbol == arcade.key.LEFT:
            self.player.change_x = 0



playMap = level1()
playMap.setup()
playMap.run()




