import arcade
from player import PlayerCharacter

width = 16 * 60
height = 16 * 45
title = "project"
Speed = 1


class start(arcade.View):
    def __init__(self):
        super().__init__()
        self.music = arcade.load_sound("Assets/HarvestOst.mp3")
        arcade.play_sound(self.music, volume=0.5, looping=True, speed=1.0)

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Destroy-it",width/2,300,arcade.color.BLACK,font_size=50,anchor_x="center")
        arcade.draw_text("Click to continue", width/2,255,arcade.color.BLACK,font_size=24,anchor_x="center")

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == 1:
            window = menu()
            window.setup()
            game.show_view(window)

class menu(arcade.View):

    def __init__(self):
        super().__init__()

        self.project = None
        self.fence = None
        self.crop = None
        self.chicken = None
        self.bird = None
        self.bridge = None
        self.tree = None
        self.dirt = None
        self.ground = None
        self.door = None
        self.water = None
        self.under = None
        self.player = None
        self.players = None
        # self.houses = None
        self.waters = None
        self.masjid = None

        self.fences = None
        self.score = 0
        self.rig = False
        self.masjids = None

    def setup(self):
        self.project = arcade.load_tilemap("assets/project.json",scaling=1)



        self.masjid = self.project.sprite_lists["masjid"]
        self.fence = self.project.sprite_lists["fence"]
        self.crop = self.project.sprite_lists["crop"]
        self.chicken = self.project.sprite_lists["chicken"]
        self.bird = self.project.sprite_lists["bird"]
        self.bridge = self.project.sprite_lists["bridge"]
        # self.houses = self.project.sprite_lists["house"]
        self.tree = self.project.sprite_lists["tree"]
        self.dirt = self.project.sprite_lists["dirt"]
        self.ground = self.project.sprite_lists["ground"]
        self.door = self.project.sprite_lists["door"]
        self.water = self.project.sprite_lists["water"]
        self.under = self.project.sprite_lists["under"]

        self.players = arcade.SpriteList()
        self.player = PlayerCharacter()
        self.player.center_x = 400
        self.player.center_y = 90
        self.players.append(self.player)
        self.waters = arcade.PhysicsEngineSimple(self.player, self.water)
        self.masjids = arcade.PhysicsEngineSimple(self.player, self.masjid)

    def on_draw(self):
        self.clear()
        self.under.draw()
        self.water.draw()
        self.door.draw()
        self.ground.draw()
        self.dirt.draw()
        self.tree.draw()
        # self.houses.draw()
        self.bridge.draw()
        self.bird.draw()
        self.chicken.draw()
        self.crop.draw()
        self.fence.draw()
        self.masjid.draw()
        self.player.draw()

        scoring = f"Things destroyed {self.score}"
        arcade.draw_text(scoring, 10, 590, color=arcade.color.CRIMSON_GLORY)

    def on_update(self, delta_time: float):
        self.players.update()
        self.players.update_animation()

        self.waters.update()
        self.masjids.update()

        inside = arcade.check_for_collision_with_list(self.player, self.door)
        if inside:
            window = indoor()
            window.setup()
            game.show_view(window)










        collect = arcade.check_for_collision_with_list(self.player, self.crop)
        if collect and self.rig == True:
            for each_item in collect:
                each_item.remove_from_sprite_lists()
                self.score += 1

        chop = arcade.check_for_collision_with_list(self.player, self.tree)
        if chop and self.rig == True:
            for each_item in chop:
                each_item.remove_from_sprite_lists()
                self.score += 1

        # destroy = arcade.check_for_collision_with_list(self.player, self.houses)
        #
        # if destroy:
        #     for house in destroy:
        #         if house.center_x is None or house.center_y is None:
        #             print(f"Invalid house sprite detected: {house}")
        #         else:
        #             print("house destroyed")
        #             house.remove_from_sprite_lists()
        #             self.score += 1

        chicken = arcade.check_for_collision_with_list(self.player, self.chicken)
        if chicken and self.rig == True:
            for each_item in chicken:
                each_item.remove_from_sprite_lists()
                self.score += 1

        bird = arcade.check_for_collision_with_list(self.player, self.bird)
        if bird and self.rig == True:
            for each_item in bird:
                each_item.remove_from_sprite_lists()
                self.score += 1

        fence = arcade.check_for_collision_with_list(self.player, self.fence)
        if fence and self.rig == True:
            for each_item in fence:
                each_item.remove_from_sprite_lists()
                self.score += 1






    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.player.change_y = Speed
        elif symbol == arcade.key.S:
            self.player.change_y = -Speed
        elif symbol == arcade.key.A:
            self.player.change_x = -Speed
        elif symbol == arcade.key.D:
            self.player.change_x = Speed
        elif symbol == arcade.key.E:
            self.rig = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.player.change_y = 0
        elif symbol == arcade.key.S:
            self.player.change_y = 0
        elif symbol == arcade.key.A:
            self.player.change_x = 0
        elif symbol == arcade.key.D:
            self.player.change_x = 0
        elif symbol == arcade.key.E:
            self.rig = False

