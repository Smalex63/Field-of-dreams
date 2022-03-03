from database import Database

class Word:
#класс, управляющий процессом открытия слова
	@staticmethod
	def get_letter(letter, name):
		for i in range(len(Database.word)):
		#цикл проверяет наличие буквы в слове и подставляет букву вместо "*" в переменную Database.field
			if Database.word[i] == letter:
				Database.field = Database.field[:i] + letter + Database.field[i + 1:]
			
		if letter in Database.word:
		#если буква есть в слове
			Database.countLetters = 0
			#счётчик одинаковых букв в слове обнуляется
			Database.correct += letter
			#буква добавляется в строку угаданных букв
			Database.allLetters += letter
			#буква добавляется в строку всех названных букв
			Database.answer = True
			#'флаг' верного ответа = True
			for i in Database.word:
				if i == letter:
					Database.countLetters += 1
		else:
		#если буквы в слове нет
			Database.missed += letter
			#буква добавляется в строку ошибочных букв
			Database.allLetters += letter
			#буква добавляется в строку всех угаданных букв
			Database.answer = False
			#'флаг' верного ответа = False
			
		if Database.field == Database.word:
		#если угадано слово
			Database.foundAllLetters = name
			#'флагу' 'открытыВсеБуквы' присваивается имя игрока ( нужно для переключения игровых процессов)
	
			