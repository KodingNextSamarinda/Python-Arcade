import arcade as ar
import arcade.gui
from players import PlayerCharacter
x=30*2*16
y=20*2*16
movement=1

class StartScreen(ar.View):
    
    def __init__(self):
        super().__init__()
        self.sound = ar.load_sound("HarvestOst.mp3")


        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="How To Play", width=200)
        self.v_box.add(settings_button.with_space_around(bottom=20))



        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start

        # --- Method 3 for handling click events,
        # use a decorator to handle on_click events
        @settings_button.event("on_click")
        def on_click_settings(event):
            HTP=HTPWindow()
            self.window.show_view(HTP)
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def setup(self):
        ar.play_sound(self.sound, looping=True, volume=2.0)

    def on_click_start(self, event):
        game=GameWindow()
        game.setup()
        self.window.show_view(game)

    def on_draw(self):
        self.clear()
        self.manager.draw()
class HTPWindow(ar.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Back", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))
        start_button.on_click =  self.on_click_start
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        start=StartScreen()
        self.window.show_view(start)

    def on_draw(self):
        self.clear()
        self.manager.draw()
        ar.draw_text("WASD or Arrow Key To Move",x/2*0.75,y/2*1.25,color=ar.color.BLACK)
class GameWindow(ar.View):
    def __init__(self):
        super().__init__()

        self.Map1=None
        self.Ground=None
        self.Path=None
        self.Water=None
        self.Tent=None
        self.BHouse=None
        self.RHouse=None
        self.BigHouse=None
        self.Flower=None
        self.Tree=None
        self.Decor=None
        self.Crops=None
        self.Chicken=None
        self.Player = None
        self.Players = None
        self.left_press = None
        self.right_press = None
        self.down_press = None
        self.up_press = None
        self.physic_engine = None
    def setup(self):

        self.Map1=ar.load_tilemap("Outside.json",2)

        self.Ground=self.Map1.sprite_lists["Ground"]
        self.Path=self.Map1.sprite_lists["Path"]
        self.Water=self.Map1.sprite_lists["Water"]
        self.Tent=self.Map1.sprite_lists["Tent"]
        self.RHouse=self.Map1.sprite_lists["RHouse"]
        self.BHouse=self.Map1.sprite_lists["BHouse"]
        self.BigHouse=self.Map1.sprite_lists["BigHouse"]
        self.Flower=self.Map1.sprite_lists["Flower"]
        self.Tree=self.Map1.sprite_lists["Tree"]
        self.Decor=self.Map1.sprite_lists["Decor"]
        self.Crops=self.Map1.sprite_lists["Crops"]
        self.Chicken=self.Map1.sprite_lists["Chicken"]
        self.Players = ar.SpriteList()
        self.Player = PlayerCharacter()
        self.Player.center_x = x // 2
        self.Player.center_y = y // 2
        self.Player.scale=0.5
        self.Players.append(self.Player)
        self.physic_engine=ar.PhysicsEngineSimple(self.Player, [self.Tree,self.Tent,self.Decor] )

    def on_draw(self):
        ar.start_render()

        self.Ground.draw()
        self.Path.draw()
        self.Tent.draw()
        self.Water.draw()
        self.RHouse.draw()
        self.BHouse.draw()
        self.BigHouse.draw()
        self.Flower.draw()
        self.Tree.draw()
        self.Decor.draw()
        self.Crops.draw()
        self.Chicken.draw()


        self.Players.draw()
    def on_key_press(self,key,modifiers):
        if key==ar.key.A or key==ar.key.LEFT:
            self.left_press=True
        elif key==ar.key.D or key==ar.key.RIGHT:
            self.right_press=True
        elif key==ar.key.W or key==ar.key.UP:
            self.up_press=True
        elif key==ar.key.S or key==ar.key.DOWN:
            self.down_press=True
    def on_key_release(self,key,modifiers):
        if key==ar.key.A or key==ar.key.LEFT:
            self.left_press=False
        elif key==ar.key.D or key==ar.key.RIGHT:
            self.right_press=False
        elif key==ar.key.W or key==ar.key.UP:
            self.up_press=False
        elif key==ar.key.S or key==ar.key.DOWN:
            self.down_press=False
    def on_update(self, delta_time: float):
        self.physic_engine.update()
        self.Players.update()
        self.Players.update_animation()
        if self.left_press== True and not self.right_press==True:
            self.Player.change_x=-movement
        elif self.right_press== True and not self.left_press==True:
            self.Player.change_x=movement
        elif self.up_press==True and not self.down_press==True:
            self.Player.change_y=movement
        elif self.down_press==True and not self.up_press==True:
            self.Player.change_y=-movement
        else:
            self.Player.change_x=0
            self.Player.change_y=0
        RedHouseColl = ar.check_for_collision_with_list(self.Player, self.RHouse)
        if RedHouseColl:
            Red = IndoorRed()
            Red.setup()
            self.window.show_view(Red)
        BHouseColl = ar.check_for_collision_with_lists(self.Player,[self.BHouse,self.BigHouse])
        if BHouseColl:
            B = IndoorB()
            B.setup()
            self.window.show_view(B)

class IndoorRed(ar.View):
    def __init__(self):
        super().__init__()

        self.Map2=None
        self.Ground = None
        self.Doors = None
        self.DecorTranslucent = None
        self.Decor=None
        self.Carpet=None
        self.Bed=None
        self.Walls=None
        self.exit1=None
        self.Player=None
        self.Players=None
        self.left_press=None
        self.right_press=None
        self.down_press=None
        self.up_press=None
        self.physic_engine=None

    def setup(self):

        self.Map2=ar.load_tilemap("IndoorMap.json",2)

        self.Grounds=self.Map2.sprite_lists["Ground"]
        self.Walls=self.Map2.sprite_lists["Walls"]
        self.Decor=self.Map2.sprite_lists["Decoration-NotTranslucent"]
        self.Bed=self.Map2.sprite_lists["Bed"]
        self.DecorTranslucent=self.Map2.sprite_lists["Decor"]
        self.Doors=self.Map2.sprite_lists["Doors"]
        self.exit1=self.Map2.sprite_lists["exitt"]

        self.Carpet=self.Map2.sprite_lists["Carpet"]
        self.Players = ar.SpriteList()
        self.Player = PlayerCharacter()
        self.Player.center_x = x // 2
        self.Player.center_y = y // 2
        self.Player.scale=0.5
        self.Players.append(self.Player)
        self.physic_engine=ar.PhysicsEngineSimple(self.Player, [self.DecorTranslucent, self.Walls,self.Bed] )


    def on_draw(self):
        ar.start_render()

        self.Grounds.draw()
        self.Walls.draw()
        self.Carpet.draw()
        self.Decor.draw()
        self.Doors.draw()
        self.DecorTranslucent.draw()
        self.Bed.draw()
        self.exit1.draw()

        self.Players.draw()
    def on_key_press(self,key,modifiers):
        if key==ar.key.A or key==ar.key.LEFT:
            self.left_press=True
        elif key==ar.key.D or key==ar.key.RIGHT:
            self.right_press=True
        elif key==ar.key.W or key==ar.key.UP:
            self.up_press=True
        elif key==ar.key.S or key==ar.key.DOWN:
            self.down_press=True
    def on_key_release(self,key,modifiers):
        if key==ar.key.A or key==ar.key.LEFT:
            self.left_press=False
        elif key==ar.key.D or key==ar.key.RIGHT:
            self.right_press=False
        elif key==ar.key.W or key==ar.key.UP:
            self.up_press=False
        elif key==ar.key.S or key==ar.key.DOWN:
            self.down_press=False
    def on_update(self, delta_time: float):
        self.physic_engine.update()
        self.Players.update()
        self.Players.update_animation()
        if self.left_press== True and not self.right_press==True:
            self.Player.change_x=-movement
        elif self.right_press== True and not self.left_press==True:
            self.Player.change_x=movement
        elif self.up_press==True and not self.down_press==True:
            self.Player.change_y=movement
        elif self.down_press==True and not self.up_press==True:
            self.Player.change_y=-movement
        else:
            self.Player.change_x=0
            self.Player.change_y=0
        Way=ar.check_for_collision_with_list(self.Player,self.exit1)
        if Way:
            game = GameWindow()
            game.setup()
            self.window.show_view(game)
class IndoorB(ar.View):
    def __init__(self):
        super().__init__()

        self.Map3=None
        self.Floor=None
        self.Carpet=None
        self.Walls=None
        self.Decor=None
        self.Door=None
        self.Player=None
        self.Players=None
        self.left_press=None
        self.right_press=None
        self.down_press=None
        self.up_press=None
        self.physic_engine=None

    def setup(self):

        self.Map3=ar.load_tilemap("IndoorBigAndBlue.json",2)
        self.Floor=self.Map3.sprite_lists["Floor"]
        self.Carpet=self.Map3.sprite_lists["Carpet"]
        self.Walls=self.Map3.sprite_lists["Walls"]
        self.Decor=self.Map3.sprite_lists["Decoration"]
        self.Door=self.Map3.sprite_lists["Door"]

        self.Players = ar.SpriteList()
        self.Player = PlayerCharacter()
        self.Player.center_x = x // 2
        self.Player.center_y = y // 2
        self.Player.scale=0.5
        self.Players.append(self.Player)
        self.physic_engine=ar.PhysicsEngineSimple(self.Player, [self.Decor, self.Walls] )


    def on_draw(self):
        ar.start_render()
        self.Floor.draw()
        self.Carpet.draw()
        self.Walls.draw()
        self.Decor.draw()
        self.Door.draw()


        self.Players.draw()
    def on_key_press(self,key,modifiers):
        if key==ar.key.A or key==ar.key.LEFT:
            self.left_press=True
        elif key==ar.key.D or key==ar.key.RIGHT:
            self.right_press=True
        elif key==ar.key.W or key==ar.key.UP:
            self.up_press=True
        elif key==ar.key.S or key==ar.key.DOWN:
            self.down_press=True
    def on_key_release(self,key,modifiers):
        if key==ar.key.A or key==ar.key.LEFT:
            self.left_press=False
        elif key==ar.key.D or key==ar.key.RIGHT:
            self.right_press=False
        elif key==ar.key.W or key==ar.key.UP:
            self.up_press=False
        elif key==ar.key.S or key==ar.key.DOWN:
            self.down_press=False
    def on_update(self, delta_time: float):
        self.physic_engine.update()
        self.Players.update()
        self.Players.update_animation()
        if self.left_press== True and not self.right_press==True:
            self.Player.change_x=-movement
        elif self.right_press== True and not self.left_press==True:
            self.Player.change_x=movement
        elif self.up_press==True and not self.down_press==True:
            self.Player.change_y=movement
        elif self.down_press==True and not self.up_press==True:
            self.Player.change_y=-movement
        else:
            self.Player.change_x=0
            self.Player.change_y=0
        Out=ar.check_for_collision_with_list(self.Player,self.Door)
        if Out:
            game = GameWindow()
            game.setup()
            self.window.show_view(game)


def main():
    window=ar.Window(x,y,"Game")
    start=StartScreen()
    start.setup()
    game=GameWindow()
    Red=IndoorRed()
    B=IndoorB()
    HTP=HTPWindow()
    window.show_view(start)


    ar.run()
main()