class indoor(arcade.View):
    def __init__(self):
        super().__init__()

        self.indoor = None
        self.exit = None
        self.door = None
        self.money = None
        self.house = None
        self.book = None
        self.bed = None
        self.clock = None
        self.candle = None
        self.stuff = None
        self.piano = None
        self.wall = None
        self.tablechair = None
        self.insidewall = None
        self.walkthrough = None
        self.floor = None

        self.player = None
        self.players = None
        self.trigger = False
        self.score = 0

    def setup(self):

        self.indoor = arcade.load_tilemap("assets/projectinterior.json", scaling=1)
        self.walkthrough = self.indoor.sprite_lists["walkthrough"]
        self.insidewall = self.indoor.sprite_lists["inside wall"]
        self.tablechair = self.indoor.sprite_lists["table/chair"]
        self.wall = self.indoor.sprite_lists["wall"]
        self.piano = self.indoor.sprite_lists["piano"]
        self.stuff = self.indoor.sprite_lists["stuff"]
        self.candle = self.indoor.sprite_lists["candle"]
        self.clock = self.indoor.sprite_lists["clock"]
        self.bed = self.indoor.sprite_lists["bed"]
        self.floor = self.indoor.sprite_lists["floor"]
        self.book = self.indoor.sprite_lists["book"]
        self.house = self.indoor.sprite_lists["house"]
        self.money = self.indoor.sprite_lists["money"]
        self.door = self.indoor.sprite_lists["door"]
        self.exit = self.indoor.sprite_lists["exit"]

        self.players = arcade.SpriteList()
        self.player = PlayerCharacter()
        self.player.center_x = 400
        self.player.center_y = 400
        self.players.append(self.player)
        self.walls = arcade.PhysicsEngineSimple(self.player, self.wall)
        self.insidewalls = arcade.PhysicsEngineSimple(self.player, self.insidewall)

    def on_draw(self):
        self.floor.draw()
        self.walkthrough.draw()
        self.insidewall.draw()
        self.tablechair.draw()
        self.wall.draw()
        self.piano.draw()
        self.stuff.draw()
        self.candle.draw()
        self.clock.draw()
        self.bed.draw()
        self.book.draw()
        # self.house.draw()
        self.money.draw()
        self.door.draw()
        self.exit.draw()
        self.player.draw()

    def on_update(self, delta_time: float):



        self.players.update()

        self.players.update_animation()

        outside = arcade.check_for_collision_with_list(self.player, self.exit)
        if outside:
            window = menu()
            window.setup()
            game.show_view(window)

        take = arcade.check_for_collision_with_list(self.player, self.tablechair)
        if take and self.trigger == True:
            for each_item in take:
                each_item.remove_from_sprite_lists()
                self.score += 1

        pianist = arcade.check_for_collision_with_list(self.player, self.piano)
        if pianist and self.trigger == True:
            for each_item in pianist:
                each_item.remove_from_sprite_lists()
                self.score += 1

        take = arcade.check_for_collision_with_list(self.player, self.tablechair)
        if take and self.trigger == True:
            for each_item in take:
                each_item.remove_from_sprite_lists()
                self.score += 1

        stuf = arcade.check_for_collision_with_list(self.player, self.stuff)
        if stuf and self.trigger == True:
            for each_item in stuf:
                each_item.remove_from_sprite_lists()
                self.score += 1

        lit = arcade.check_for_collision_with_list(self.player, self.candle)
        if lit and self.trigger == True:
            for each_item in lit:
                each_item.remove_from_sprite_lists()
                self.score += 1

        zzz = arcade.check_for_collision_with_list(self.player, self.bed)
        if zzz and self.trigger == True:
            for each_item in zzz:
                each_item.remove_from_sprite_lists()
                self.score += 1

        read = arcade.check_for_collision_with_list(self.player, self.book)
        if read and self.trigger == True:
            for each_item in read:
                each_item.remove_from_sprite_lists()
                self.score += 1

        # ohno = arcade.check_for_collision_with_list(self.player, self.house)
        # if ohno and self.trigger == True:
        #     for each_item in ohno:
        #         each_item.remove_from_sprite_lists()
        #         self.score += 1

        steal = arcade.check_for_collision_with_list(self.player, self.money)
        if steal and self.trigger == True:
            for each_item in steal:
                each_item.remove_from_sprite_lists()
                self.score += 1

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.player.change_y = Speed
        elif symbol == arcade.key.S:
            self.player.change_y = -Speed
        elif symbol == arcade.key.A:
            self.player.change_x = -Speed
        elif symbol == arcade.key.D:
            self.player.change_x = Speed
        elif symbol == arcade.key.E:
            self.trigger = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.player.change_y = 0
        elif symbol == arcade.key.S:
            self.player.change_y = 0
        elif symbol == arcade.key.A:
            self.player.change_x = 0
        elif symbol == arcade.key.D:
            self.player.change_x = 0
        elif symbol == arcade.key.E:
            self.trigger = False



game = arcade.Window(width, height, title)
show = start()
game.show_view(show)
arcade.run()

