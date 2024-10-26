import arcade
from player2 import PlayerCharacter

tilesize = 16
width = 30 * tilesize * 2
height = 20 * tilesize * 2

title = "start my game"

movementspeed  = 5

class startscreens(arcade.View):
    def __init__(self):
        super().__init__()
        self.sound = arcade.load_sound("HarvestOstt.mp3")
        arcade.play_sound(self.sound,volume=0.2,looping=True)

    def setup(self):
        self.logo = arcade.load_texture("logo.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_SKY_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("harvest farming",width/2,height/4,arcade.color.BEIGE, anchor_x="center")
        arcade.draw_texture_rectangle(width/2,400,250,200,self.logo)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        game_on = GameScreen()
        game_on.setup()
        self.window.show_view(game_on)



class GameScreen(arcade.View):

    def __init__(self):
        super().__init__()
        self.COLLECT = None
        self.out_into = None
        self.Roof_object = None
        self.things = None
        self.objects = None
        self.Ground_overlay = None
        self.Ground_terrain = None
        self.gameMaps = None


        self.player = None
        self.players = None

        self.left_press = None
        self.right_press = None
        self.up_press = None
        self.down_press = None



    def setup(self):
        self.gameMaps = arcade.load_tilemap("sample_map_roger.json", scaling = 0.1)
        print(self.gameMaps)
        self.COLLECT = self.gameMaps.sprite_lists['COLLECT']
        self.out_into = self.gameMaps.sprite_lists['out_into']
        self.Roof_object = self.gameMaps.sprite_lists['Roof_object']
        self.things = self.gameMaps.sprite_lists['things']
        self.Objects = self.gameMaps.sprite_lists['Objects']
        self.Ground_overlay = self.gameMaps.sprite_lists['Ground_overlay']
        self.Ground_terrain = self.gameMaps.sprite_lists['Ground_terrain']

        self.players = arcade.SpriteList()

        self.player = PlayerCharacter()
        self.player.center_x = width // 2
        self.player.center_y = height // 2
        self.player.scale = 0.3

        self.players.append(self.player)

    def on_update(self, delta_time: float):
        self.players.update()
        self.players.update_animation()

        self.player.change_x = 0
        self.player.center_y = 0

        if self.left_press:
            self.player.change_x = - movementspeed
        if self.right_press:
            self.player.change_x =  movementspeed
        if self.up_press:
            self.player.change_y =  movementspeed
        if self.down_press:
            self.player.change_y = - movementspeed

        collide_door = arcade.check_for_collision_with_list(
            self.player,
            self.out_into
        )

        if collide_door:
            Gameview = GameScreen2()
            Gameview.setup()
            self.window.show_view(Gameview)

    def on_draw(self):
        self.clear()
        #self.camera_sprites.use()
        self.COLLECT.draw()
        self.out_into.draw()
        self.Roof_object.draw()
        self.things.draw()
        self.Objects.draw()
        self.Ground_overlay.draw()
        self.Ground_terrain.draw()
        self.players.draw()

        #self.camera_gui.use()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_press = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_press_press = True
        elif key == arcade.key.UP or key == arcade.key.W:
            self.up_press = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_press = True






class GameScreen2(arcade.View):

    def __init__(self):
        super().__init__()
        self.FLOOR = None
        self.painting = None
        self.window = None
        self.kitchen_hangin_decor = None
        self.bed = None
        self.decor = None
        self.carpet = None
        self.water = None
        self.wall = None
        self.out_in = None
        self.FLOOR = None
        self.gameMaps = None

        self.player = None
        self.players = None

        self.left_press = None
        self.right_press = None
        self.up_press = None
        self.down_press = None

    def setup(self):
        self.gameMaps = arcade.load_tilemap("roger mansion 16.json", scaling=2)
        print(self.gameMaps)
        self.collect = self.gameMaps.sprite_lists['collect']
        self.painting = self.gameMaps.sprite_lists['painting']
        self.window = self.gameMaps.sprite_lists['window']
        self.kitchen_hangin_decor = self.gameMaps.sprite_lists['kitchen_hangin_decor']
        self.bed = self.gameMaps.sprite_lists['bed']
        self.decor = self.gameMaps.sprite_lists['decor']
        self.carpet = self.gameMaps.sprite_lists['carpet']
        self.water = self.gameMaps.sprite_lists['water']
        self.wall = self.gameMaps.sprite_lists['wall']==
        self.out_in = self.gameMaps.sprite_lists['out_in']
        self.FLOOR = self.gameMaps.sprite_lists['FLOOR']

        self.players = arcade.SpriteList()

        self.colitionBox = None

        self.player = PlayerCharacter()
        self.player.center_x = 500
        self.player.center_y = 500
        self.player.scale = 0.6

        self.players.append(self.player)

    def on_update(self, delta_time: float):
        self.players.update()
        self.players.update_animation()

        self.player.change_x = 0
        self.player.center_y = 0

        if self.left_press:
            self.player.change_x = - movementspeed
        if self.right_press:
            self.player.change_x = + movementspeed
        if self.up_press:
            self.player.change_y = + movementspeed
        if self.down_press:
            self.player.change_y = - movementspeed

        collide_door = arcade.check_for_collision_with_list(
            self.player,
            self.out_in
        )

        if collide_door:
            Gameview = GameScreen()
            Gameview.setup()
            self.window.show_view(Gameview)

    def on_draw(self):
        self.clear()
        self.collect.draw()
        self.painting.draw()
        self.kitchen_hangin_decor.draw()
        self.bed.draw()
        self.decor.draw()
        self.carpet.draw()
        self.water.draw()
        self.wall.draw()
        self.out_in.draw()
        self.FLOOR.draw()
        self.player.draw()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_press = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_press_press = True
        elif key == arcade.key.UP or key == arcade.key.W:
            self.up_press = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_press = True

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        game_Over = GameOver()
        self.window.show_view(game_Over)




class GameOver(arcade.View):
    def __init__(self):
        super().__init__()


    def on_draw(self):
        self.clear()
        arcade.draw_text("GAME OVER",width/2,height/2,font_size=15,anchor_x="center",color=arcade.csscolor.BEIGE)
        arcade.draw_text("Press(R) to Restart and Press (Q) to Quit",width/2,height/2 - 150,font_size=11,anchor_x="center",color=arcade.csscolor.BEIGE)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            game_on = GameScreen()
            self.window.show_view(game_on)
        elif symbol == arcade.key.Q:
            self.window.close()


def main():
    #create window size
    window = arcade.Window(width,height,title)
    #creating an object for the start screen
    game_start = startscreens()
    #creating an object for game play
    #game_on = GameScreen()
    #showing / calling in the game
    game_start.setup()
    #showing wich view
    window.show_view(game_start)

    arcade.run()

main()