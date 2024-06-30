from field import Field
from object import Player
class InstanceClass:
    # player =  Player.render()
    # field = Field(Player.render())
    @classmethod
    def get_player():
        return Player.render()
    @classmethod
    def get_field():
        return Field(Player.render())