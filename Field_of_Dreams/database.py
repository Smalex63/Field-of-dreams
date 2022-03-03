from wordbase import *
from choice_prizes import prizeDict
from names import Names

class Database:
#класс, хранящий основные переменные, используемые в игровом процессе
	myName = Names.myName
	#переменная, содержащая имя игрока
	category = category
	#категория, к которой принадлежит загаданное слово (берётся из модуля wordbase)
	word = choiceWord.upper()
	#загаданное слово (берётся из модуля wordbase)
	field = '*' * len(word)
	#поле с закрытыми буквами
	correct = ''
	#отгаданные буквы
	missed = ''
	#ошибочные буквы
	allLetters = ''
	#все названные буквы
	players = {}
	#словарь, содержащий объекты класса Player (игроков)
	allPoints = {}
	#словарь, содержащий имена игроков и их игровые очки
	answer = False
	#'флаг' верного ответа по умолчанию равен False
	countLetters = 0
	#счётчик одинаковых букв в слове (используется для начисления очков)
	foundAllLetters = ''
	#по умолчанию переменная foundAllLetters (открытыВсеБуквы) равна False
	prizeDict = prizeDict
	#словарь, принимающий из модуля choice_prizes наименования призов и их стоимость
	myPrizes = []
	#список призов, выбранных игроком по окончании игры
	myFinishedPoints = 0
	#финишные очки игрока для выбора призов
	
	supergameQuestion = myQuestion
	#вопрос для супер игры (берётся из модуля wordbase)
	supergameAnswer = myAnswer
	#ответ на вопрос для супер игры (берётся из модуля wordbase)
	supergameOpenLetters = openLetters
	#количество букв, которое разрешено назвать игроку в супер игре (берётся из модуля wordbase)
	supergameCalledLetters = ''
	#список названных игроком букв в супер игре 
	
	
	
	