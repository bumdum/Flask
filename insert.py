import csv, sqlite3

con = sqlite3.connect("C:\\Users\\jboyle\\Desktop\\CurrentWork\\f1\\Flask\\instance\\formula1.sqlite")
cur = con.cursor()

with open('races.csv') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['raceId'], i['year'], i['round'], i['circuitId'], i['name'], i['date'], i['time'], i['url']) for i in dr]

cur.executemany("INSERT INTO t (raceId, year, round, circuitId, name, date, time, url) VALUES (?,?,?,?,?,?,?,?);", to_db)
con.commit()

with open('results.csv') as fun: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fun) # comma is default delimiter
    to_db = [(i['resultId'], i['raceId'], i['driverId'], i['constructorId'], i['number'], i['grid'], i['position'], i['positionText'], i['positionOrder'], i['points'], i['laps'], i['time'], i['milliseconds'], i['fastestLap'], i['rank'], i['fastestLapTime'], i['fastestLapSpeed'], i['statusId']) for i in dr]

cur.executemany("INSERT INTO t (resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, rank, fastestLapTime, fastestLapSpeed, statusId) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
con.commit()
con.close()




