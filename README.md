# 12th Project: Non-Graphical-Game
This is a non-graphical, text-based game created by me for my 12th school project in python.
It features several mini-games in itself like 21 matchsticks, hangman, hot or cold, etc and follows the player's quest.
It also has many chocies throughout the game and the game's ending depends on the choices made by the player.
I've also included a scoring system in the game and a database where players can save their scores. If a player takes multiple tries to win a mini-game, less score is awarded to them.

The game starts with a menu with options like -
  1. Play the game
  2. View highest score
  3. View score of a particular player (searched by name of player)
  4. Exit

However, options 2 & 3 will show an error if the game has never been played in the particular system as the 'scores.txt' file won't exist. The file 'scores.txt' is created only when the game is played in its entirety atleast once.
A sample 'scores.txt' file is also available and must be stored in the same folder as the code file.
