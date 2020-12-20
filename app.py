from random import shuffle


class Player:
    CITIZEN = 0
    MAFIA = 1

    def __init__(self, username):
        self.username = username
        self.role = Player.CITIZEN
        self.votes = 0

    def __str__(self):
        return self.username

    def __gt__(self, other):
        return self.votes >= other.votes

    def vote(self):
        self.votes += 1


class Room:
    MIN_CITIZENS = 1

    def __init__(self):
        self.players = []

    def add(self, player):
        self.players.append(player)

    def assign_roles(self):
        shuffle(self.players)
        self.players[0].role = Player.MAFIA

    def kill(self, player):
        self.players.remove(player)

    def end(self):
        print('game ended')

    def initialize(self):
        player_to_kill = max(self.players)
        self.kill(player_to_kill)

        for player in self.players:
            player.votes = 0

    def step(self):
        if len(self.players) < Room.MIN_CITIZENS:
            self.end()
        else:
            self.initialize()

    def start(self):
        if len(self.players) < 4:
            raise Exception('At least 4 players required')
        self.initialize()


if __name__ == '__main__':
    room = Room()
    for i in range(5):
        room.add(Player(f'test{i}'))
    room.players[-1].vote()

    print(max(room.players))
