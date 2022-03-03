from database import Database

class Display:
#класс, выводящий на экран основные данные
	
	@staticmethod
	def get_display():
	#этот метод выводит данные для основной игры
		print('____________________________________________________________')
		print('')
		for i, j in Database.allPoints.items():
			print(i + ': ', end='')
			print(str(j) + ' очков', end='   ')
		print('\n')
		print(f'Загадано слово из категории: {Database.category}')
		print()
		for i in Database.field:
			print(i, end=' ')
		print('')
		print('\nОтгаданные буквы:', end=' ')
		for i in Database.correct:
			print(i, end=' ')
		print()
		print('\nОшибочные буквы:', end=' ')
		for i in Database.missed:
			print(i, end=' ')
		print()
	
	@staticmethod	
	def get_prizes():
	#этот метод выводит данные для экрана выбора призов
		print('____________________________________________________________')
		for i, j in Database.prizeDict.items():
			print(f'{i}).  {j[0]} – {j[1]} очков')
		print()
		print(f'Ваши очки: {Database.myFinishedPoints}')
		print()
		print('Ваши призы:', end=' ')
		for i in Database.myPrizes:
			print(i, end=' ')
		print()
		
	@staticmethod
	def get_super_display():
	#этот метод выводит данные для супер игры
		Database.correct = ''
		Database.missed = ''
		print('____________________________________________________________')
		print(f'ВОПРОС: "{Database.supergameQuestion}"')
		print()
		for i in Database.field:
			print(i, end=' ')
		print('')
		print('\nОтгаданные буквы:', end=' ')
		for i in Database.correct:
			print(i, end=' ')
		print()
		print('\nОшибочные буквы:', end=' ')
		for i in Database.missed:
			print(i, end=' ')
		print()
		
