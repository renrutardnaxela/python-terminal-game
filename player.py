class GamePlayer:
    def __init__(self, playerHP, damage):
        self.playerHP = playerHP
        self.damage = damage

    def print_player_stats(self):
        print('============')
        print('Monster: You')
        print(f'HP: {self.playerHP}')
        print(f'Damage: {self.damage}')
        print('============')

    def change_playerHP(self, attack):
        self.playerHP -= attack