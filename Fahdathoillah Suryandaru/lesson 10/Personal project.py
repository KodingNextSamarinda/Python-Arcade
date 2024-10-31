import arcade

GRID = 140
WIDTH_MAP = 10 * GRID
HEIGHT_MAP = 5 * GRID
TITLE = "Inside"
Speed = 3
Jump = 5

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH_MAP, HEIGHT_MAP, TITLE)
        self.personal = None
        self.main = None
        self.background = None
        self.obstacles = None
        self.ladder = None
        self.deco = None
        self.player = None
        self.physics = None
        self.stand = None
        self.score= None


    def setup(self):
        self.personal = arcade.load_tilemap("assets/personal.json", scaling=0.2)
        self.main = self.personal.sprite_lists["main"]
        self.ladder = self.personal.sprite_lists["ladder"]
        self.deco = self.personal.sprite_lists["decoration"]
        self.background = self.personal.sprite_lists["background"]
        self.obstacles = self.personal.sprite_lists["obstacles"]

        self.physics = arcade.PhysicsEnginePlatformer(self.player,self.main)


        self.player = arcade.Sprite(":resources:images/animated_characters/robot/robot_walk4.png", scale=0.3)
        self.player.center_x = 75
        self.player.center_y = 650

        self.physics = arcade.PhysicsEnginePlatformer(self.player,self.main)
        self.stand = arcade.PhysicsEnginePlatformer(self.player,self.deco)
        self.slipped = arcade.()

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.obstacles.draw()
        self.deco.draw()
        self.ladder.draw()
        self.main.draw()
        self.player.draw()

    def on_update(self,delta_time: float):
        self.player.update()
        self.physics.update()
        self.stand.update()
        if arcade.check_for_collision_with_list(self.player,self.obstacles):
            self.close()



    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.player.change_x = Speed
        elif symbol == arcade.key.A:
            self.player.change_x = -Speed
        elif symbol == arcade.key.SPACE:
            if self.physics.can_jump():
                self.player.change_y = Jump

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.player.change_x = 0
        elif symbol == arcade.key.A:
            self.player.change_x = 0





level = Game()
level.setup()
arcade.run()























































#Yipee yay, there'll be no wedding bells for today!

#I got spurs that jingle, jangle, jingle (Jingle, jangle)
#As I go riding merrily along (Jingle, jangle)
#And they sing, "Oh, ain't you glad you're single?" (Jingle, jangle)
#And that song ain't so very far from wrong (Jingle, jangle)

#Oh, Lillie Belle (Oh Lillie Belle)
#Oh, Lillie Belle (Oh, Lillie Belle)
#Though I may have done some fooling
#This is why I never fell

#I got spurs that jingle, jangle, jingle (Jingle, jangle)
#As I go riding merrily along (Jingle, jangle)
#And they sing, "Oh, ain't you glad you're single?" (Jingle, jangle)
#And that song ain't so very far from wrong (Jingle, jangle)

#Oh, Mary Ann
#Oh, Mary Ann
#Though we done some moonlight walking
#This is why I up and ran

#I got spurs that jingle, jangle, jingle
#As I go riding merrily along
#And they sing, "Oh, ain't you glad you're single?"
#And that song ain't so very far from wrong