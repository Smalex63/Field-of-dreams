import time

from player import Player, AiPlayer
from word import Word
from names import Names
from database import Database


def process_game():
	welcome = 'ДОБРО ПОЖАЛОВАТЬ НА "ПОЛЕ ЧУДЕС"!'
	for i in welcome:
		print(i, end='', flush=True)
		time.sleep(0.1)
	print('\n')
	
	myPlayer = Player(Names.myName, 1)
	#инициализация игрока
	aiPlayer1 = AiPlayer(Names.player1Name(myPlayer.name), 2)
	aiPlayer2 = AiPlayer(Names.player2Name(myPlayer.name, aiPlayer1.name), 3)
	#инициализация ещё двух игроков (ИИ)
	
	Database.players = {1: myPlayer, 2: aiPlayer1, 3: aiPlayer2}
	#словарь с перечнем игроков, используемый в игровом цикле
	
	if __name__ == '__main__':
		while True:
			for player in Database.players.values():
				while player.nextPlayer == False:
					if Database.foundAllLetters == myPlayer.name:
						myPlayer.my_choice()
						myPlayer.supergame()
					elif Database.foundAllLetters == aiPlayer1.name or Database.foundAllLetters == aiPlayer2.name:
						print(f'{myPlayer.name}, для Вас игра окончена.')
						exit()	
					else:
						player.get_two_boxes()
						player.spin_wheel(player.get_prize, player.give_word)
						if player.value == '0' or player.value == 'Банкрот':
							break
						elif player.play == False:
							break
						else:
							if Database.foundAllLetters:
								break
							else:
								letter = player.give_letter()
								Word.get_letter(letter, player.name)
								player.process_values()
				player.nextPlayer = False
	
			
process_game()