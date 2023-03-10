import sqlite3

conn = sqlite3.connect(':memory:') #C:/Users/lucy.white.207_acc/Documents/Collegg/
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS emulators(
    emulator TEXT,
    path TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS games(
    game TEXT,
    path TEXT,
    emulator TEXT
)''')

conn.commit()

def mainmenu():
    choice = input('''
    Choose an action:
    (1): Add a game
    (2) Add an emulator
    >''')
    match choice:
        case "1":
            add_game()
        case "2":
            add_emulator()

def add_game():
    game = input("Input game name: >")
    path = input("Input path to game: >")
    emulator = input("Input name of emulator for game: >")
    cursor.execute('''
INSERT INTO games (game, path, emulator)
VALUES($1, $2, $3)
    ''', (game, path, emulator)) 

def add_emulator():
    emulator = input("Input name of emulator: >")
    path = input("Input path to emulator: >")
    cursor.execute('''
INSERT INTO emulators (emulator, path)
VALUES($1, $2)
    ''', (emulator, path))

mainmenu()
conn.close()