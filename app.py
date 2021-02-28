import constants
from decimal import Decimal

#Creates new copies of the dictionaries

teams = constants.TEAMS
players = constants.PLAYERS
num_of_players = len(players) / len(teams)

#Converting dictionaries
#updated_players list holds the cleaned version of the constants dictionary. new_players and experienced_players holds lists of players and their respective XP. same for the guardians lists.

updated_players = []
new_players = []
new_player_guardians = []
experienced_players = []
experienced_players_guardians = []

#teams holds three lists of teams with their 'drafted' players. team_height holds their heights, team_guardians holds their guardians.

teams = {0: [], 1: [], 2: []}
team_height = {0: [], 1: [], 2: []}
team_guardians = {0: [], 1: [], 2: []}


#balances the three teams by adding three experienced and new players to each        
def balance_teams():
  counter = 0
  for i in players:
    
    if i['experience'] == 'YES':
      i['name'] = "*" + i['name']
      experienced_players.append(i['name'])
      i['guardians'] = i['name'] + "'s guardian(s): " + i['guardians'].replace("and", "" )
      experienced_players_guardians.append(i['guardians'])
      
      
    elif i['experience'] == 'NO':
      new_players.append(i['name'])
      i['guardians'] = i['name'] + "'s guardian(s): " + i['guardians'].replace("and", "" )
      new_player_guardians.append(i['guardians'])
  team_list = len(teams)
  for j in new_players:
      teams[counter % team_list].append(j)
      counter+= 1
      
  for f in experienced_players:
      teams[counter % team_list].append(f)
      counter+= 1 
      
  for guardian in new_player_guardians:
      team_guardians[counter % team_list].append(guardian)
      counter+= 1
      
  for g in experienced_players_guardians:
      team_guardians[counter % team_list].append(g)
      counter+= 1      
      
#takes average height of each team and converts to feet, rounds to the next inch
def get_average_height():
  counter = 0
  team_height_list = len(team_height)
  
  for i in updated_players:
    team_height[counter % team_height_list].append(i['height'])
    counter+= 1
  return (
    round((sum(team_height[0]) / len(team_height[0]) / 12 ) + .1, 1), 
    round((sum(team_height[1]) / len(team_height[1]) / 12) + .1, 1), 
    round((sum(team_height[2]) / len(team_height[2]) / 12) + .1, 1)
  )
  
#cleans data from player dictionary. adds an asterisk to players who are experienced, removes the 'in' from their height, and changes their experience to a Boolean value

def clean_data():
  for player in players:
    if len(player['height']) > 2 and player['experience'] == 'YES':
      player['height'] = int(player['height'][0:2])
      player['experience'] = 'True'
      updated_players.append(player)
      
    elif len(player['height']) > 2 and player['experience'] == 'NO':
      player['height'] = int(player['height'][0:2])
      player['experience'] = 'False'
      updated_players.append(player)
      
    if "and" in player['guardians']:
      updated_players.append(player)
      
    elif "and" not in player['guardians']:
      updated_players.append(player)

            
#Gets the list of guardians
def get_guardians():
  return (
    team_guardians[0],
    team_guardians[1],
    team_guardians[2]
  )

#Introduction
def intro():
  print("BASKETBALL TEAM STATS TOOL")
  print("Enter A to navigate through the team stats or B to quit: \n A) Display Team Stats \n B) Quit")

#simple parting message after the user ends the program
def terminate():
  print("Goodbye!")    
  
#Initiates the program
def start():  
  user_choice = ""
  while user_choice != "A" or user_choice != "B":
    try:
      user_choice = str(input("Enter your selection:  ").upper())
      if user_choice == "A":
        break
      elif user_choice == "B":
        terminate()
        break
      else:
        raise ValueError
    except ValueError:
        print("Please enter a valid option.")
        
  second_choice = ""
  if user_choice != "B":
    while second_choice != "A" or second_choice != "B" or second_choice != "C" or second_choice != "X":
      try:
        second_choice = str(input("\n Select a team to view their stats or enter X to quit.  \n TEAMS: \n A) Panthers \n B) Bandits \n C) Warriors \n").upper())
        
        if second_choice == "A":
          print(f"Roster for the Panthers: \n  \n An * indicates a veteran player \n  \n {', '.join(teams[0])} \n  \n Total players on the Panthers: {len(teams[0])} \n  \n Average team height: {panthers_height}\' \n  \n {panthers_guardians} \n") 

        elif second_choice == "B":
          print(f"\n Roster for the Bandits: \n  \n An * indicates a veteran player \n  \n {', '.join(teams[1])} \n  \n Total players on the Bandits: {len(teams[1])} \n  \n Average team height: {bandits_height}\' \n  \n {bandits_guardians} \n")

        elif second_choice == "C":
          print(f"Roster for the Warriors: \n  \n An * indicates a veteran player \n  \n {', '.join(teams[2])} \n  \n Total players on the Warriors: {len(teams[2])} \n  \n Average team height: {warriors_height}\' \n  \n {warriors_guardians}")

        elif second_choice == "X":
          terminate()
          break
        else:
          raise ValueError
      except:
        print(f"Please choose one of the {len(teams)} teams.")

if __name__ == "__main__":
  balance_teams()
  clean_data()      
  panthers_height, bandits_height, warriors_height = get_average_height()
  get_guardians()
  panthers_guardians, bandits_guardians, warriors_guardians = get_guardians()
  intro()
  start()


