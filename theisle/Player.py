import json


class Player:
    def __init__(self, path, steamid):
        self.path = path
        self.steamid = steamid

        with open(self.path) as file:
            self.player_data = json.load(file)
            self.CharacterClass = self.player_data['CharacterClass']
            self.Growth = self.player_data['Growth']
            self.Hunger = self.player_data['Hunger']
            self.Thirst = self.player_data['Thirst']
            self.Stamina = self.player_data['Stamina']
            self.Health = self.player_data['Health']
            self.BleedingRate = self.player_data['BleedingRate']
            self.Oxygen = self.player_data['Oxygen']
            self.bGender = str(self.player_data['bGender'])
            self.bIsResting = str(self.player_data['bIsResting'])
            self.bBrokenLegs = str(self.player_data['bBrokenLegs'])
            self.UnlockedCharacters = self.player_data['UnlockedCharacters']

    def grow(self, growth='1.0'):
        growth = float(growth)

        if growth < 0 or growth > 1.0:
            return False

        self.Growth = str(growth)
        self.bIsResting = 'false'
        self.UnlockedCharacters = ''
        self.heal()
        return True

    def heal(self):
        self.Health = '99999'
        self.Thirst = '99999'
        self.Stamina = '99999'
        self.Hunger = '99999'
        self.BleedingRate = '0'
        self.Oxygen = '40'

    def save(self):
        self.player_data['CharacterClass'] = self.CharacterClass
        self.player_data['Growth'] = str(self.Growth)
        self.player_data['Hunger'] = str(self.Hunger)
        self.player_data['Thirst'] = str(self.Thirst)
        self.player_data['Stamina'] = str(self.Stamina)
        self.player_data['Health'] = str(self.Health)
        self.player_data['BleedingRate'] = str(self.BleedingRate)
        self.player_data['Oxygen'] = str(self.Oxygen)
        self.player_data['bGender'] = self.bGender.lower()
        self.player_data['bIsResting'] = self.bBrokenLegs.lower()
        self.player_data['bBrokenLegs'] = self.bBrokenLegs.lower()
        self.player_data['UnlockedCharacters'] = str(self.UnlockedCharacters)

        with open(self.path, 'w') as file:
            file.write(json.dumps(self.player_data, indent=4))
        return True
