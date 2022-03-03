import  random

#from database import Database

playersNames = 'Иван Сергей Игорь Олег Инна Ольга Андрей Татьяна Анна Карен Илья Кристина Юлия Валентин Мария Марина Дмитрий Александр Алексей Алина Ариадна Валерий Валерия Алтынбек Мутали Вера Евгения'.split()

class Names:
#класс инициализации игроков
	myName = input('Пожалуйста, введите Ваше имя: ')
	print()
	
	@staticmethod
	def player1Name(myName):
	#метод, рандомно выбирающий имя первого ИИ (не позволяет пересечься с именем игрока)
		while True:
			name1 = random.choice(playersNames)
			if name1 != myName:
				player1Name = name1
				return player1Name
				
	@staticmethod
	def player2Name(myName, player1Name):
	#метод, рандомно выбирающий имя второго ИИ (не позволяет пересечься с именами игрока и первого ИИ)
		while True:
			name2 = random.choice(playersNames)
			if name2 != myName and name2 != player1Name:
				player2Name = name2
				return player2Name
