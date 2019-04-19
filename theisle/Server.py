from .Player import Player
import os


class Server:
    def __init__(self, path):
        self.path = path
        if not self.path[-1:] == '/':
            self.path = self.path + '/'

    def getplayer(self, steamid):
        steamid = str(steamid)
        if os.path.exists(self.path + steamid + '.json'):
            return Player(self.path + steamid + '.json', steamid)
        return False

    def players(self):
        for file in os.listdir(self.path):
            if file.endswith('.json'):
                yield Player(self.path + file, file[:-5])
