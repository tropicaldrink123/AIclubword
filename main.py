'''
list_happy_words = [“joyful”, “happy”, “amazing”, “beautiful”]
list_sad_words = [“sad”, “tears”, “crying”, “depressed”]
list_games = [“tetris”, “flappy bird”, “snake”]
'''

# Declare the 3 lists
list_happy_words = ["joyful", "happy", "amazing", "beautiful"]
list_sad_words = ["sad", "tears", "crying", "depressed"]
list_games = ["tetris", "flappy bird", "snake"]

# Initialize the games_index variable
games_index = 0
# A variable to tell if the program should break from the while loop
set_break_flag = False

# This while loop goes on infinitely
# Till it encounters a breaak in the program
while True:
  # ask the user to input a word describing their feeling, save the string
  feeling = input('How are you feeling today?')
  # Check if the word is a part of the happy list
  feeling_lower = feeling.casefold()
  for item in list_happy_words:
    if item in feeling_lower:
      print('Glad to know!')
      set_break_flag = True
      break

  if set_break_flag:
    break
  else:
    # Check if games list is over
    # This can be done in several way, we will
    # use the index to determine this
    if games_index >= len(list_games):
      print('Sorry, we are out of games to suggest')
      break
    else:
      for item in list_sad_words:
        if item in feeling_lower:
          print('Sorry you feel this way.')
          print('Please play ', list_games[games_index])
          games_index = games_index + 1
          # Note that below break is just for the for loop, not the while loop
          break
        # Go back to asking user how they feel
      else:
        print('I dont understand how you feel!')
        break

# Note that break is used in the above to break out of the loop

# An alternate solution using a for loop on number of games

"""
# Initialize the games_index variable
games_index = 0

for game_index in range(0,len(list_games)):
  # ask the user to input a word describing their feeling, save the string
  feeling = input('How are you feeling today?')
  # Check if the word is a part of the happy list
  # Check if the word is a part of the happy list
  feeling_lower = feeling.casefold()
  for item in list_happy_words:
    if item in feeling_lower:
      print('Glad to know!')
      set_break_flag = True
      break

  if set_break_flag:
    break
  else:
    for item in list_sad_words:
        feeling_lower = feeling.casefold()
        if item in feeling_lower:
          print('Sorry you feel this way.')
          print('Please play ', list_games[games_index])
          # Break out of the inner for loop
          break

      # Go back to asking user how they feel
    else:
      print('I dont understand how you feel!')
      break

# Check if the last feeling was sad
if feeling in list_sad_words:
  print('Sorry, we are out of games to suggest')
"""