import sqlite3
import random
conn = sqlite3.connect('coinfliper.db')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Coinflip;
CREATE TABLE Coinflip (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    heads    INTEGER,
    tails    INTEGER,
    percent_heads    INTEGER,
    percent_tails    INTEGER
);
''')
heads=0
tails=0
flip=200
for coin in range(flip):
    coini=random.randint(0,1)
    if coini > 0:
        heads+=1
    else:
        tails+=1
perct=tails/flip
perch=heads/flip
perct*=100
perch*=100
cur.execute('''INSERT OR IGNORE INTO Coinflip (heads, tails, percent_heads, percent_tails) 
    VALUES ( ?, ?, ?, ? )''', ( heads, tails, perct, perch ))
print ('If you flip',flip,'coins at the same time it would be heads',perch,
       'percent and tails',perct,'percent of the time')
tryAgain=input('Do you want to flip again? y/n').lower()
while tryAgain=='y' or tryAgain=='yes':
    heads=0
    tails=0
    for coin in range(flip):
        coini=random.randint(0,1)
        if coini > 0:
            heads+=1
        else:
            tails+=1
    perct=tails/flip
    perch=heads/flip
    perct*=100
    perch*=100
    cur.execute('''INSERT OR IGNORE INTO Coinflip (heads, tails, percent_heads, percent_tails) 
    VALUES ( ?, ?, ?, ? )''', ( heads, tails, perct, perch ))
    print ('If you flip',flip,'coins at the same time it would be heads',perch,
       'percent and tails',perct,'percent of the time')
    tryAgain=input('Do you want to flip again? y/n').lower()
    conn.commit()
else:
    conn.commit()
    quit()
