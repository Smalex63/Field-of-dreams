import random

words = {'Животные': 'муравьед колибри пеликан леопард верблюд фламинго броненосец шимпанзе осьминог страус'.split(),
'Фрукты': 'апельсин маракуйя питахайя карамбола нектарин манго авокадо мандарин грейпфрут мангустин'.split(),
'Ягоды': 'черешня виноград клубника крыжовник вишня земляника клюква брусника голубика малина'.split(),
'Овощи': 'морковь картофель редька капуста баклажан патиссон чеснок помидор огурец кабачок'.split(),
'Деревья': 'тополь карагач лиственница ясень баобаб осина яблоня секвойя кипарис береза'.split()}

category = random.choice(list(words.keys()))
index = random.randint(0, len(words) - 1)
choiceWord = words[category][index]

supergameWords = {'Ягоды этого дерева не являются предметом экспорта из за своей хрупкости': ('ШЕЛКОВИЦА', 5), 'Эту одежду американцы называли "таксидо", а англичане "динке джанет"': ('СМОКИНГ', 4), 'Этот старейший метод лечения используется даже дикими животными': ('ГОЛОДАНИЕ', 5), 'Этот продукт изобретен в 1868 году и предназначался для потребления низшими слоями населения и солдатами': ('МАРГАРИН', 4), 'Этот недуг не позволил Илье Репину в преклонном возрасте исправить свою знаменитую картину Иван Грозный и сын его Иван': ('ДАЛЬТОНИЗМ', 5), 'Этот механизм был изобретен в 1868 году. Его первый экземпляр находится в Лондоне': ('СВЕТОФОР', 5), 'Этот материал был известен в Египте и Месопотамии, но в современном виде был получен только в 17 веке': ('ХРУСТАЛЬ', 5), 'Этот зверь при виде врага притворяется мертвым': ('ОПОССУМ', 4)}

myQuestion = random.choice(list(supergameWords.keys()))
myAnswer = supergameWords[myQuestion][0]
openLetters = supergameWords[myQuestion][1]