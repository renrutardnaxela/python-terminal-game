class Monster:
    def __init__(self, name, monsterHP, attack, defend, sneak):
        self.name = name
        self.monsterHP = monsterHP
        self.attack = attack
        self.defend = defend
        self.sneak = sneak

    def print_monster_stats(self):
        print('============')
        print(f'Monster: {self.name}')
        print(f'HP: {self.monsterHP}')
        print('============')

    def change_monsterlHP(self, damage):
        self.monsterHP -= damage