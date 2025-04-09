class Player:

  def __init__(self, name, team):
    self.name = name
    self.xp = 1500
    self.team = team

  def introduce(self):
    print(f"Hi, my name is {self.name} and I'm on team {self.team}")


class Team:

  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []

  def add_player(self, player):
    new_player = Player(player, self.team_name)
    self.players.append(new_player)
    print(f"Added {new_player.name} to team {self.team_name}")

  def show_players(self):
    for player in self.players:
      player.introduce()

  #remote player
  def remove_player(self, name):
    for player in self.players:
      if player.name == name:
        self.players.remove(player)
        print(f"Removed {player.name} from team {self.team_name}")
        player.team = None
        return
    print(f"No player named {name} found in team {self.team_name}")

  #total team xp
  def total_team_xp(self):
    total_xp = 0
    for player in self.players:
      total_xp += player.xp
    print(f"Total team XP: {total_xp}")

team_x = Team("Team X")
team_x.add_player("John")
team_x.add_player("Jane")
team_x.show_players()

team_x.remove_player("John")
team_x.show_players()

team_x.total_team_xp()