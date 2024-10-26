import arcade
pixeltilesize = 105

screenwidth = 12 * pixeltilesize
screenheight = 9 * pixeltilesize
speedofcharacter = 9

class Projectmap(arcade.Window):
    def __init__(self):
        super().__init__(screenwidth,screenheight,"Escape The Industry")

        self.bg = None
        self.ground = None
        self.obstacle = None
        self.decor = None
        self.player = None
        self.coin = None

        self.tileMap = None
        self.physics = None

        self.hitcoins = None
        self.hittraps = None

        self.rghtclick = None
        self.leftclick = None
        self.jump = None
        self.score = 0

    def setup(self):

        self.tileMap = arcade.load_tilemap("Personal project map.json")
        self.bg = self.tileMap.sprite_lists["Background"]
        self.ground = self.tileMap.sprite_lists["Ground"]
        self.obstacle = self.tileMap.sprite_lists["Traps"]
        self.coin = self.tileMap.sprite_lists["Coins"]
        self.decor = self.tileMap.sprite_lists["Decor"]

        self.player = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png")
        self.player.center_x = screenwidth / 2
        self.player.center_y = screenheight / 2

        self.physic = arcade.PhysicsEnginePlatformer(
            self.player,
            self.ground,

        )

    def on_update(self, delta_time):
        if self.leftclick and not self.rghtclick:
            self.player.change_x = -speedofcharacter
        elif self.rghtclick and not self.leftclick:
            self.player.change_x = speedofcharacter
        else:
            self.player.change_x = 0

        self.physic.update()

        hitcoin = arcade.check_for_collision_with_list(self.player, self.coin)
        hitobstacle = arcade.check_for_collision_with_list(self.player, self.obstacle)

        if hitcoin:
            for coin in hitcoin:
                coin.remove_from_sprite_lists()
                self.score += 1


        if hitobstacle:
            self.player.center_x = 100000
            self.player.center_y = 100000
            self.score = 0




    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.LEFT:
            self.leftclick = True
        elif key == arcade.key.RIGHT:
            self.rghtclick = True
        elif key == arcade.key.SPACE:
            if self.physic.can_jump():
                self.player.change_y = 30

    def on_key_release(self, key, modifiers: int):
        if key == arcade.key.LEFT:
            self.leftclick = False
        elif key == arcade.key.RIGHT:
            self.rghtclick = False



    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        self.ground.draw()
        self.obstacle.draw()
        self.coin.draw()
        self.player.draw()
        self.decor.draw()
        text = f"Score = {self.score}"
        arcade.draw_text(text, 100, 200, arcade.csscolor.WHITE, 20)


arena1 = Projectmap()

arena1.setup()
arcade.run()

