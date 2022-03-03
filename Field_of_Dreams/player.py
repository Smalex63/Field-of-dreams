import random
import time

from database import Database
from display import Display
from wheel import sectors
from choice_prizes import prizes


class Player(Display):
	
	def __init__(self, name, id):
		self.name = name
		self.id = id
		self.points = 0
		self.value = ''
		self.choicePrize = ''
		self.choicePrizes = []
		self.nextPlayer = False
		self.play = True
		#при значении True переменной происходит переход хода к другому игроку
		self.twoBoxes = 0
		#счетчик букв при достижении 3 позволяет открыть одну из двух 'шкатулок'
		Database.allPoints[self.name] = self.points
		
	def get_two_boxes(self):
		#метод, позволяющий игроку, угадавшему три буквы подряд, открыть одну из двух 'шкатулок', в одной из которых находятся 'деньги'
		if self.twoBoxes == 3:
			print()
			print(f'{self.name}, Вы угадали три буквы подряд и заслужили "две шкатулки". В одной из них находятся деньги, другая – пустая.')
			boxes = ['л', 'п']
			box = random.choice(boxes)
			while True:
				print()
				choiceBox = input(' Какую выбираете: левую или правую? л/п ')
				if choiceBox == box:
				#'правильная шкатулка' добавляет очки и обнуляет счетчик букв
					print()
					print('Поздравляем! Вы выбрали правильно и получаете 2000 рублей!')
					self.points += 2000
					Database.allPoints[self.name] = self.points
					self.twoBoxes = 0
					break
				else:
				#'неправильная шкатулка' обнуляет счетчик букв
					print()
					print('К сожалению, Вы не угадали.')
					self.twoBoxes = 0
					break
		
	def give_word(self):
		if Database.foundAllLetters:
			pass
		else:
			print()
			choiceOpenWord = input(f'{self.name}, хотите ли Вы назвать слово целиком? д/н ').lower()
			if choiceOpenWord == 'д' or choiceOpenWord == 'да':
				print()
				openWord = input('Введите слово: ')
				if openWord.upper() == Database.word:
					Database.foundAllLetters = self.name
					return Database.foundAllLetters
				else:
					print()
					print(f'{self.name}, к сожалению, Вы ошиблись и выбываете из игры. Было загадано слово – {Database.word}.')
					exit()
		
	def get_prize(self):
		self.choicePrize = input(f'{self.name}, вы можете выбрать приз и закончить игру. Либо отказаться от приза и играть дальше. \nИтак, хотите ли вы забрать приз? д/н ').lower()
		print('')
		if self.choicePrize == 'д' or self.choicePrize == 'да':
			print('И.... вам достаётся...')
			print()
			time.sleep(2)
			print(random.choice(prizes))
			time.sleep(2)
			print()
			print('Игра окончена.')
			exit()
		else:
			print(f'{self.name}, вы выбрали игру, и если угадаете букву, получите 2000 очков!')
	
	def spin_wheel(self, get_prize, give_word):
	#метод, рандомно выбирающий значение из списка "sectors' 
		if self.play:
			self.get_display()
			give_word()
			print()
			if Database.foundAllLetters:
				pass
			else:
				print(f'{self.name}, вращайте, пожалуйста, барабан!')
				time.sleep(2)
				print()
				print('Барабан вращается...')
				time.sleep(2)
				self.value = sectors[random.randint(0, len(sectors) - 1)]
				print(f'\nИтак, {self.name}, сектор "{self.value}" на барабане!')
				print()
				time.sleep(2)
				if self.value == '*2':
					if self.points == 0:
						print('У вас 0 очков, но Вы можете назвать букву.')
						print()
						time.sleep(2)
					else:
						print(f'{self.name}, если Вы назовёте правильную букву, все Ваши очки удвоятся!')
						print()
						time.sleep()
				elif self.value == '+':
					print(f'{self.name}, Вы можете открыть любую букву в этом слове!')
					print()
					time.sleep(2)
				elif self.value == '0':
					print(f'{self.name}, к сожалению, ход переходит к следующему игроку.')
					print()
					time.sleep(3)
				elif self.value == 'Банкрот':
					print(f'{self.name}, к сожалению, все Ваши очки "сгорают", и ход переходит к следующему игроку.')
					self.points *= 0
					Database.allPoints[self.name] = self.points
					time.sleep(3)
				elif self.value == 'Приз':
					get_prize()
				else:
					print(f'{self.name}, если Вы назовёте правильную букву, Ваши очки увеличатся на ' + str(self.value) + '!')
					print()
					time.sleep(2)
		else:
			pass
		
		
	def give_letter(self):
	#метод для выбора буквы игроком
		while True:
			if self.value == '+':
				while True:
					try:	
						numLetter = int(input('Введите номер буквы от 1 до ' + str(len(Database.word)) + ': '))
						if numLetter > len(Database.word):
							print('Введите номер буквы от 1 до ', len(Database.word))
							print('')
						elif numLetter == 0:
						#если введён 0
							print('Номер буквы должен быть не меньше 1!')
							print('')
						elif Database.word[numLetter - 1] in Database.correct:
						#если буква под введённым номером уже была открыта
							print('Эта буква уже открыта! Выберите другую.')
							print('')
						else:
							letter = Database.word[numLetter - 1]
							return letter
					except ValueError:
					#если введено не целочисленное значение
						print('\nВведите НОМЕР буквы!')
						print()
			else:
				letter = input('\nВведите букву: ').upper()
				print()
				if len(letter) > 1:
				#если игрок ввёл более одного знака
					print(f'{self.name}, введите ОДНУ букву!')
					print()
				elif  letter not in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'.upper():
				#если игрок ввёл НЕ букву кириллицы
					print(f'{self.name}, введите БУКВУ КИРИЛЛИЦЫ!')
					print('')
				elif letter in Database.allLetters:
				#если буква, введённая игроком, находится в совмещённом списке использованных букв
					print(f'{self.name}, эту букву уже называли. Попробуйте другую.')
					print('')
				else:
					return letter
				
	def process_values(self):
		if self.play:
			if self.value == '+':
				pass
			else:
				if Database.answer == True:
					print('Есть такая буква!')
					time.sleep(2)
					self.twoBoxes += 1
					if Database.countLetters > 1:
						print()
						print('И не одна в этом слове!')
						time.sleep(2)
		
					if self.value == '*2':
						self.points *= 2
					elif self.value == 'Приз':
						self.points += 2000 * Database.countLetters
					else:
						self.points += int(self.value) * Database.countLetters
					Database.allPoints[self.name] = self.points
					print()
				else:
					print('Такой буквы нет, и ход переходит к следующему игроку.')
					self.twoBoxes = 0
					self.nextPlayer = True
					time.sleep(3)
		else:
				pass
				
	def my_choice(self):
		Database.myFinishedPoints += self.points
		print()
		print(f'{Database.myName}, поздравляем! Вы выиграли! Было загадано слово – {Database.word}.')
		print()
		time.sleep(3)
		while True:
			Display.get_prizes()
			print()
			self.choicePrizes = input(f'{self.name}, выберите себе приз, введя его порядковый номер. Если закончили выбор, нажмите на любую букву: ')
			print()
			if Database.myFinishedPoints > 200:
				try:
					values = Database.prizeDict[int(self.choicePrizes)]
					if Database.myFinishedPoints >= values[1]:
						x = Database.prizeDict.pop(int(self.choicePrizes))
						Database.myFinishedPoints -= x[1]
						Database.myPrizes.append(x[0])
					else:
						print('У Вас недостаточно очков.')
						print()
						time.sleep(2)
				except KeyError:
					pass
				except ValueError:
					break
			else:
				print()
				print(f'{Database.myName}, к сожалению, у Вас недостаточно очков, чтобы выбрать призы.')
				print()
				time.sleep(2)
				break
				
	def supergame(self):
		Database.field = '*' * len(Database.supergameAnswer)
		openLetters = False
		supergame = input('Хотите ли Вы сыграть в Супер игру? Если выиграете – получите Супер приз - автомобиль!!! В случае проигрыша Вы лишитесь всех призов. Итак, Супер игра? д/н ').lower()
		print()
		if supergame == 'д' or supergame == 'да':
			while True:
				self.get_super_display()
				if openLetters != True:
					print()
					Database.supergameCalledLetters = input(f'{self.name}, Вы можете назвать {Database.supergameOpenLetters} букв(ы): ').upper()
					print()
					for i in Database.supergameCalledLetters:
						for j in range(len(Database.supergameAnswer)):
							if Database.supergameAnswer[j] == i:
								Database.field = Database.field[:j] + i + Database.field[j + 1:]
								openLetters = True
				else:
					print()
					print('У Вас есть одна минута на размышление. Время пошло.')
					print()
					for sec in reversed(range(10, 60)):
    						print(' ', sec, end='')
    						time.sleep(1)
    						print('\r', end='')
					for sec in reversed(range(1, 10)):
   						print(' ', '0' + str(sec), end='')
    						time.sleep(1)
    						print('\r', end='')
					print('\n')	
					myAnswer = input('Итак, введите слово: ').upper()
					print()
					if myAnswer == Database.supergameAnswer:
						print(f'{self.name}, поздравляем! Вы выиграли и получаете АВТОМОБИЛЬ!!!')
						exit()
					else:
						print(f'{self.name}, к сожалению, Вы не угадали. Загаданное слово – {Database.supergameAnswer}.')
						exit()
		else:
			print('До новых встреч в игре!')
			exit()
			
			
			

