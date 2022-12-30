from war_simulator.dao.game_dao import GameDao
from war_simulator.model.battlefield import Battlefield
from war_simulator.model.game import Game
from war_simulator.model.player import Player
from war_simulator.model.vessel import Vessel


class GameService:
    def __init__(self):
        self.game_dao = GameDao()

    def create_game(self, player_name: str, min_x: int, max_x: int, min_y: int, max_y: int, min_z: int,
                    max_z: int) -> int:
        game = Game()
        battle_field = Battlefield(min_x, max_x, min_y, max_y, min_z, max_z)
        game.add_player(Player(player_name, battle_field))
        return self.game_dao.create_game(game)

    def join_game(self, game_id: int, player_name: str) -> bool:
        # à implementer
        game = self.get_game(game_id)
        game.add_player(self.get_player(player_name))

    def get_game(self, game_id: int) -> Game:
        return self.game_dao.find_game(game_id)

    def get_player(self, player_name: str) -> Player:
        return self.game_dao.find_player(player_name)

    def find_vessel(self, vessel_id: int) -> Player:
        return self.game_dao.find_vessel(vessel_id)

    def add_vessel(self, game_id: int, player_name: str, vessel_type: str, x: int, y: int, z: int) -> bool:
        # à implementer
        game = self.get_game(game_id)
        player = self.get_player(player_name)
        battlefield = player.get_battlefield()
        vessel = Vessel(id=None, x=x, y=y, z=z, weapon=None, hits=None, type=vessel_type)
        battlefield.add_vessel(vessel)

        self.game_dao.update_vessel(vessel)

    def shoot_at(self, game_id: int, shooter_name: str, vessel_id: int, x: int, y: int, z: int) -> bool:
        # à implementer
        vessel = self.game_dao.find_vessel(vessel_id)
        map_to_vessel

    def get_game_status(self, game_id: int, shooter_name: str) -> str:
        # à implemente
        pass
