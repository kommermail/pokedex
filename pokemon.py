#create a database from pdexjson.json that can be used for analysis

import sqlite3
import json

conec=sqlite3.connect('kpokedex.sqlite')
cur=conec.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Pokemon;
DROP TABLE IF EXISTS Types;
DROP TABLE IF EXISTS Weaknesses;
DROP TABLE IF EXISTS Height;
DROP TABLE IF EXISTS Weight;


CREATE TABLE Pokemon (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    types_id INTEGER,
    weaknesses TEXT,
    types TEXT,
    img TEXT,
    spawn_chance REAL,
    height_id INTEGER,
    weight_id INTEGER);

CREATE TABLE Types (id INTEGER PRIMARY KEY AUTOINCREMENT,
    names TEXT);

CREATE TABLE Weaknesses (id INTEGER PRIMARY KEY AUTOINCREMENT,
    names TEXT, weaknesses_num INTEGER);

CREATE TABLE Height (id INTEGER PRIMARY KEY AUTOINCREMENT,
    ht REAL);

CREATE TABLE Weight (id INTEGER PRIMARY KEY AUTOINCREMENT,
    wt REAL)''')
conec.commit()

handle=open('pdexjson.json')

js=json.load(handle)


for item in js['pokemon']:

    name=item['name']
    img=item['img']
    type=str(item['type'])
    height=item['height']
    weight=item['weight']
    spawn_chance=item['spawn_chance']
    weaknesses=str(item['weaknesses'])
    weaknesses_num=len(item['weaknesses'])

    print(name,type,height,weight,spawn_chance,weaknesses)

    cur.execute('''INSERT INTO Types (names) VALUES (?)''', (type, ))
    cur.execute('SELECT id FROM Types WHERE names= ?', (type, ))
    types_id=cur.fetchone()[0]

    cur.execute('''INSERT INTO Weaknesses (names, weaknesses_num) VALUES (?,?)''', (weaknesses, weaknesses_num))
    cur.execute('SELECT id FROM Weaknesses WHERE names= ?', (weaknesses, ))
    weaknesses_id=cur.fetchone()[0]

    cur.execute('''INSERT INTO Height (ht) VALUES (?)''', (height,))
    cur.execute('SELECT id FROM Height WHERE ht=?', (height,))
    height_id=cur.fetchone()[0]

    cur.execute('''INSERT INTO Weight (wt) VALUES (?)''', (weight,))
    cur.execute('SELECT id FROM Weight WHERE wt=?', (weight,))
    weight_id=cur.fetchone()[0]

    cur.execute(''' INSERT INTO Pokemon (name, types_id, weaknesses, types, img, spawn_chance, 
                height_id, weight_id) VALUES (?,?,?,?,?,?,?,?)''',
                  (name, types_id, weaknesses, type, img, spawn_chance,
                        height_id, weight_id,))
    
    conec.commit()

