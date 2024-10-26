import arcade
import arcade as ar
tileSize=70
title="g"
width=20*tileSize
movement=10
JumpSpeed=15
backsound=ar.load_sound("lesson10/sounds/supermario.mp3")
height=15*tileSize
Score=0

class myMaps(arcade.Window):
    def __init__(self):
        super().__init__(width,height,title)
        self.Platform= None
        self.Decor=None
        self.Back=None
        self.Grass=None
        self.Obs=None
        self.Coins=None
        self.p_x = 200
        self.p_y = 200
        self.change_x = 0
        self.change_y = 0
        self.Score = Score
        self.physics_engine = None
        self.left_press = None
        self.right_press = None

        self.Map1=None

    def setup(self):
            self.scene = arcade.Scene()
            self.scene.add_sprite_list("Player")
            self.Map1=ar.load_tilemap("lesson10/Map1.json")
            self.Platform=self.Map1.sprite_lists["Ground"]
            self.Obs=self.Map1.sprite_lists["Obstacle"]
            self.Coins=self.Map1.sprite_lists["Coin"]
            self.Decor=self.Map1.sprite_lists["Decor"]
            self.Grass=self.Map1.sprite_lists["Grass"]
            self.Back=self.Map1.sprite_lists["Back"]

            self.player_sprite = ar.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png", 1)
            self.player_sprite.center_x = self.p_x
            self.player_sprite.center_y = self.p_y
            self.scene.add_sprite_list("Player", self.player_sprite)
            self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.Platform)
            ar.PhysicsEnginePlatformer(self.player_sprite, self.Platform)
            ar.play_sound(backsound)
    def on_draw(self):
        ar.start_render()
        self.Back.draw()
        self.Platform.draw()
        self.Decor.draw()
        self.Grass.draw()
        self.Coins.draw()
        self.Obs.draw()
        self.player_sprite.draw()
        Text = f"Score:{self.Score}"
        ar.draw_text(Text, 50, 100, ar.color.BLACK, 17)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.LEFT:
            self.left_press = True
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_press = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.LEFT:
            self.left_press = False
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_press = False
        elif key == ar.key.UP or key == ar.key.SPACE:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JumpSpeed
                jumpsound = ar.load_sound("lesson10/jump.wav")
                ar.play_sound(jumpsound)

    def on_update(self, delta_time):
        self.physics_engine.update()

        if self.left_press == True and not self.right_press == True:
            self.player_sprite.change_x = -movement
        elif self.right_press == True and not self.left_press == True:
            self.player_sprite.change_x = movement
        else:
            self.player_sprite.change_x = 0

        hit_coin = arcade.check_for_collision_with_list(self.player_sprite, self.Coins)
        for Coins in hit_coin:
            Coins.remove_from_sprite_lists()
            self.Score += 1
        hit_obs = ar.check_for_collision_with_list(self.player_sprite, self.Obs)
        if hit_obs:
            self.player_sprite.center_x = 10000
            self.player_sprite.center_y = 10000





map1=myMaps()
map1.setup()
ar.run()