class AiPlayer(Player):
	
	def give_word(self):
		pass
	
	def get_prize(self):
		self.choicePrize = random.randint(1,2)
		if self.choicePrize == 1:
			print(f'Итак, {self.name} выбирает приз!')
			time.sleep(3)
			print()
			print(f'{self.name},... Вам достаётся...')
			time.sleep(3)
			print()
			print(random.choice(prizes))
			time.sleep(2)
			print()
			print(f'{self.name}, для Вас игра окончена.')
			self.play = False
			time.sleep(2)
		else:
			print(f'{self.name} выбирает игру, и если угадает букву, получит 2000 очков!')
			time.sleep(2)
	
	def give_letter(self):
		#метод для выбора буквы игроком
		if self.play:
			while True:
				Database.allLetters = Database.correct + Database.missed
				#совмещённый список использованных букв
				if self.value == '+':
					while True:
						numLetter = random.randint(1, len(Database.word)) 
						if Database.word[numLetter-1] not in Database.correct:
							letter = Database.word[numLetter-1]
							print(f'{self.name} выбирает букву под номером {numLetter}')
							time.sleep(3)
							return letter
				else:
					while True:
						letter = random.choice('а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ь ы ъ э ю я'.split()).upper()
						if letter not in Database.allLetters: 
							print(f'{self.name} выбирает букву {letter}')
							print()
							time.sleep(3)
							return letter 
		else:
			self.nextPlayer = True
	
