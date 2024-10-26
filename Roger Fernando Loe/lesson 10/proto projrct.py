import arcade

Tile_size = 70

movementspeed = 5
jumpspeed = 10

Widthscreen = 15 * Tile_size
Heightscreen = 10 * Tile_size
title = "map1 -- Journey 1"

class mymap(arcade.Window) :

    def __init__(self):
        super().__init__(Widthscreen,Heightscreen,title)
        self.background = None
        self.ground = None
        self.decor = None
        self.obstacle = None
        self.map1 = None
        self.score = 0

        self.player = None

        self.physicsEngine = None

        self.colitionBox = None

        self.leftpress = None
        self.rightpress = None

        #self.bg_sound = arcade.load_sound("sounds/supermario.mp3")
        #self.play_bgsound = arcade.play_sound(self.bg_sound)


    def setup(self):

        self.map1 = arcade.load_tilemap("Tilemap.json")

        self.background = self.map1.sprite_lists["background"]
        self.ground = self.map1.sprite_lists["ground"]
        self.decor = self.map1.sprite_lists["decor"]
        self.obstacle = self.map1.sprite_lists["obstacle"]
        self.COIN = self.map1.sprite_lists["COIN"]


        self.player = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png", 0.5)
        self.player.center_x = 2 * Tile_size
        self.player.center_y = 5 * Tile_size

        self.physicsEngine = arcade.PhysicsEnginePlatformer(self.player, self.ground)



    def on_update(self, delta_time: float):
        if self.leftpress == True and not self.rightpress :
            self.player.change_x = -movementspeed

        elif self.rightpress == True and not self.leftpress :
            self.player.change_x = +movementspeed
        else :
            self.player.change_x = 0

        self.physicsEngine.update()

        coinget = arcade.check_for_collision_with_list(self.player, self.COIN)

        for i in coinget :
            i.remove_from_sprite_lists()
            self.score

        obstaclehit = arcade.check_for_collision_with_list(self.player, self.obstacle)

        if obstaclehit :
            self.player.center_x = 1000000
            self.player.center_y = -1000


    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.LEFT :
            self.leftpress = True

        elif key == arcade.key.RIGHT :
            self.rightpress = True

        elif key == arcade.key.UP:
            if self.physicsEngine.can_jump():
                self.player.change_y = jumpspeed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT :
            self.leftpress = False

        elif key == arcade.key.RIGHT :
            self.rightpress = False

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.decor.draw()
        self.obstacle.draw()
        self.ground.draw()
        self.player.draw()
        self.COIN.draw()


        output = f"score : {self.score}"
        arcade.draw_text(output, 20, 40, arcade.color.WHITE, 15)

map1 = mymap()
map1.setup()
arcade.run()