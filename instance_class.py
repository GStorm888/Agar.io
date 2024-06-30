from field import Field
from object import Player
class InstanceClass:
    player = Player(0, 0, 8)
    field = Field(player)
    
    # player =  Player.render()
    # field = Field(Player.render())
    # @staticmethod
    # def get_player():
    #     return Player.render()
    # @classmethod
    # def get_field():
    #     return Field(Player.render())