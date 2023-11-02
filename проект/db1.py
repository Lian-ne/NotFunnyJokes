import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Jokes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               joke TEXT
    )
""")

cursor.execute('''
INSERT INTO Jokes (joke)
VALUES ('Студент отвечает на экзамене, фейлится по полной, думает вот- вот на пересдачу отправят, и говорит профессору: — Профессор, а давайте я за тройку сейчас одной рукой эту парту сломаю? - Но это невозможно... ладно, давайте. Студент размахивается и ударяет по парте, она трескается пополам. Профессор: — Хмм, впечатляет. Ладно, тройку поставлю... — Подождите, а давайте я за четвёрку головой стену пробью? — НУ. давайте. Студент со всей дури бьёт головой о стену, и пробивает её насквозь. Профессор: — Ну так и быть, ставлю четыре... — Подождите, а давайте я за пятёрку на вас одеколоном нассу? — Ну... давайте. Студент расстёгивает ширинку и обоссыввает профессора. Тот принюхивается: — да это же обычная моча! — Ну ладно, ладно, ставьте четыре.')
''')
cursor.execute('''
INSERT INTO Jokes (joke)
VALUES ('Врезается Тойота в новый мерс, стоящий на перекрестке. Из мерса вылазят двое мощных братков, вытаскивают мужика из Тойоты и начинают бить. Тот орет: -Это же Тойота! Те продолжают его усердно бить. Он опять: -Ну мужики, это же Тойота! Ноль внимания. Он опять, уже изнемогая: -Мужики, это же Тойота!!! Ударив ему еще по разу, братки спрашивают: -И чё? -Как что? Водитель-то справа!')
''')
cursor.execute('''
INSERT INTO Jokes (joke)
VALUES ('Рассказывает прапорщик рядовым про танк: — Вот это гусеницы, вот это запаска. Вот это топливный отсек. На танке установлена радиостанция. Один из особо умных солдат спрашивает: — А радиостанция на лампах, или на транзисторах? Прапорщик повернулся, грозно посмотрел на солдат, и как заорет: — ДЛЯ ОСОБО ТУПЫХ, ПОВТОРЯЮ: РАДИОСТАНЦИЯ НА ТАНКЕ')
''')
cursor.execute('''
INSERT INTO Jokes (joke)
VALUES ('Мужик ловит такси: -Куда вам? -Нет, к удавам я не поеду. -Вы меня неправильно поняли. Куда вам надо? -Ну раз надо, поехали к удавам.')
''')
cursor.execute('''
INSERT INTO Jokes (joke)
VALUES ('Я не верю в эволюцию. Если бы это было правдой, то чёрные уже давно были бы пуленепробиваемыми')
''')

conn.commit()

cursor.execute('SELECT * FROM Jokes')
all_jokes = cursor.fetchall()
print('all jokes:')
for i in all_jokes:
    print(i)

conn.close()