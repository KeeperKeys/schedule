import sqlite3
from dicttoxml import dicttoxml

conn = sqlite3.connect('db.sqlite3')
curs = conn.cursor()
res = curs.execute(
    'SELECT first_name, last_name, middle_name FROM timetable_extuser WHERE user_type==1 OR user_type==0')
all_teacher = res.fetchall()
xml = dicttoxml(all_teacher)
print(xml)

