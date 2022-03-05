<h1>Поле Чудес</h1>
Игра "Поле Чудес" написана по мотивам одноименного телевизионного шоу. Весь код написан и протестирован на смартфоне в приложении Pydroid 3. Игровое поле также настроено под размеры смартфона.

<h4>Особенности программы:</h4>

В игре участвуют трое игроков: пользователь и два ИИ, которые инициализируются в начале программы. Пользователь становится объектом класса Player, а оппоненты – объектами наследованного класса AiPlayer. 
Методы класса Display в зависимости от игровой ситуации выводят на экран различные данные. Например, в основной игре одновременно выводятся: поле имён игроков и количество их игровых очков, поле слова, поля угаданных и ошибочных букв.<br>
Программа рандомно выбирает слово и категорию, к которой оно относится, из модуля, содержащего соответствующий словарь. В начале каждого хода пользователю предлагается назвать слово целиком. В случае отказа программа рандомно выбирает игровое значение (сектор) из списка, имитирующего барабан из шоу Поле Чудес. В соответствии с этим значением строится дальнейший процесс игры.<br> 
Сектор '0' переводит ход на следующего игрока.<br>
Сектор 'Приз' даёт возможность выбрать приз и выйти из игры, или назвать букву и заработать 2000 очков. Если буква названа неверно, ход переходит к следующему игроку. ИИ, выбравшие приз, исключаются из игрового процесса.<br>
Сектор 'Банкрот' обнуляет очки игрока и переводит ход на следующего.<br>
Сектор '*2' при правильно названной букве удваивает очки игрока.<br>
Все игровые данные записываются в переменные, содержащиеся в отдельном модуле в классе Database.<br>
Специальный модуль word, содержит класс Word, который отвечает за постепенно открывающиеся буквы загаданного слова (изначально буквы заменены знаками *) и контролирует 'флаг' полностью открытого слова.<br>
При открытии слова ИИ, игра завершается.<br>
При открытии слова пользователем из класса Display вызывается метод, выводящий на экран список призов и финишные очки игрока. После выбора призов программа предлагает игроку сыграть в супер игру. <br>
При положительном выборе вызывается ещё один метод класса Display, который выводит вопрос и скрытый ответ, правильные и ошибочные буквы, количество букв, которое игрок может назвать. Все эти данные берутся из класса Database, который в свою очередь черпает их из специального модуля word, содержащего соответствующий словарь.<br>
После этого включается обратный таймер на 60 сек с выводом на экран. По истечении времени игрок называет слово.
