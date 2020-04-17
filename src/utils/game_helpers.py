from v1.player import Player


def find_player_by_name(players: list, name: str) -> Player:
    return next((p for p in players if p.name == name), None)


def count_player_by_name(players: list, name: str) -> int:
    return len([p for p in players if p.name == name])
