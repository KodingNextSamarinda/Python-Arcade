import arcade

MoventSpeed = 5
UpdatePerFrame = 5

FacingRight = 0
FacingLeft = 1

def load_texture_pair(filename):

    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename,flipped_horizontally=False)
    ]

class PlayerCharacter(arcade.Sprite):
    def __init__(self):
        super().__init__()

        #making a default character facing
        self.Char_face_direction = FacingRight

        self.current_texture = 0

        self.scale = 0.5

        #setting the collition box
        self.points = [[-22,-36],[22,-36],[22,36],[-22,36]]

        #load the texture
        simpan_texture = ":resources:images/animated_characters/male_person/malePerson"

        #create an attributes to save idle texture
        self.idle_texture = load_texture_pair(f"{simpan_texture}_idle.png")

        #load all the walking textures
        self.walking = []
        for i in range (8):
            texture = load_texture_pair(f"{simpan_texture}_walk{i}.png")
            self.walking.append(texture)

        self.set_hit_box(self.points)

    def update_animation(self, delta_time: float = 1 / 60):

        #idle texture
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture[self.Char_face_direction]
            return

        #walking texture
        self.current_texture += 1
        if self.current_texture > 7 * UpdatePerFrame:
            self.current_texture = 0

        frame = self.current_texture // UpdatePerFrame
        direction = self.Char_face_direction
        self.texture = self.walking[frame][direction]

        #to set the face == looking right or left
        if self.change_x < 0 and self.Char_face_direction == FacingLeft:
            self.Char_face_direction = FacingRight
        elif self.change_x > 0 and self.Char_face_direction == FacingRight:
            self.Char_face_direction = FacingLeft